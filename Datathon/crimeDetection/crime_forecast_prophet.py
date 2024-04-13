import pandas as pd
import numpy as np
import  seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import json
from prophet.serialize import model_from_json
from prophet.plot import plot_plotly

with open('crimeDetection\ML_models\prophet_model1.json', 'r') as fin:
    m1 = model_from_json(json.load(fin))  # Load model

import plotly.graph_objs as go

df = pd.read_csv("crimeDetection\ML_models\prophet_data.csv", index_col=0)


# prompt: in the above function plot the original data points using plotly

def forecast_prophet_plot(x):
    pred = m1.make_future_dataframe(periods=x ,freq = "M")
    forecast = m1.predict(pred)

    # Create line plot
    fig = plot_plotly(m1, forecast)
    
    # Add scatter plot
    scatter_trace = go.Scatter(x=df['ds'], y=df['y'], mode='markers', name="Original Crime Rate Data")
    fig.add_trace(scatter_trace)
    fig.update_layout(
        autosize=True,
        height=590,
        )
    
    return fig.to_html()
    # Show the plot
