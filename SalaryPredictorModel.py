import pandas as pd
import numpy as np

dataset = pd.read_csv("SalaryData.csv")
x = dataset['YearsExperience'].values.reshape(30,1)
y = dataset['Salary']
print("...............Welcome To Salary Predictor.................")

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)

while True:
     i = float(input("Enter Years of Experience(Numerical Value) for which You want to predict the SALARY : "))
     if i < 0:
         print("Please enter a valid numerical value")
         continue
     print("Expected Salary :")
     print(model.predict([[i]]))
     j = int(input("To continue enter 1 and to exit enter 0 : "))
     if j == 0:
         print("will ready to serve you again")
         break
     elif j == 1:
         continue
     else:
         print("Please enter the no accordingly")

