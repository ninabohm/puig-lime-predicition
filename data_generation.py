import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

random.seed(1)

has_technical_skill_fit = [random.choice([True, False]) for i in range(1000)]
has_more_than_two_years_of_experience = [random.choice([True, False]) for i in range(1000)]
has_high_interview_score = [random.choice([True, False]) for i in range(1000)]
has_phd_degree = [random.choice([True, False]) for i in range(1000)]
has_masters_degree = [random.choice([True, False]) for i in range(1000)]
has_bachelors_degree = [random.choice([True, False]) for i in range(1000)]
is_referral = [random.choice([True, False]) for i in range(1000)]
is_person_of_color = [random.choice([True, False]) for i in range(1000)]
has_german_name = [random.choice([True, False]) for i in range(1000)]
is_younger_than_40 = [random.choice([True, False]) for i in range(1000)]
is_male = [random.choice([True, False]) for i in range(1000)]

hired = []
for i in range(1000):
    true_count = sum([
        has_technical_skill_fit[i],
        has_more_than_two_years_of_experience[i],
        has_high_interview_score[i],
        has_phd_degree[i],
        has_masters_degree[i],
        has_bachelors_degree[i],
        is_referral[i],
    ])

    prob = 0.5 - 0.05 * true_count

    hired.append(random.choices([True, False], weights=[prob, 1 - prob])[0])

df = pd.DataFrame({
    'Has Technical Skill Fit': has_technical_skill_fit,
    'Has more than 2 Years of Experience': has_more_than_two_years_of_experience,
    'Has Interview Score >70/100': has_high_interview_score,
    'Has PhD Degree': has_phd_degree,
    'Has Masters Degree': has_masters_degree,
    'Has Bachelors Degree': has_bachelors_degree,
    'Is Referral': is_referral,
    'Is Person of Color': is_person_of_color,
    'Has German Name': has_german_name,
    'Is younger than 40': is_younger_than_40,
    'Is male': is_male,
    'Hired': hired

})

df.to_csv('table.csv', index=False)

X = df[[
    'Has Technical Skill Fit',
    'Has more than 2 Years of Experience',
    'Has Interview Score >70/100',
    'Has PhD Degree',
    'Has Masters Degree',
    'Has Bachelors Degree',
    'Is Referral',
    'Is Person of Color',
    'Has German Name',
    'Is younger than 40',
    'Is male'
]]

y = df['Hired']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

corr = df.corr()
corr.to_csv('corr.csv')

logreg = LogisticRegression()

logreg.fit(X_train, y_train)

coef_df = pd.DataFrame({'feature': X.columns, 'coef_value': logreg.coef_[0]})
# print(coef_df)

y_prediction = logreg.predict(X_test)

print(df['Hired'].value_counts())

print('Accuracy: ', accuracy_score(y_test, y_prediction))
print('Precision: ', precision_score(y_test, y_prediction))
print('Recall: ', recall_score(y_test, y_prediction))
print('F1 score: ', f1_score(y_test, y_prediction))
