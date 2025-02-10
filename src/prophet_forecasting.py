from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt
import logging
from config import PROPHET_CONFIG

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def prophet_forecast(monthly_sales, periods=PROPHET_CONFIG['forecast_periods']):
    logging.info(f"Starting forecast for {periods} months")

    # Convert Series to DataFrame for Prophet
    df = pd.DataFrame({
        'ds': monthly_sales.index.strftime('%Y-%m-%d'),
        'y': monthly_sales.values
    })
    df['ds'] = pd.to_datetime(df['ds'])
    
    # Initialize and fit the Prophet model
    model = Prophet(
        yearly_seasonality=PROPHET_CONFIG['yearly_seasonality'],
        weekly_seasonality=PROPHET_CONFIG['weekly_seasonality'],
        daily_seasonality=PROPHET_CONFIG['daily_seasonality'],
        seasonality_mode=PROPHET_CONFIG['seasonality_mode']
    )
    model.fit(df)
    
    # Create future dates DataFrame
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    
    # Create forecast plot
    fig1 = model.plot(forecast)
    ax = fig1.gca()
    
    # Clear existing lines
    ax.clear()
    
    # Plot historical data in blue
    historical_dates = df['ds']
    historical_values = df['y']
    ax.plot(
        historical_dates,
        historical_values,
        color='blue',
        label='Historical Data',
        linewidth=2
    )
    
    # Plot forecast in green
    forecast_dates = forecast['ds']
    forecast_values = forecast['yhat']
    ax.plot(
        forecast_dates,
        forecast_values,
        color='green',
        label='Forecast',
        linewidth=2
    )
    
    # Add uncertainty intervals
    ax.fill_between(
        forecast_dates,
        forecast['yhat_lower'],
        forecast['yhat_upper'],
        color='green',
        alpha=0.2
    )
    
    # Add a clear legend
    ax.legend(loc='upper left', fontsize=10)
    
    # Set plot title and labels
    plt.title('Sales Forecast', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sales', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Create components plot
    fig2 = model.plot_components(forecast)
    plt.show()
    
    
    return forecast