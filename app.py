import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Kepler Exoplanet Predictor", page_icon="🌌")
st.title("🌌 Kepler Exoplanet Predictor")
st.write("Enter the observed planet characteristics below to predict if it is a CONFIRMED exoplanet or a FALSE POSITIVE.")

# Load the downloaded model and scaler
@st.cache_resource
def load_model():
    with open("kepler_xgb_model.pkl", "rb") as f:
        return pickle.load(f)

data = load_model()
model = data["model"]
scaler = data["scaler"]

# User interface inputs matching your key dataset metrics
st.header("🔭 Transit & Star Properties")
col1, col2 = st.columns(2)

with col1:
    koi_fpflag_nt = st.selectbox("Not Transit-Like Flag (koi_fpflag_nt)", [0, 1], help="Is the signature transit-like?")
    koi_fpflag_ss = st.selectbox("Stellar Eclipse Flag (koi_fpflag_ss)", [0, 1], help="Is there a flag for a binary star eclipse?")
    koi_period = st.number_input("Orbital Period (days)", value=10.0)

with col2:
    koi_duration = st.number_input("Transit Duration (hours)", value=3.0)
    koi_depth = st.number_input("Transit Depth (ppm)", value=500.0)
    koi_kepmag = st.number_input("Kepler Magnitude (koi_kepmag)", value=15.0)

# When the user clicks the predict button
if st.button("🔮 Run Prediction", type="primary"):
    # Create an input array mapping to the exact structural shape your X matrix expects.
    # Note: Because your notebook generated 2,000+ columns from pd.get_dummies, 
    # we initialize a zero-array matching the model's exact expected feature length:
    expected_features = model.get_booster().feature_names
    input_data = pd.DataFrame(0.0, index=[0], columns=expected_features)
    
    # Map your inputs safely into their respective feature spots
    if "koi_fpflag_nt" in input_data.columns: input_data["koi_fpflag_nt"] = koi_fpflag_nt
    if "koi_fpflag_ss" in input_data.columns: input_data["koi_fpflag_ss"] = koi_fpflag_ss
    if "koi_period" in input_data.columns: input_data["koi_period"] = koi_period
    if "koi_duration" in input_data.columns: input_data["koi_duration"] = koi_duration
    if "koi_depth" in input_data.columns: input_data["koi_depth"] = koi_depth
    if "koi_kepmag" in input_data.columns: input_data["koi_kepmag"] = koi_kepmag

    # Scale inputs using your saved scaler
    scaled_features = scaler.transform(input_data)
    
    # Execute prediction
    prediction = model.predict(scaled_features)
    
    st.markdown("---")
    if prediction[0] == 1:
        st.success("### 🎉 Prediction: CONFIRMED EXOPLANET!")
    else:
        st.error("### ❌ Prediction: FALSE POSITIVE / CANDIDATE")