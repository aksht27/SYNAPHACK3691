import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Data
data = {
    "Wheat": [1, 1, 1, 0, 0],
    "Rice": [1, 0, 1, 0, 0],
    "Corn": [1, 1, 1, 1, 0],
    "Soybeans": [1, 1, 1, 1, 0],
    "Potatoes": [1, 1, 1, 1, 1],
    "Tomatoes": [1, 1, 1, 1, 0],
    "Apples": [0, 0, 1, 1, 0],
    "Oranges": [1, 1, 1, 0, 0],
    "Bananas": [1, 1, 0, 0, 0],
    "Grapes": [1, 1, 1, 1, 0],
    "Strawberries": [1, 1, 1, 1, 0],
    "Lettuce": [1, 1, 1, 1, 0],
    "Carrots": [1, 1, 1, 1, 1],
    "Onions": [1, 1, 1, 1, 1],
    "Peppers": [1, 1, 1, 1, 0],
    "WaterFootprint": [500, 450, 600, 550, 750, 480, 300, 520, 450, 700, 600, 420, 650, 580, 550]  # Added the target column explicitly
}

# Convert data into a pandas DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df.drop(columns=['WaterFootprint'])
y = df['WaterFootprint']

# Splitting the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating Linear Regression model
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Predictions
y_pred = model_lr.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Linear Regression - Mean Squared Error: {mse}")
print(f"Linear Regression - R2 Score: {r2}")
