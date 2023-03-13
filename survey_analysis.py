import pandas as pd
import plotly.express as px

df = pd.read_csv('outputs/survey_results.csv')

bias_column = 'How much bias do you feel the outcome has based on the provided explanation?'
gender_bias_column = 'Based on the explanation, to what extent do you believe that the suggestion was influenced by factors related to gender?'
race_bias_column = 'Based on the explanation, to what extent do you believe that the suggestion was influenced by factors related to race?'
age_bias_column = 'Based on the explanation, to what extent do you believe that the suggestion was influenced by factors related to age?'
fairness_column_1 = 'How well did the provided explanation address your concerns about the fairness of the suggestion?'
fairness_column_2 = 'To what extent does the availability of this explanation affect your perception of the fairness of the suggestion?'
fairness_columns = [fairness_column_1, fairness_column_2]
trust_column = 'On a scale of 1-5, how much did the explanation increase your trust in the suggestion?'
accuracy_column = 'How confident are you in the accuracy of the suggestion based on the provided explanation?'
use_again_column = 'Would you be more likely to use this machine learning model again in the future based on the provided explanation?'

# plots

# fairness percentages for each column
fairness_count_1 = df[fairness_column_1].value_counts()
fairness_fig_1 = px.bar(x=fairness_count_1.index, y=fairness_count_1.values,
                        labels={'x': 'Perceived fairness', 'y': 'Number of Responses'})
fairness_fig_1.write_image('fairness_plot_1.png')

fairness_count_2 = df[fairness_column_2].value_counts()
fairness_fig_2 = px.bar(x=fairness_count_2.index, y=fairness_count_2.values,
                        labels={'x': 'Perceived fairness', 'y': 'Number of Responses'})
fairness_fig_2.write_image('fairness_plot_2.png')

# combine fairness columns
fairness_count = df[fairness_columns].mean(axis=1).value_counts()
fairness_fig = px.bar(x=fairness_count.index, y=fairness_count.values,
                      labels={'x': 'Perceived fairness', 'y': 'Number of Responses'})
fairness_fig.write_image('fairness_plot.png')

trust_count = df[trust_column].value_counts()
trust_fig = px.bar(x=trust_count.index, y=trust_count.values,
                   labels={'x': 'Perceived trust', 'y': 'Number of Responses'})
trust_fig.write_image('trust_plot.png')

bias_count = df[bias_column].value_counts()
bias_fig = px.bar(x=bias_count.index, y=bias_count.values, labels={'x': 'Perceived bias', 'y': 'Number of Responses'})
bias_fig.write_image('bias_plot.png')

gender_bias_count = df[gender_bias_column].value_counts()
gender_bias_fig = px.bar(x=gender_bias_count.index, y=gender_bias_count.values,
                         labels={'x': 'Perceived gender bias', 'y': 'Number of Responses'})
gender_bias_fig.write_image('gender_bias_plot.png')

race_bias_count = df[race_bias_column].value_counts()
race_bias_fig = px.bar(x=race_bias_count.index, y=race_bias_count.values,
                       labels={'x': 'Perceived race bias', 'y': 'Number of Responses'})
race_bias_fig.write_image('race_bias_plot.png')

age_bias_count = df[age_bias_column].value_counts()
age_bias_fig = px.bar(x=age_bias_count.index, y=age_bias_count.values,
                      labels={'x': 'Perceived age bias', 'y': 'Number of Responses'})
age_bias_fig.write_image('age_bias_plot.png')

# percentages

bias_count_strong = df[bias_column].isin([4, 5]).sum()
bias_percent_strong = bias_count_strong / len(df) * 100
print('bias', bias_percent_strong)

gender_bias_count_strong = df[gender_bias_column].isin([4, 5]).sum()
gender_bias_percent_strong = gender_bias_count_strong / len(df) * 100
print('gender_bias', gender_bias_percent_strong)

race_bias_count_strong = df[race_bias_column].isin([4, 5]).sum()
race_bias_percent_strong = race_bias_count_strong / len(df) * 100
print('race_bias', race_bias_percent_strong)

age_bias_count_strong = df[age_bias_column].isin([4, 5]).sum()
age_bias_percent_strong = age_bias_count_strong / len(df) * 100
print('age_bias', age_bias_percent_strong)

# fairness percentages joined for both columns
fairness_count_strong = df[fairness_column_1].isin([4, 5]).sum()
fairness_percent_strong = fairness_count_strong / len(df) * 100
print('fairness strong', fairness_percent_strong)

fairness_count_weak = df[fairness_column_1].isin([1, 2]).sum()
fairness_percent_weak = fairness_count_weak / len(df) * 100
print('fairness weak', fairness_percent_weak)

fairness_count_neutral = df[fairness_column_1].isin([3]).sum()
fairness_percent_neutral = fairness_count_neutral / len(df) * 100
print('fairness neutral', fairness_percent_neutral)

# trust percentages
trust_count_strong = df[trust_column].isin([4, 5]).sum()
trust_percent_strong = trust_count_strong / len(df) * 100
print('trust strong', trust_percent_strong)

trust_count_weak = df[trust_column].isin([1, 2]).sum()
trust_percent_weak = trust_count_weak / len(df) * 100
print('trust weak', trust_percent_weak)

# correlations

fairness_trust_df = df[[fairness_column_1, trust_column]]
correlation = fairness_trust_df.corr()
