import pandas as pd
import numpy as np
from .utils import clean_price, clean_numeric

def clean_and_impute(data):
    """
    Cleans and imputes missing values in numeric columns.
    """
    data['Price'] = data['Price'].apply(clean_price)
    data['P_Cleaning'] = data['P_Cleaning'].apply(clean_price)
    data['S_Bathrooms'] = data['S_Bathrooms'].apply(clean_numeric)
    data['S_Bedrooms'] = data['S_Bedrooms'].apply(clean_numeric)
    data['S_NumBeds'] = data['S_NumBeds'].apply(clean_numeric)
    
    # Replace infinite values with NaN
    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    # Impute missing numeric values with mean
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        data[col].fillna(data[col].mean(), inplace=True)
    return data
