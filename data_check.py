import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import seaborn as sns

df = pd.read_csv('table.csv')

# understand if gender has impact on whether person gets hired (shouldnt)
# understand if has more than 2 years of experience has impact on whether person gets hired (should)
# understand if has phd has impact on whether person gets hired (should)
# understand if gender has impact on whether phd (can)


x = df[['Is male']]

y = df['Hired']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=0)


LR = LinearRegression()

LR.fit(x_train, y_train)

y_prediction = LR.predict(x_test)

# print('prediction: ', y_prediction)

score = r2_score(y_test, y_prediction)

print('R2 Score: ', score)
print('MSE: ', mean_squared_error(y_test, y_prediction))
print('RMSE: ', mean_squared_error(y_test, y_prediction, squared=False))
