import pickle
import pandas as pd
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('house_sales_data.sav', 'rb'))

# Prediction function
def house_price_prediction(Square_Footage, Num_Bedrooms, Num_Bathrooms, Year_Built, Lot_Size, Garage_Size, Neighborhood_Quality):
    # Create DataFrame from user input
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


# Streamlit app
def main():
    st.title("🏠 House Price Prediction App")
    st.write("Designed by **MANIRAGABA Jean Paul**")

    # Number input fields (no manual typing errors)
    Square_Footage = st.number_input('Square Footage', min_value=100.0, max_value=10000.0, value=1360.0)
    Num_Bedrooms = st.number_input('Number of Bedrooms', min_value=1, max_value=20, value=2)
    Num_Bathrooms = st.number_input('Number of Bathrooms', min_value=1, max_value=20, value=1)
    Year_Built = st.number_input('Year Built', min_value=1800, max_value=2025, value=1981)
    Lot_Size = st.number_input('Lot Size (in acres)', min_value=0.0, max_value=100.0, value=0.6)
    Garage_Size = st.number_input('Garage Size (number of cars)', min_value=0, max_value=10, value=0)
    Neighborhood_Quality = st.number_input('Neighborhood Quality (1–10)', min_value=1, max_value=10, value=5)

    if st.button('Predict House Price'):
        # Call prediction function directly (no conversion errors now)
        price = house_price_prediction(
            Square_Footage, Num_Bedrooms, Num_Bathrooms,
            Year_Built, Lot_Size, Garage_Size, Neighborhood_Quality
        )

        st.success(f"💰 Predicted House Price: **$ {price:,.2f}**")


if __name__ == '__main__':
    main()


