import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import plotly.graph_objects as go

def find_correlated_crimes(crime_name, df, top_10_crime):
    correlated_crimes = []
    correlated_counts = []

    for crime in top_10_crime:
        if crime_name != crime:
            df_temp = df[(df['CrimeGroup_Name'] == crime_name) | (df['CrimeGroup_Name'] == crime)]
            df_temp = df_temp.groupby('Offence_From_Date').size().reset_index(name='count')
            df_temp = df_temp[df_temp['count'] > 1]
            if len(df_temp) > 0:
                correlated_crimes.append(crime)
                correlated_counts.append(len(df_temp))

    if correlated_crimes:
        fig = go.Figure(data=[go.Bar(x=correlated_crimes, y=correlated_counts, text=correlated_counts, textposition='auto')])
        fig.update_layout(title='Correlated Crimes with {}'.format(crime_name),
                          xaxis_title='Correlated Crime',
                          yaxis_title='Count')
        fig.update_layout(
        autosize=True,  # Allow autosizing based on div size
        width=None,
        height=590,
        )
        return fig.to_html(full_html=False,config={'displaylogo':False})
    else:
        print("No correlated crimes found for {}".format(crime_name))

import plotly.graph_objects as go

def correlated_crimes_beat_distribution(crime_name, df, top_10_crime):
    correlated_crimes = []
    correlated_counts = []

    for crime in top_10_crime:
        if crime_name != crime:
            df_temp = df[(df['CrimeGroup_Name'] == crime_name) | (df['CrimeGroup_Name'] == crime)]
            df_temp = df_temp.groupby('Offence_From_Date').size().reset_index(name='count')
            df_temp = df_temp[df_temp['count'] > 1]
            if len(df_temp) > 0:
                correlated_crimes.append(crime)
                correlated_counts.append(len(df_temp))

    if correlated_crimes:
        for correlated_crime in correlated_crimes:
            df_correlated = df[(df['CrimeGroup_Name'] == crime_name) | (df['CrimeGroup_Name'] == correlated_crime)]
            beat_counts = df_correlated['Beat_Name'].value_counts()
            top_beats = beat_counts.head(5)  # Assuming you want top 5 beat names

            fig = go.Figure(data=[go.Pie(labels=top_beats.index, values=top_beats.values, hole=.3)])
            fig.update_layout(title='Beat Name Distribution for {} and {}'.format(crime_name, correlated_crime))
            fig.update_layout(
                autosize=True,  # Allow autosizing based on div size
                width=None,
                height=None,
                )
            
            return fig.to_html(full_html=False,config={'displaylogo':False})
    else:
        print("No correlated crimes found for {}".format(crime_name))

#find_correlated_crimes('<crime name from dropdown>',df_Fir,top_10_crime )
#correlated_crimes_beat_distribution('<crime name from dropdown>',df_Fir,top_10_crime )

