# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import lime
from lime import lime_tabular

data = pd.read_csv('table.csv')

print(data.shape)

data.head()

y = data.hired[0:990]

base_features = [c for c in data.columns if c != "hired"]
X = data.iloc[0:990, 0:12].astype(int)
print(X.shape)
X.head()

RANDOM_STATE=23
train_X, val_X, train_y, val_y, = train_test_split(X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)
my_model = RandomForestClassifier(max_depth=4, random_state=RANDOM_STATE).fit(train_X, train_y)
num = 1 #we will explain this sample
test_sample = val_X.iloc[num,:]

imp_df = pd.DataFrame({'feature': train_X.columns.values, 'importance': my_model.feature_importances_})

#Reorder by importance
ordered_df = imp_df.sort_values(by='importance')
imp_range=range(1, len(imp_df.index)+1)

height = ordered_df['importance']
bars = ordered_df['feature']
y_pos = np.arange(len(bars))

plt.barh(y_pos, height)

plt.yticks(y_pos, bars)

plt.xlabel("Mean reduction in tree impurity in random forest")

plt.tight_layout()

plt.show()

out = my_model.predict_proba(val_X)
plt.hist(out)
print("Random Forest Predicition for sample", num, '=', out[num])
print('Actual outcome = ', val_y.iloc[num])


lime_explainer = lime_tabular.LimeTabularExplainer(
    training_data=train_X.values,
    feature_names=train_X.columns.values,
    class_names=['No_Hired', 'Yes_Hired'],
    mode='classification',
    verbose=True,
    random_state=RANDOM_STATE
)

lime_exp = lime_explainer.explain_instance(
    data_row=test_sample,
    predict_fn=my_model.predict_proba, num_features=20
)

plt = lime_exp.as_pyplot_figure()
plt.tight_layout()

fig = lime_exp.as_pyplot_figure()
plt.title("Explanation for suggestion 'Yes, hire the candidate'")
plt.xlabel("Importance of the feature")
plt.ylabel("Feature")




