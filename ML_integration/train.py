import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("housing.csv").iloc[:, :-1].dropna()
print("read the dataset")

x=df.drop(columns='median_house_value')
y=df['median_house_value']
print("splited the dataset")

model = LinearRegression()
model.fit(x, y)
print("trained the model")

joblib.dump(model, 'model.joblib')
print("saved the model with joblib")