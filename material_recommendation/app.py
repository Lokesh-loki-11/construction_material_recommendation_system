import streamlit as st
import pandas as pd
import hashlib

# ---------- User Authentication ----------
users_db = {"admin": hashlib.sha256("admin".encode()).hexdigest()}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_ui():
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users_db and users_db[username] == hash_password(password):
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.session_state["page"] = "recommend"
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

def register_ui():
    st.subheader("📝 Register")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Register"):
        if new_username in users_db:
            st.warning("Username already exists.")
        else:
            users_db[new_username] = hash_password(new_password)
            st.success("Registered successfully! Please log in.")

# ---------- Session Setup ----------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# ---------- UI Routing ----------
if st.session_state["page"] == "home":
    col1, col2 = st.columns([8, 2])
    with col1:
        st.title("Construction Material Recommendation System")
    with col2:
        if not st.session_state["logged_in"]:
            if st.button("Login/Register"):
                st.session_state["page"] = "auth"
                st.rerun()
        else:
            if st.button("Logout"):
                st.session_state["logged_in"] = False
                st.session_state["user"] = None
                st.session_state["page"] = "home"
                st.rerun()

    st.markdown("""
        <p style='font-size:18px;'>This system recommends suitable construction materials based on strength, cost, water resistance, and durability.</p>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("🏗️ Material Recommend"):
        st.session_state["page"] = "recommend"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state["page"] == "auth":
    auth_mode = st.radio("Select Option", ["Login", "Register"])
    if auth_mode == "Login":
        login_ui()
    else:
        register_ui()

elif st.session_state["page"] == "recommend":
    # ---------- Optional Sidebar User Info ----------
    if st.session_state["logged_in"]:
        with st.sidebar:
            st.markdown("## 👤 User Panel")
            st.markdown(f"**Username:** `{st.session_state['user']}`")
            if st.button("🚪 Logout"):
                st.session_state["logged_in"] = False
                st.session_state["user"] = None
                st.session_state["page"] = "home"
                st.rerun()

    # ---------- Load Datasets ----------
    @st.cache_data
    def load_datasets():
        return {
            "Bricks": pd.read_csv("Bricks_products_list_200.csv"),
            "Cement": pd.read_csv("Cement_Product_List_200_Modified.csv"),
            "Concrete": pd.read_csv("Concrete_Product_List_200_Modified.csv"),
            "Steel": pd.read_csv("Steel_Product_List_200_Modified.csv"),
            "Wood": pd.read_csv("Wood_Product_List_200_Modified.csv"),
            "Iron": pd.read_csv("Iron_Product_List_200_Modified.csv"),
            "Aggregate": pd.read_csv("aggregate_product_list_200.csv"),
        }

    datasets = load_datasets()

    st.title("Material Recommendation System")

    # ---------- Material Input UI ----------
    material_type = st.selectbox("Material Type", list(datasets.keys()))
    level_map = {"Low": 3, "Medium": 6, "High": 9}

    strength_input = st.selectbox("Strength", list(level_map.keys()))
    cost_input = st.selectbox("Cost", list(level_map.keys()))
    water_res_input = st.selectbox("Water Resistance", list(level_map.keys()))
    durability_input = st.selectbox("Durability", list(level_map.keys()))

    strength = level_map[strength_input]
    cost = level_map[cost_input]
    water_resistance = level_map[water_res_input]
    durability = level_map[durability_input]

    # ---------- Recommendation Logic ----------
    if st.button("🔍 Recommend Materials"):
        df = datasets[material_type].copy()

        df["Strength"] = df["Strength"].map(level_map)
        df["Cost"] = df["Cost"].map(level_map)
        df["Water Resistance"] = df["Water Resistance"].map(level_map)
        df["Durability"] = df["Durability"].map(level_map)

        df = df.dropna(subset=["Strength", "Cost", "Water Resistance", "Durability"])

        def score(row):
            return (
                -abs(row["Strength"] - strength)
                -abs(row["Water Resistance"] - water_resistance)
                -abs(row["Cost"] - cost)
                -abs(row["Durability"] - durability)
            )

        try:
            df["score"] = df.apply(score, axis=1)
            top_matches = df.sort_values(by="score", ascending=False).head(6)

            st.subheader("🔝 Top Recommended Materials:")
            for _, row in top_matches.iterrows():
                st.markdown(
                    f"""
                    <div style='
                        background-color: #1e1e1e;
                        border: 1px solid #444;
                        border-radius: 10px;
                        padding: 15px;
                        margin-bottom: 15px;
                    '>
                        <h4 style='color: #ffcc00;'> {row['Name']}</h4>
                        <p><strong>🔧 Application:</strong> {row['Application']}</p>
                        <p><strong>🌱 Eco-Friendly:</strong> {row['Eco-Friendly']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        except Exception as e:
            st.error(f"Error: {e}")
