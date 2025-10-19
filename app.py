# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:14:20 2025

@author: Admin
"""

import pickle
import pandas as pd
import numpy as np
import streamlit as st


# Load the trained model
loaded_model = pickle.load(open('C:/Users/Benjamin/Desktop/HOUSE PRICE/house_sales_data.sav', 'rb'))

def house_price_prediction(Square_Footage,Num_Bedrooms,Num_Bathrooms,Year_Built,Lot_Size,Garage_Size,Neighborhood_Quality):
     
    # Create DataFrame from input
    new_house = pd.DataFrame([{
        'Square_Footage': 1360,
        'Num_Bedrooms': 2,
        'Num_Bathrooms': 1,
        'Year_Built':1981,
        'Lot_Size': 0.59963664,
        'Garage_Size': 0,
        'Neighborhood_Quality': 5,
    }])
    
    # Predict price
    predicted_house = loaded_model.predict(new_house)
    
    # Return the prediction
    return predicted_house[0]
# Main Streamlit app
def main():
    st.title("house Price Prediction")

    # Input fields for all features
    Square_Footage = st.text_input('Square_Footage (numeric code, e.g., 1360)')
    Num_Bedrooms = st.text_input('Num Bedrooms (e.g., 2)')
    Num_Bathrooms = st.text_input('Num_Bathrooms (e.g., 1)')
    Year_Built = st.text_input('Year_Built (e.g., 1981)')
    Lot_Size = st.text_input('Lot_Size (numeric code, e.g., 8)')
    Garage_Size = st.text_input('Garage_Size (e.g., 0)')
    Neighborhood_Quality = st.text_input('Neighborhood_Quality (e.g., 5)')
    

    if st.button('Predict house Price'):
        try:
        # Convert inputs to numeric types
         Square_Footage = float(Square_Footage)
         Num_Bedrooms = float(Num_Bedrooms)
         Num_Bathrooms = float( Num_Bathrooms)
         Year_Built = int(Year_Built)
         Lot_Size = int(Lot_Size)
         Garage_Size = int(Garage_Size)
         Neighborhood_Quality = float(Neighborhood_Quality)
       

        # Call the prediction function (just fix indentation)
         price = house_price_prediction(Square_Footage,Num_Bedrooms,Num_Bathrooms,
                                        Year_Built,Lot_Size,Garage_Size,Neighborhood_Quality  )
      

         st.success(f'The predicted price for the house is: RWF {price:.2f}')
        except ValueError:
            
         st.error("Please enter valid numeric values for all inputs.")
         
if __name__ == '__main__':
    main()         