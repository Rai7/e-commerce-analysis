import streamlit as st
import pandas as pd
import pickle

# Load the saved model from the pickle file
model_filename = 'ratings_model.pkl'
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Function to predict ratings based on user input
def predict_ratings(page_views, price):
    input_data = pd.DataFrame({'page_views': [page_views], 'price': [price]})
    prediction = loaded_model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.sidebar.image('totebag.jpg', use_column_width=True)  # Image in the sidebar

# Main content area
st.title('Rating Prediction App')
st.image('machine.jpg', use_column_width=True)  # Image in the main content area

# Input fields for page_views and price
page_views = st.number_input('Enter Page Views:', min_value=0)
price = st.number_input('Enter Price:', min_value=0.0)

# Button to trigger prediction
if st.button('Predict Ratings'):
    # Predict ratings and display the result
    prediction_result = predict_ratings(page_views, price)
    st.success(f'Predicted Ratings: {prediction_result:.2f}')
