# 🏪 Walmart Weekly Sales Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

This project predicts **Walmart weekly sales** using Machine Learning.

The complete workflow includes:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Comparison
- Feature Importance Analysis
- Model Deployment using Streamlit

---

## 🌐 Live Demo

Try the deployed application here:

### **https://sales-forecasting-dashboard-ctbxtutnrddlv26btxt4ui.streamlit.app/**

---

## 📊 Dataset

The dataset contains historical weekly sales information collected from Walmart stores.

### Features

- Store
- Date
- Holiday Flag
- Temperature
- Fuel Price
- CPI
- Unemployment

### Target

- Weekly Sales

---

## 🤖 Models Evaluated

| Model | MAE | RMSE | R² |
|--------|------------:|------------:|---------:|
| Linear Regression | 433,270 | 521,853 | 0.155 |
| Decision Tree | 75,320 | 136,002 | 0.943 |
| **Random Forest** | **62,144** | **114,411** | **0.959** |

After comparing multiple regression models, **Random Forest** achieved the highest predictive performance and was selected as the final model for deployment.

---

## 📈 Feature Importance

The most influential features were:

1. Store
2. CPI
3. Unemployment
4. Week

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit web application where users can estimate weekly Walmart sales by entering:

- Store
- Date
- Holiday Flag
- Temperature
- Fuel Price
- CPI
- Unemployment

The application instantly predicts the expected weekly sales using the trained **Random Forest** model.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Nour158/Walmart-Sales-Prediction.git
```

Navigate into the project:

```bash
cd Walmart-Sales-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

Add a screenshot of the deployed application here.

```text
images/dashboard.png
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Joblib

---

## 📁 Project Structure

```text
Walmart-Sales-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── models/
│   ├── random_forest_model.pkl
│   └── preprocessor.pkl
├── data/
│   └── Walmart.csv
├── notebooks/
│   └── Walmart_Sales_Prediction.ipynb
└── images/
    └── dashboard.png
```

---

## 👨‍💻 Author

**Nourallah Ghonim**

Artificial Intelligence & Robotics Student

Machine Learning • Deep Learning • Computer Vision • Robotics
