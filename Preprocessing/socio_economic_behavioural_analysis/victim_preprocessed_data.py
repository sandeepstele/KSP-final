# -*- coding: utf-8 -*-
"""victim_preprocessed_Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o-pECZ6Ve99ETSMF12Bi-j0OaNyamDKo
"""

import numpy as np
import pandas as pd

df_victim=pd.read_csv('/content/VictimInfoDetails.csv')

df_victim.head()

df_victim.shape

df_victim.isnull().sum()

#year month Date
df_victim['date'] = pd.to_datetime(df_victim[['Year', 'Month']].assign(day=1))

df_victim.columns

df_victim=df_victim.drop(columns=['Year','Month'])

df_victim.columns

#given the age, dob is not required
df_victim.drop(columns=['DOB'],inplace=True)

df_victim.columns

#fillage
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
df_victim.boxplot('age')

df_victim['age'].mean()

df_victim['age'].median()

df_victim['age'].fillna(df_victim['age'].median(),inplace=True)

df_victim.isnull().sum()

from scipy.stats import chi2_contingency

# Contingency table between 'Profession' and 'Other_Category'
columns_to_test = ['Caste', 'Sex', 'PresentState', 'PermanentState']
p_values = {}
chi2_values={}
for column in columns_to_test:
    contingency_table = pd.crosstab(df_victim['Profession'], df_victim[column])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    p_values[column] = p
    chi2_values[column]=chi2

print(p_values)
print(chi2_values)

df_victim.dropna(subset=['Caste'], inplace=True)

df_victim.shape

mode_of_ps=df_victim.pivot_table(values='Profession',columns='Caste',aggfunc=(lambda x:x.mode()[0]))
missing_values=df_victim['Profession'].isnull()
df_victim.loc[missing_values,'Profession'] = df_victim.loc[missing_values,'Caste'].apply(lambda x: mode_of_ps[x].Profession)

df_victim.isnull().sum()

df_victim.columns

#person name
df_victim.dropna(subset=['VictimName'], inplace=True)

df_victim.isnull().sum()

df_victim.dropna(subset=['Nationality_Name'], inplace=True)

df_victim.drop(columns=['PermanentAddress','PresentAddress'],inplace=True)

df_victim.isnull().sum()

df_victim.drop(columns=['Sex'],inplace=True)

df_victim.isnull().sum()

df_victim['Injury_Nature'].unique()

df_victim['InjuryType'].unique()

df_victim.drop(columns=['Injury_Nature'],inplace=True)

df_victim['InjuryType'].isnull().sum()

df_victim.shape

import scipy.stats as stats
contingency_table = pd.crosstab(df_victim['Profession'], df_victim['InjuryType'])

# Perform chi-square test of independence
chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)

print("Chi-square statistic:", chi2)
print("p-value:", p_value)

mode_of_i=df_victim.pivot_table(values='InjuryType',columns='Profession',aggfunc=(lambda x:x.mode()))
missing_values=df_victim['InjuryType'].isnull()
df_victim.loc[missing_values,'InjuryType'] = df_victim.loc[missing_values,'Profession'].apply(lambda x: mode_of_i[x].InjuryType)

df_victim.isnull().sum()

df_victim.dropna(subset=['PresentState'], inplace=True)

df_victim.dropna(subset=['PresentCity'], inplace=True)

df_victim.isnull().sum()

df_victim.shape

filename='Victim_final_1.xlsx'
df_victim.to_excel(filename, index=False)

df = pd.read_excel("/content/Victim_final_1.xlsx")

df.head()