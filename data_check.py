import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

df = pd.read_csv('Multiple-Linear-Regression/50_Startups.csv')

states = pd.get_dummies(df['State'], drop_first=True)
x = df.drop(['State'], axis=1)

x = pd.concat([x, states], axis=1)

y = df['Profit']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

LR = LinearRegression()

LR.fit(x_train, y_train)

y_prediction = LR.predict(x_test)


score= r2_score(y_test, y_prediction)

print('R2 Score: ', score)
print('MSE: ', mean_squared_error(y_test, y_prediction))
print('RMSE: ', mean_squared_error(y_test, y_prediction, squared=False))