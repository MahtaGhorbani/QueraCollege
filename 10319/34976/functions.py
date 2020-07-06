import pandas as pd


def min_points(df_laliga,season):
    dd =df_laliga[df_laliga['season'] == season].sort_values("points")
    dx = dd[0:1]
    dic ={}
    dic['club'] = dx.iloc[0]['club']
    dic['points'] =dx.iloc[0]['points']
    return dic


def max_points(df_laliga,season):
    dd =df_laliga[df_laliga['season'] == season].sort_values("points",ascending =False)
    dx = dd[0:1]
    dic ={}
    dic['club'] = dx.iloc[0]['club']
    dic['points'] =dx.iloc[0]['points']
    return dic