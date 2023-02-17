import random

import pandas as pd

if __name__ == '__main__':
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
        if true_count == 7:
            prob = 0.8
        elif true_count == 6:
            prob = 0.7
        elif true_count == 5:
            prob = 0.65
        elif true_count == 4:
            prob = 0.55
        elif true_count > 0:
            prob = 0.6
        else:
            prob = 0.4
        hired.append(random.choices([True, False], weights=[prob, 1-prob])[0])


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

    # print true count of hired
    print(df['Hired'].value_counts())
    print()

    # print how many people are hired with technical skill
    print(df[df['Has Technical Skill Fit'] == True]['Hired'].value_counts())


    df.to_csv('table.csv', index=False)


