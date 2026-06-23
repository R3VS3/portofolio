import streamlit as st
import pandas as pd
import joblib


# 1. PAGE CONFIGURATION

st.set_page_config(
    page_title="Logistics Intelligence | Enterprise",
    page_icon="📊",
    layout="centered"
)


st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; }
    </style>
""", unsafe_allow_html=True)


# 2. MODEL LOADING

@st.cache_resource
def load_model():
    return joblib.load('ecommerce_advanced_model.pkl')

model = load_model()


# 3. INTERFACE (UI)

st.title("Logistics Intelligence Portal")
st.markdown("Automated customer segmentation and routing optimization for enterprise operations.")

st.divider()

with st.form("input_form"):
    st.markdown("### Transaction Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        items_bought = st.number_input("Total Units Purchased", min_value=1, max_value=500, value=1)
        freight_tol = st.number_input("Freight Tolerance ($)", min_value=0.0, max_value=1000.0, value=15.0)
        item_weight = st.number_input("Item Weight (Grams)", min_value=10.0, max_value=100000.0, value=1500.0)
        
    with col2:
        delivery_days = st.number_input("Est. Delivery Time (Days)", min_value=0, max_value=90, value=7)
        is_metro = st.selectbox("Destination Zone", options=["Metropolitan Area", "Regional / Remote Area"])
        metro_val = 1 if "Metropolitan" in is_metro else 0
        
    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Execute Routing Analysis", type="primary")


# 4. PREDICTION LOGIC

if submitted:
    input_data = pd.DataFrame({
        'Total_Items_Bought': [items_bought],
        'Avg_Freight_Tolerance': [freight_tol],
        'Avg_Delivery_Days': [delivery_days],
        'Avg_Item_Weight_g': [item_weight],
        'Is_Metro_City': [metro_val]
    })
    
    prediction = model.predict(input_data)[0]
    
    st.divider()
    st.markdown("### System Decision")
    

    if prediction == 1:
        st.subheader("Classification: METRO REGULAR")
        st.info("Efficient shipping lane. Recommended: Standard courier service.")
    
    elif prediction == 0:
        st.subheader("Classification: VIP / HEAVY-CARGO")
        st.warning("High-value/Heavy-load logistics detected. Recommended: Specialized handling and escalated CS oversight.")
        
    elif prediction == 2:
        st.subheader("Classification: REGIONAL REGULAR")
        st.info("Extended logistics lane. Recommended: Enhanced packaging and extended delivery tracking.")