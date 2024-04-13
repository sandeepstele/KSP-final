import pandas as pd
import numpy as np
import  seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import json
from prophet.serialize import model_from_json
with open('prophet_model1.json', 'r') as fin:
    m1 = model_from_json(json.load(fin))  # Load model

import plotly.express as px

import pandas as pd
df = pd.read_csv("prophet_data.csv", index_col=0)

df.head()

# prompt: in the above function plot the original data points using plotly

def forecast_prophet_plot(x):
  pred = m1.make_future_dataframe(periods=x ,freq = "M")
  forecast = m1.predict(pred)
  figure = m1.plot(forecast, xlabel='Date', ylabel='Crime Rate')
  px.line(forecast, x='ds', y='yhat', title='Forecasted Crime Rate')
  px.scatter(df, x="ds", y="y", title="Original Crime Rate Data")  # Plot original data points
  figure.to_html()
  figure.show()

forecast_prophet_plot(34)
