import pickle
import pandas as pd

# model load karo
with open('house_rent_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_rent(input_dict):
    df = pd.DataFrame(input_dict)
    prediction = model.predict(df)
    return prediction[0]



import streamlit as st 
st.title("Wine Quality Prediction")