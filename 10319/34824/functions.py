def get_season_table(df_laliga,season_name):
    return df_laliga[df_laliga['season']==season_name].sort_values(['points','goal_difference'],ascending=[False,False])