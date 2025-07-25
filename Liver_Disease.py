import streamlit as st
import pandas as pd
import pickle


# Load the Logistic Regression model
model_path = "C:/Users/Think/Downloads/Liver_Disease/logistic_regression_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Logistic Regression Model Deployment")

# Sidebar for user input
st.header("Enter Your Details to Predict Liver Disease Risks")

# Function to collect user input
def user_input_features():
    st.write("### Please provide the following details:")
    age = st.slider("Age (years)", min_value=0, max_value=100, value=30)
    albumin = st.slider("Albumin (g/dL)", min_value=34.0, max_value=54.0, value=40.0, step=0.1)
    alkaline_phosphatase = st.slider("Alkaline Phosphatase (U/L)", min_value=40, max_value=129, value=80)
    alanine_aminotransferase = st.slider("Alanine Aminotransferase (U/L)", min_value=7, max_value=55, value=25)
    aspartate_aminotransferase = st.slider("Aspartate Aminotransferase (U/L)", min_value=8, max_value=48, value=25)
    bilirubin = st.slider("Bilirubin (mg/dL)", min_value=1.0, max_value=12.0, value=5.0, step=0.1)
    cholinesterase = st.slider("Cholinesterase (U/L)", min_value=8, max_value=18, value=12)
    cholesterol = st.slider("Cholesterol (mmol/L)", min_value=0.0, max_value=5.2, value=3.0, step=0.1)
    gamma_glutamyl_transferase = st.slider("Gamma Glutamyl Transferase (IU/L)", min_value=0, max_value=50, value=25)
    protein = st.slider("Protein (mg)", min_value=0.0, max_value=80.0, value=40.0, step=0.1)
    
    # Create a DataFrame with the inputs
    data = {
        'age': age,
        'albumin': albumin,
        'alkaline_phosphatase': alkaline_phosphatase,
        'alanine_aminotransferase': alanine_aminotransferase,
        'aspartate_aminotransferase': aspartate_aminotransferase,
        'bilirubin': bilirubin,
        'cholinesterase': cholinesterase,
        'cholesterol': cholesterol,
        'gamma_glutamyl_transferase ': gamma_glutamyl_transferase,
        'protein   ': protein
    }
    return pd.DataFrame(data, index=[0])

# Get user input
input_df = user_input_features()



# Make predictions
if st.button("Predict"):
    prediction = model.predict(input_df)
    prediction_category = {
        0: "No Disease",
        1: "Cirrhosis",
        2: "Hepatitis",
        3: "Fibrosis",
        5: "Suspect Disease"
    }.get(prediction[0], "No Disease")
    st.write(f"### Prediction: {prediction_category}")

