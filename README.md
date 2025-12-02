# Construction Material Recommendation System (Content-Based ML)

## 📌 Overview

The **Construction Material Recommendation System** is a content-based machine learning project that recommends the best construction materials based on user-defined features such as:

* Cost
* Durability
* Strength
* Water Resistance
* Material Type

The system compares user input with a database of 1000+ construction materials and returns the **Top-N most similar materials** using **cosine similarity**.

---

## 🎯 Objectives

* Recommend construction materials using a similarity-based approach.
* Provide a fast, automated decision-support tool for engineers and buyers.
* Build a scalable and explainable ML system.
* Save the trained pipeline using Pickle for deployment.

---

## 🧩 Features

### ✔ Content-based recommendations (Cosine Similarity)

### ✔ Clean modular code

### ✔ Multiple dataset support

### ✔ Evaluation metrics included

### ✔ Deployable using Streamlit

---

## 📁 Dataset Details

Seven datasets were used:

* Steel product list 
* Iron product list 
* Wood product list 
* Concrete product list 
* Cement product list 
* Aggregate product list 
* Bricks product list

Each dataset contains:

* Name
* Material Type
* Cost
* Durability
* Strength
* Water Resistance
* Application

---

## 🏗 Project Architecture

```
📦 Material Recommendation System
 ┣ 📂 data
 ┃ ┣ Steel_Product_List_200_Modified.csv
 ┃ ┣ Iron_Product_List_200_Modified.csv
 ┃ ┣ Wood_Product_List_200_Modified.csv
 ┃ ┣ Concrete_Product_List_200_Modified.csv
 ┃ ┣ Cement_Product_List_200_Modified.csv
 ┃ ┣ aggregate_product_list_200.csv
 ┃ ┗ Bricks_products_list_200.csv
 ┣ 📂 model
 ┣ ┗ material recommendaton.ipynb
 ┃ ┗ product_recommender.pkl
 ┣ 📄 app.py
 ┗ 📄 README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-Learn**
* **Cosine Similarity**
* **OneHotEncoder**
* **Pickle**
* **Streamlit** (optional for UI)

---

## 🔧 Installation

```bash
pip install pandas numpy scikit-learn streamlit pickle
```

---

## 🧹 Data Preprocessing Steps

1. Load all datasets
2. Combine into a single DataFrame
3. Remove missing values
4. Select important features
5. Apply OneHotEncoding to categorical fields
6. Save preprocessor and data as Pickle

---

## 🤖 Machine Learning Approach

The project uses **content-based filtering**:

* Convert categorical features to vectors using **OneHotEncoder**
* Apply **cosine similarity** to find closest matches
* Rank products based on similarity scores

---

## 📘 Core Code Structure

### 1. Load and preprocess data

### 2. Fit OneHotEncoder

### 3. Transform data into vectors

### 4. Implement recommendation using cosine similarity

### 5. Save model using pickle

### 6. Streamlit 

---

## 🌐 Streamlit App 

Run the application:

```bash
streamlit run app.py
```

---

## 📝 Future Improvements

* Add hybrid ML classification (predict material type)
* Add application-based recommendations
* Add user history for personalized ranking
* Deploy as a web application with database

---

## 👨‍💻 Author

**Asi Lokesh**
Beginner in Machine Learning & Data Science.

