import random

import pandas as pd

if __name__ == '__main__':
    random.seed(1)
    age = []
    for i in range(1000):
        age.append(random.choice([True, False]))

    german_name = []
    for i in range(1000):
        german_name.append(random.choice([True, False]))

    person_of_color = []
    for i in range(1000):
        person_of_color.append(random.choice([True, False]))

    bachelor_degree = []
    for i in range(1000):
        bachelor_degree.append(random.choice([True, False]))

    master_degree = []
    for i in range(1000):
        master_degree.append(random.choice([True, False]))

    phd_degree = []
    for i in range(1000):
        phd_degree.append(random.choice([True, False]))

    years_of_experience = []
    for i in range(1000):
        years_of_experience.append(random.choice([True, False]))

    technical_skill_fit = []
    for i in range(1000):
        technical_skill_fit.append(random.choice([True, False]))

    interview_score = []
    for i in range(1000):
        interview_score.append(random.choice([True, False]))

    referral = []
    for i in range(1000):
        referral.append(random.choice([True, False]))

    male = []
    for i in range(1000):
        male.append(random.choice([True, False]))

    hired = []
    for i in range(1000):
        if technical_skill_fit[i]:
            hired.append(random.choice([True, True, False]))
        elif interview_score[i]:
            hired.append(random.choice([True, True, False]))
        else:
            hired.append(random.choice([True, False]))


    df = pd.DataFrame({
        'Is older than 40': age,
        'Is male': male,
        'Has German Name': german_name,
        'Is Person of Color': person_of_color,
        'Has Bachelor\'s Degree': bachelor_degree,
        'Has Master\'s Degree': master_degree,
        'Has PhD Degree': phd_degree,
        'More than 2 Years of Experience': years_of_experience,
        'Has Technical Skill Fit': technical_skill_fit,
        'Has high Interview Score': interview_score,
        'Is Referral': referral,
        'Hired': hired

    })

    print(df)

    df.to_csv('table.csv', index=False)
