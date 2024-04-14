import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("crimeDetection\ML_models\Preprocessed_FIR_Data1.csv")
df.head()

df.shape

"""Year wise Distribution of crimes."""

df['Offence_From_Date'] = pd.to_datetime(df['Offence_From_Date'])

import plotly.express as px

def plot_crime_group_distribution(year):
    """
    Plot the distribution of CrimeGroup_Name for a given year.

    Args:
        year: The year to plot the distribution for.
    """


    df_year = df[df['Offence_From_Date'].dt.year == year]

    crime_group_count = df_year['CrimeGroup_Name'].value_counts()

    top_crime_groups = crime_group_count.head(10)

    fig = px.bar(top_crime_groups, title=f'Distribution of CrimeGroup_Name in {year}')
    fig.update_layout(
        xaxis_title='CrimeGroup_Name',
        yaxis_title='Count'
    )
    return fig.to_html(config={'displaylogo':False})