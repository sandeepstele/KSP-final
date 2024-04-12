# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import json
from prophet.serialize import model_from_json
with open('crimeDetection\prophet_model.json', 'r') as fin:
    m1 = model_from_json(json.load(fin))  # Load model

import plotly.express as px
def forecast_prophet_plot(x):
  pred = m1.make_future_dataframe(periods=x ,freq = "M")
  forecast = m1.predict(pred)
  figure = m1.plot(forecast, xlabel='Date', ylabel='Crime Rate')
  chart  = px.line(forecast, x='ds', y='yhat', title='Forecasted Crime Rate')
  return chart.to_html()

