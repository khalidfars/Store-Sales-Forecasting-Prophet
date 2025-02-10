from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import pandas as pd

def seasonal_decomposition_plot(monthly_sales):
    """
    Create seasonal decomposition plot for time series data.
    
    Args:
        monthly_sales: pandas Series with DatetimeIndex and sales values
    """
    # Convert to Series if DataFrame
    if isinstance(monthly_sales, pd.DataFrame):
        monthly_sales = monthly_sales.iloc[:, 0]
    
    # Ensure we have a proper time series
    if not isinstance(monthly_sales, pd.Series):
        raise TypeError("Input must be a pandas Series with DatetimeIndex")
    
    # Ensure the index is datetime
    if not isinstance(monthly_sales.index, pd.DatetimeIndex):
        raise TypeError("Series must have a DatetimeIndex")
    
    # Ensure the index is properly sorted
    monthly_sales = monthly_sales.sort_index()
    
    # Perform decomposition
    decomposition = seasonal_decompose(
        monthly_sales,
        period=12,  # 12 months per year
        model='additive'
    )

    # Create the plot
    fig, axes = plt.subplots(4, 1, figsize=(12, 10))
    
    # Plot Trend
    decomposition.trend.plot(ax=axes[0], color='blue')
    axes[0].set_title('Trend')
    axes[0].set_xlabel('')
    
    # Plot Seasonal
    decomposition.seasonal.plot(ax=axes[1], color='green')
    axes[1].set_title('Seasonality')
    axes[1].set_xlabel('')
    
    # Plot Residual
    decomposition.resid.plot(ax=axes[2], color='red')
    axes[2].set_title('Residuals')
    axes[2].set_xlabel('')
    
    # Plot Original
    monthly_sales.plot(ax=axes[3], color='black')
    axes[3].set_title('Original')
    
    plt.tight_layout()
    plt.show()