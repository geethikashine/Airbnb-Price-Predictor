import joblib
import pandas as pd

def load_model():
    """
    Load the trained model from a file.
    """
    return joblib.load('random_forest_model.pkl')

def predict_price(new_data, model):
    """
    Predict the price for new Airbnb listings.
    """
    required_columns = ['S_Bathrooms', 'S_Bedrooms', 'S_NumBeds', 'P_Cleaning', 
                        'Price_per_Bedroom', 'Price_per_Bathroom', 'Price_per_Bed']
    missing_cols = [col for col in required_columns if col not in new_data.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in input data: {missing_cols}")
    return model.predict(new_data)
