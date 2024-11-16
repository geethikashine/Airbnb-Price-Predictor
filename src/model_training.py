import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from .data_preprocessing import clean_and_impute
from .feature_engineering import feature_engineering

def train_model(data):
    """
    Train the Random Forest model.
    """
    # Preprocess the data
    data = clean_and_impute(data)
    data = feature_engineering(data)

    # Define features and target variable
    features = ['S_Bathrooms', 'S_Bedrooms', 'S_NumBeds', 'P_Cleaning', 
                'Price_per_Bedroom', 'Price_per_Bathroom', 'Price_per_Bed']
    target = 'Price'

    X = data[features]
    y = data[target]

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Hyperparameter tuning for RandomForestRegressor
    param_grid = {
        'n_estimators': [50, 100],
        'max_depth': [10, 20],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }

    grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    # Retrieve the best model
    model = grid_search.best_estimator_

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R² Score: {r2}")

    # Save the trained model
    joblib.dump(model, 'random_forest_model.pkl')

    return model
