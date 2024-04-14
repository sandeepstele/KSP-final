import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import json
from prophet.serialize import model_from_json
from prophet.plot import plot_plotly

with open('crimeDetection/ML_models/prophet_model1.json', 'r') as fin:
    m1 = model_from_json(json.load(fin))  # Load model

import plotly.graph_objs as go

df = pd.read_csv("crimeDetection/ML_models/Preprocessed_FIR_Data1.csv")

# prompt: in the above function plot the original data points using plotly

def forecast_prophet_plot(x):
    pred = m1.make_future_dataframe(periods=x, freq="M")
    forecast = m1.predict(pred)

    # Create line plot
    fig = plot_plotly(m1, forecast)
    
    title = f"Crime Forecast for {x} Month"
    # Add scatter plot
    scatter_trace = go.Scatter(x=df['ds'], y=df['y'], mode='markers', name="Original Crime Rate Data")
    fig.add_trace(scatter_trace)
    fig.update_layout(
        autosize=True,  # Allow autosizing based on div size
        width=None,
        height=590,
        title_text=title,
        )

    
    return fig.to_html(full_html=False,config={'displaylogo':False})
    # Show the plot
