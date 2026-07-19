# 🏪 Walmart Weekly Sales Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview

This project predicts Walmart weekly sales using Machine Learning.

The workflow includes:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Comparison
- Feature Importance Analysis
- Model Deployment using Streamlit

---

## 📊 Dataset

The dataset contains historical weekly sales information from Walmart stores.

Features include:

- Store
- Date
- Holiday Flag
- Temperature
- Fuel Price
- CPI
- Unemployment

Target:

- Weekly Sales

---

## 🤖 Models Evaluated

| Model | MAE | RMSE | R² |
|--------|------------:|------------:|---------:|
| Linear Regression | 433,270 | 521,853 | 0.155 |
| Decision Tree | 75,320 | 136,002 | 0.943 |
| **Random Forest** | **62,144** | **114,411** | **0.959** |

Random Forest achieved the best performance and was selected as the final model.

---

## 📈 Feature Importance

The most important features were:

1. Store
2. CPI
3. Unemployment
4. Week

---

## 🖥️ Streamlit Application

The trained model was deployed using Streamlit.

Users can enter:

- Store
- Holiday
- Temperature
- Fuel Price
- CPI
- Unemployment
- Date

and instantly receive a prediction for weekly sales.

---

## 🚀 Installation

```bash
git clone https://github.com/Nour158/Walmart-Sales-Prediction.git

cd Walmart-Sales-Prediction

pip install -r requirements.txt

streamlit run app.py
```

---

## 📸 Application Preview

Add your screenshot here.

```
images/dashboard.png
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Joblib

---

## 👨‍💻 Author

**Nourallah Ghonim**

Artificial Intelligence & Robotics Student

Machine Learning | Robotics | Computer Vision