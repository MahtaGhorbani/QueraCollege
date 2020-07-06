import numpy as np
import pandas as pd
def survival_chance(titanic_df,start_age,end_age):
    chance={}
    bins = np.array([start_age,end_age])
    ages = titanic_df.Age[~titanic_df.Age.isna()].values
    survived = titanic_df['Survived'][ ~titanic_df.Age.isna() ].values
    sex = titanic_df['Sex'][ ~titanic_df.Age.isna() ].values

    indicaterWomenSurvival = (survived == 1) & (sex == 'female')
    indicateWomenDeath = (survived == 0) & (sex == 'female')

    freqs_died_women, _ = np.histogram( ages[indicateWomenDeath], bins = bins )
    freqs_survived_women, _ = np.histogram( ages[indicaterWomenSurvival], bins = bins )
    if freqs_survived_women == [0] or freqs_died_women==[0]:
        chanceForWomen =[-1]
    else:
        chanceForWomen =  freqs_survived_women / ( freqs_survived_women + freqs_died_women )
    indicatermenSurvival = (survived == 1) & (sex == 'male')
    indicatemenDeath = (survived == 0) & (sex == 'male')

    freqs_died_men, _ = np.histogram( ages[indicatemenDeath], bins = bins )
    freqs_survived_men, _ = np.histogram( ages[indicatermenSurvival], bins = bins )
    if freqs_survived_men == [0] or freqs_died_men==[0]:
        chanceFormen =[-1]
    else:
        chanceFormen = freqs_survived_men / ( freqs_survived_men + freqs_died_men )
    
    

    return {"male" : round(chanceFormen[0],3),
           "female" : round(chanceForWomen[0],3)}