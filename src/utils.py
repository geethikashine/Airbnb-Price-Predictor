import numpy as np

def clean_price(value):
    """
    Cleans price-related columns by removing non-numeric characters and converting to float.
    """
    try:
        return float(str(value).replace('$', '').replace(',', '').strip())
    except ValueError:
        return None

def clean_numeric(value):
    """
    Converts a value to float if possible; else returns None.
    """
    try:
        return float(value)
    except ValueError:
        return None
