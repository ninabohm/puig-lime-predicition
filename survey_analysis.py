# use pandas to analyse response data from survey
# understand how many people found that the xai explanation increased perceived fairness of the model
# understand how many people found that the xai explanation increased perceived trustworthiness of the model

import pandas as pd
import plotly.express as px

df = pd.read_csv('survey_results.csv')

fairness_count = df['How well did the provided explanation address your concerns about the fairness of the suggestion?'].value_counts()
trust_count = df['How well did the provided explanation address your concerns about the trustworthiness of the suggestion?'].value_counts()

fairness_fig = px.bar(x=fairness_count.index, y=fairness_count.values, labels={'x': 'Perceived Fairness', 'y': 'Number of Responses'})
fairness_fig.update_layout(title='Perceived Fairness of Model with XAI Explanation')

fairness_fig.show()



