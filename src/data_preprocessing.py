import pandas as pd

def load_and_preprocess_data(file_path):
    try:
        data = pd.read_csv(file_path, encoding='latin1')
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None, None
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return None, None

    # Drop columns with unique values (Row Id) or single value (Country)
    unique_col = [col for col in data.columns if data[col].nunique() == 1]
    data.drop(columns=unique_col, inplace=True)

    # Drop duplicate rows
    data.drop_duplicates(inplace=True)

    # Convert 'Order Date' to datetime
    data['Order Date'] = pd.to_datetime(data['Order Date'])

    # Create monthly sales Series
    monthly_sales = data.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales'].sum()
    
    # Ensure it's a Series with DatetimeIndex
    monthly_sales = pd.Series(monthly_sales.values, index=monthly_sales.index)
    
    # Set the index name
    monthly_sales.index.name = 'Date'
    
    return data, monthly_sales