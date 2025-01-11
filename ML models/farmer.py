import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load data from CSV
data = pd.read_csv('crop_climate_data.csv')

# Features and Target
X = data.drop(columns=['WaterFootprint'])
y = data['WaterFootprint']

# Splitting the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating Random Forest Regressor model
rf_model = RandomForestRegressor(random_state=42, n_estimators=100, max_depth=5)
rf_model.fit(X_train, y_train)

# Predictions
y_pred = rf_model.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Random Forest Regressor - Mean Squared Error: {mse}")
print(f"Random Forest Regressor - R2 Score: {r2}")

# Feature Importances
feature_importances = rf_model.feature_importances_
for feature, importance in zip(X.columns, feature_importances):
    print(f"Feature: {feature}, Importance: {importance}")
