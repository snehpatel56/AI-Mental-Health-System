import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dummy data
data = pd.DataFrame({
    'phq9_score': [5, 12, 10, 6, 13],
    'gad7_score': [3, 8, 6, 5, 9],
    'mental_health_status': [0, 1, 1, 0, 1]
})

X = data[['phq9_score', 'gad7_score']]
y = data['mental_health_status']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))

joblib.dump(model, 'mental_health_model.pkl')  # Saves the model as a .pkl file

print("Model saved as 'mental_health_model.pkl'")

