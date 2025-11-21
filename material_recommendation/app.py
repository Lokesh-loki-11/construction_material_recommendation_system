import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------- LOAD PICKLE MODEL ----------------------
@st.cache_resource
def load_model():
    with open("product_recommender.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()
preprocessor = model["preprocessor"]
filtered_df = model["filtered_df"]
X = model["X"]

# ---------------------- UI ----------------------
st.title("🏗 Construction Material Recommendation System")
st.write("Provide your requirements to get the best material recommendations.")

# ----------- User Input UI -----------
material_type = st.selectbox(
    "Material Type",
    sorted(filtered_df["Material Type"].unique())
)

cost = st.selectbox(
    "Cost",
    sorted(filtered_df["Cost"].unique())
)

durability = st.selectbox(
    "Durability",
    sorted(filtered_df["Durability"].unique())
)

strength = st.selectbox(
    "Strength",
    sorted(filtered_df["Strength"].unique())
)

water_res = st.selectbox(
    "Water Resistance",
    sorted(filtered_df["Water Resistance"].unique())
)

# ----------- Recommend Button -----------
if st.button("🔍 Recommend Materials"):
    try:
        # Build user input vector
        user_df = pd.DataFrame([{
            "Material Type": material_type,
            "Cost": cost,
            "Durability": durability,
            "Strength": strength,
            "Water Resistance": water_res
        }])

        # Vectorize using preprocessor
        user_vector = preprocessor.transform(user_df)

        # Similarity scores
        similarities = cosine_similarity(user_vector, X).flatten()

        # Top 3 recommendations
        top_idx = similarities.argsort()[::-1][:3]
        top_results = filtered_df.iloc[top_idx]

        st.subheader("🔝 Top Recommended Materials")

        # Display cards
        for _, row in top_results.iterrows():
            st.markdown(f"""
                <div style='background-color:#1e1e1e;border:1px solid #444;
                padding:15px;border-radius:10px;margin-bottom:15px;'>
                    <h4 style='color:#ffcc00;'> {row['Name']} </h4>
                    <p><b>📦 Application:</b> {row['Application']}</p>
                    <p><b>🏗 Material Type:</b> {row['Material Type']}</p>
                </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {e}")
