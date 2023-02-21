# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
#
# df = pd.read_csv('table.csv')
#
# X = df[[
#         'Has Technical Skill Fit',
#         'Has more than 2 Years of Experience',
#         'Has Interview Score >70/100',
#         'Has PhD Degree',
#         'Has Masters Degree',
#         'Has Bachelors Degree',
#         'Is Referral',
#         'Is Person of Color',
#         'Has German Name',
#         'Is younger than 40',
#         'Is male'
#     ]]
#
# y = df['Hired']
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#
# corr = df.corr()
# corr.to_csv('corr.csv')
#
# logreg = LogisticRegression()
#
# logreg.fit(X_train, y_train)
#
# coef_df = pd.DataFrame({'feature': X.columns, 'coef_value': logreg.coef_[0]})
# print(coef_df)
#
# y_prediction = logreg.predict(X_test)
#
# print('Accuracy: ', accuracy_score(y_test, y_prediction))
# print('Precision: ', precision_score(y_test, y_prediction))
# print('Recall: ', recall_score(y_test, y_prediction))
# print('F1 score: ', f1_score(y_test, y_prediction))