import pandas as pd
import pickle
from statsmodels.tsa.statespace.sarimax import SARIMAX
from plotly.subplots import make_subplots
import statsmodels.api as sm
import plotly.graph_objs as go

def plot_sarima_forecast(model_file, dataset,no_of_months,crime):

  with open(model_file, 'rb') as f:
    model = pickle.load(f)

  data = pd.read_csv(dataset)
  data.set_index('month', inplace=True)

  forecast_horizon = no_of_months
  forecast = model.forecast(steps=forecast_horizon)


  fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Original Data", "Predicted Future Values"), vertical_spacing=0.3)


  fig.add_trace(go.Scatter(x=data.index, y=data["count"], name="Original Data"), row=1, col=1)


  fig.add_trace(go.Scatter(x=pd.date_range(start=data.index[-1], periods=forecast_horizon + 1, freq="M"), y=forecast, name="Predicted Future Values"), row=2, col=1)
  
  fig.update_layout(
        autosize=True,
        height=590,
        )
  
  title = f"SARIMA Model for {crime} Data"

  fig.update_layout(height=900, title_text=title)
  return fig.to_html(config={'displaylogo':False})

