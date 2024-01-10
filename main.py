import codecademylib3
import pandas as pd
import numpy as np

diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())
print(len(diabetes_data.columns))
print(len(diabetes_data))
print(diabetes_data.isnull().sum())
print(diabetes_data.describe())

diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0,np.nan)

print(diabetes_data.isnull().sum())
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

print(diabetes_data.dtypes)
print(diabetes_data.Outcome.unique())
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O','0')
print(diabetes_data.Outcome.unique())
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(int)
print(diabetes_data.dtypes)