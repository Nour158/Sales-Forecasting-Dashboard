import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Walmart Weekly Sales Prediction",
    page_icon="🏪",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

div[data-testid="metric-container"]{
    background-color:white;
    border-radius:10px;
    padding:15px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.10);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("random_forest_model.pkl")

# ==========================================
# TITLE
# ==========================================

st.title("🏪 Walmart Weekly Sales Prediction")

st.markdown("""
Predict **Weekly Walmart Sales** using a **Random Forest Regression** model trained on the Walmart Sales Dataset.
""")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📘 Project Information")

st.sidebar.info("""
### Walmart Sales Prediction

**Model**

Random Forest Regressor

---

**Dataset**

Walmart Weekly Sales Dataset

---

**Performance**

✅ R² Score : **0.959**

✅ MAE : **62,144**

✅ RMSE : **114,411**

---

Developer

**Nourallah Ghonim**

AI & Robotics Student
""")

# ==========================================
# MODEL METRICS
# ==========================================

st.subheader("📊 Model Performance")

metric1, metric2, metric3 = st.columns(3)

metric1.metric("R² Score", "0.959")
metric2.metric("MAE", "62,144")
metric3.metric("RMSE", "114,411")

st.divider()

# ==========================================
# USER INPUT
# ==========================================

st.subheader("📝 Enter Input Features")

left, right = st.columns(2)

with left:

    store = st.number_input(
        "Store",
        min_value=1,
        max_value=45,
        value=1
    )

    holiday = st.selectbox(
        "Holiday",
        ["No", "Yes"]
    )

    holiday = 1 if holiday == "Yes" else 0

    temperature = st.number_input(
        "Temperature",
        value=60.0
    )

    fuel_price = st.number_input(
        "Fuel Price",
        value=3.5
    )

with right:

    cpi = st.number_input(
        "Consumer Price Index (CPI)",
        value=180.0
    )

    unemployment = st.number_input(
        "Unemployment Rate",
        value=7.5
    )

    date = st.date_input("Select Date")

# ==========================================
# FEATURE ENGINEERING
# ==========================================

year = date.year
month = date.month
week = date.isocalendar().week
quarter = (month - 1) // 3 + 1

# ==========================================
# CREATE INPUT DATAFRAME
# ==========================================

input_data = pd.DataFrame({

    "Store":[store],
    "Holiday_Flag":[holiday],
    "Temperature":[temperature],
    "Fuel_Price":[fuel_price],
    "CPI":[cpi],
    "Unemployment":[unemployment],
    "Year":[year],
    "Month":[month],
    "Week":[week],
    "Quarter":[quarter]

})

# ==========================================
# PREDICTION
# ==========================================

st.divider()

if st.button("🚀 Predict Weekly Sales"):

    prediction = model.predict(input_data)

    st.markdown(f"""
    <div style="
        background:#198754;
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;
    ">

    <h2>💰 Predicted Weekly Sales</h2>

    <h1>${prediction[0]:,.2f}</h1>

    </div>
    """, unsafe_allow_html=True)

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

st.divider()

st.subheader("📈 Feature Importance")

importance = pd.DataFrame({

    "Feature":[
        "Store",
        "CPI",
        "Unemployment",
        "Week",
        "Temperature",
        "Fuel Price",
        "Month",
        "Holiday",
        "Year",
        "Quarter"
    ],

    "Importance":[
        0.663322,
        0.153702,
        0.104246,
        0.049739,
        0.012988,
        0.010162,
        0.002897,
        0.001740,
        0.000967,
        0.000238
    ]

})

fig = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    color_continuous_scale="Blues",
    title="Random Forest Feature Importance"
)

fig.update_layout(yaxis=dict(categoryorder="total ascending"))

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODEL COMPARISON
# ==========================================

st.divider()

st.subheader("📊 Model Comparison")

comparison = pd.DataFrame({

    "Model":[
        "Linear Regression",
        "Decision Tree",
        "Random Forest"
    ],

    "MAE":[
        433270,
        75320,
        62144
    ],

    "RMSE":[
        521853,
        136002,
        114411
    ],

    "R² Score":[
        0.155,
        0.943,
        0.959
    ]

})

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

# ==========================================
# ABOUT
# ==========================================

st.divider()

st.subheader("ℹ️ About This Project")

st.info("""
This application predicts Walmart Weekly Sales using a **Random Forest Regression** model.

### Project Workflow

- Business Understanding
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Comparison
- Feature Importance Analysis
- Model Deployment with Streamlit

### Technologies Used

- Python
- Pandas
- Scikit-learn
- Plotly
- Streamlit
- Joblib
""")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Built by Nourallah Ghonim | AI & Robotics Student"
)