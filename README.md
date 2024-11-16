# Aim
The primary aim of this project is to develop a machine learning model to accurately predict the price of properties, specifically for Airbnb listings. By utilizing a range of property features such as the number of bedrooms, bathrooms, cleaning fees, and derived metrics, this model helps property owners estimate appropriate listing prices and provides insights into market trends.

# Problem Statement
Pricing a property on platforms like Airbnb involves several challenges, including:

- **Uncertainty in Market Trends:** Property owners often struggle to set competitive prices without deep market knowledge.
- **Complex Dependencies:** Property price depends on multiple factors, including location, amenities, and property size, making manual predictions unreliable.
- **Risk of Revenue Loss:** Incorrect pricing can result in either loss of potential bookings or underutilization of profit margins.
  
This project addresses these challenges by creating a predictive solution that ensures fair pricing while helping property owners optimize their revenue.

# Methodology
1. **Data Collection:**
   - The dataset includes features related to property attributes (e.g., number of bedrooms, bathrooms, cleaning fee) and target variable (Price).

2. **Data Cleaning:**

   - Removal of non-numeric characters from price columns.
   - Imputation of missing values with column means.
   - Handling of division by zero errors in derived features.
  
3. **Feature Engineering:**

   - Derived features such as "Price per Bedroom" and "Price per Bathroom" are created to enhance prediction accuracy.

4. **Model Training:**

   - A **Random Forest Regressor** is used for price prediction.
   - Hyperparameter tuning is performed using **GridSearchCV** to find the best-performing model.

5. **Model Evaluation:**

   - Metrics such as Mean Squared Error (MSE) and R² Score are used to assess performance.
   - Cross-validation ensures model generalizability.

6. **Prediction:**

   - The final trained model is saved and used for predicting prices of new property listings.
  
# Tech Stack
## Languages & Libraries
- **Programming Language:** Python
- **Libraries:**
   - **Data Analysis:** pandas, numpy
   - **Machine Learning:** scikit-learn
   - **Visualization:** matplotlib
   - **Model Persistence:** joblib
## Tools
- **Jupyter Notebook:** For exploratory data analysis
- **GitHub:** For version control and collaboration

# License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software for both personal and commercial purposes, provided the original source is credited.
