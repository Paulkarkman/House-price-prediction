
import pickle
import pandas as pd
import numpy as np
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('house_sales_data.sav', 'rb'))

# Prediction function
def house_price_prediction(Square_Footage, Num_Bedrooms, Num_Bathrooms, Year_Built, Lot_Size, Garage_Size, Neighborhood_Quality):
    # Use actual user input values
    new_house = pd.DataFrame([{
        'Square_Footage': Square_Footage,
        'Num_Bedrooms': Num_Bedrooms,
        'Num_Bathrooms': Num_Bathrooms,
        'Year_Built': Year_Built,
        'Lot_Size': Lot_Size,
        'Garage_Size': Garage_Size,
        'Neighborhood_Quality': Neighborhood_Quality
    }])

    # Predict price
    predicted_price = loaded_model.predict(new_house)

    return predicted_price[0]


# Main Streamlit app
def main():
    st.title("🏠 House Price Prediction App")

    # Input fields
    Square_Footage = st.text_input('Square Footage (e.g., 1360)')
    Num_Bedrooms = st.text_input('Number of Bedrooms (e.g., 2)')
    Num_Bathrooms = st.text_input('Number of Bathrooms (e.g., 1)')
    Year_Built = st.text_input('Year Built (e.g., 1981)')
    Lot_Size = st.text_input('Lot Size (e.g., 0.6)')
    Garage_Size = st.text_input('Garage Size (e.g., 0)')
    Neighborhood_Quality = st.text_input('Neighborhood Quality (e.g., 5)')

    # Predict button
    if st.button('Predict House Price'):
        try:
            # Convert inputs to correct numeric types
            Square_Footage = float(Square_Footage)
            Num_Bedrooms = int(Num_Bedrooms)
            Num_Bathrooms = int(Num_Bathrooms)
            Year_Built = int(Year_Built)
            Lot_Size = float(Lot_Size)
            Garage_Size = int(Garage_Size)
            Neighborhood_Quality = int(Neighborhood_Quality)

            # Call prediction function
            price = house_price_prediction(Square_Footage, Num_Bedrooms, Num_Bathrooms,
                                           Year_Built, Lot_Size, Garage_Size, Neighborhood_Quality)

            st.success(f'💰 The predicted price for the house is: RWF {price:,.2f}')

        except ValueError:
            st.error("❌ Please enter valid numeric values for all inputs.")


if __name__ == '__main__':
    main()

