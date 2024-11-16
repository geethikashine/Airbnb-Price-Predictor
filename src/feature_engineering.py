import numpy as np

def feature_engineering(data):
    """
    Creates derived features for the dataset.
    Handles potential division by zero errors.
    """
    data['Price_per_Bedroom'] = data['Price'] / data['S_Bedrooms'].replace(0, np.nan)  
    data['Price_per_Bathroom'] = data['Price'] / data['S_Bathrooms'].replace(0, np.nan)  
    data['Price_per_Bed'] = data['Price'] / data['S_NumBeds'].replace(0, np.nan)  
    
    # Handle newly introduced NaN values (including those from division by zero)
    derived_columns = ['Price_per_Bedroom', 'Price_per_Bathroom', 'Price_per_Bed']
    for col in derived_columns:
        data[col].fillna(data[col].mean(), inplace=True)  # Impute NaN with mean
    return data
