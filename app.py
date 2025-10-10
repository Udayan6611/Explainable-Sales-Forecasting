import streamlit as st
import pandas as pd
import joblib
import lightgbm
import shap
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(
    page_title="Sales Forecasting App",
    page_icon="📈",
    layout="wide"
)

# --- Caching Functions ---
@st.cache_data
def load_model_and_data():
    """Loads the pre-trained model and validation data."""
    model = joblib.load('lgbm_model.joblib')
    X_val = joblib.load('X_val.joblib')
    y_val = joblib.load('y_val.joblib')
    return model, X_val, y_val

@st.cache_data
def calculate_shap_values(_model, _data):
    """Calculates SHAP values for the given model and data."""
    explainer = shap.TreeExplainer(_model)
    shap_values = explainer.shap_values(_data)
    return explainer, shap_values

# --- Load Data ---
model, X_val, y_val = load_model_and_data()

# --- Sidebar ---
with st.sidebar:
    st.header("Project Information")
    st.write("""
    This app uses a LightGBM model to forecast sales for a large Ecuadorian retailer.
    It's a portfolio project demonstrating data cleaning, feature engineering, model training, and explainable AI.
    """)
    st.write("---")
    st.write("**Author:** Udayan Dusane")
    st.write("**GitHub Repo:** [Link to your repo]")

# --- App Title ---
st.title("Explainable Sales Forecasting Dashboard")

# --- Create Tabs ---
tab1, tab2 = st.tabs(["Global Feature Importance", "Individual Prediction Analysis"])

with tab1:
    st.header("Understanding the Model's Overall Behavior")
    st.write("""
    This plot shows the most important features, ranked by their impact on the model's predictions across the entire validation dataset. It explains the general logic of the model.
    """)
    with st.spinner("Calculating global feature importances..."):
        explainer, shap_values = calculate_shap_values(model, X_val)
        
        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, X_val, show=False, plot_size=None)
        st.pyplot(fig, width='stretch')

with tab2:
    st.header("Analyzing a Single Prediction")
    st.write("""
    Use the slider to select a specific prediction from the validation set. You can see the model's forecast, the actual sales, and a breakdown of how the model arrived at its decision.
    """)
    
    row_index = st.slider("Select a prediction to analyze:", 0, len(X_val)-1, 100)
    
    st.subheader(f"Analysis for Prediction #{row_index}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Model's Prediction", f"{model.predict(X_val.iloc[[row_index]])[0]:.2f}")
    with col2:
        st.metric("Actual Sales", f"{y_val.iloc[row_index]:.2f}")
    
    st.subheader("Features for this Prediction")
    st.dataframe(X_val.iloc[[row_index]])
    
    st.subheader("SHAP Force Plot")
    st.write("""
    This plot shows how each feature contributed to this specific prediction. Features in red pushed the prediction higher, while features in blue pushed it lower.
    """)
    explainer, shap_values = calculate_shap_values(model, X_val)
    
    # Generate the force plot and capture the current Matplotlib figure
    shap.force_plot(explainer.expected_value, shap_values[row_index, :], X_val.iloc[row_index, :], matplotlib=True, show=False)
    fig = plt.gcf() # Get current figure
    st.pyplot(fig, bbox_inches='tight')
    plt.clf() # Clear the figure to prevent it from showing up on other pages