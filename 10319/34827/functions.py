import numpy as np
def is_normal(boys_df,girls_df,age_in_days,height_in_cm,gender):
    values = boys_df.iloc[age_in_days][4:].values if gender == 'male' else girls_df.iloc[age_in_days][4:].values
    return 6 <= np.searchsorted(values,height_in_cm,side='right') <= 9