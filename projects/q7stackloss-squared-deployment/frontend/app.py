import streamlit as st
import requests
import json
import numpy as np
import os

def predict(data: dict) -> float:
    """Make Prediction using the API endpoint"""
    # url = "http://localhost:8000/predict"
    url = os.environ.get('API_URL', 'http://api:8000/predict')
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error calling API: {str(e)}")
        return None

def main():
    if 'history' not in st.session_state:
        st.session_state.history = []    
    st.title("Stackloss Prediction App")
    st.write("Enter values for Prediction:")

    # Create input fields for the 5 features
    col1, col2 = st.columns(2)
    
    with col1:
        feature1 = st.number_input("Air Flow", value=80.0)
        feature2 = st.number_input("Water Temp", value=27.0)
        feature3 = st.number_input("Acid Conc.", value=89.0)
    
    with col2:
        feature4 = st.number_input("AFsquared", value=42.0)
        feature5 = st.number_input("WTsquared", value=95.0)

    # Input validation
    if feature1 < 0 or feature2 < 0:
        st.error("Values cannot be negative")
        return        

    # Create a button to trigger Prediction
    if st.button("Predict"):
        # Prepare the input data
        input_data = {
            "X": [feature1, feature2, feature3, feature4, feature5]
        }

        # Show the input data
        st.write("Input data:", input_data)

        # Get Prediction
        # result = predict(input_data)
        with st.spinner("Making Prediction..."):
            result = predict(input_data)        
        
        if result:          
            # Display history
            st.write("---")
            st.write("Prediction History")
            for i, item in enumerate(st.session_state.history):
                st.write(f"Prediction {i+1}:")
                st.write(f"Input: {item['input']}")
                st.write(f"Prediction: {item['Prediction']:.2f}")

            st.success(f"Prediction: {result['Prediction']:.2f}")

            # Create a bar chart of input features
            st.write("Feature Values")
            st.bar_chart(
                data=input_data["X"],
                use_container_width=True
            )

            # Optional: Display additional information
            st.write("---")
            st.write("Prediction Details:")
            st.json(result)

            st.session_state.history.append({
                'input': input_data,
                'Prediction': result['Prediction']
            })            

if __name__ == "__main__":
    main()
