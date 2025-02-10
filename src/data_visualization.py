import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_distribution(data):
    plt.figure(figsize=(15, 5))

    # Sales Distribution
    plt.subplot(1, 3, 1)
    sns.histplot(data['Sales'], bins=30, kde=True, color='blue')
    plt.title('Sales Distribution')

    # Quantity Distribution
    plt.subplot(1, 3, 2)
    sns.histplot(data['Quantity'], bins=30, kde=True, color='green')
    plt.title('Quantity Distribution')

    # Profit Distribution
    plt.subplot(1, 3, 3)
    sns.histplot(data['Profit'], bins=30, kde=True, color='red')
    plt.title('Profit Distribution')

    plt.tight_layout()
    plt.show()

def plot_monthly_sales(monthly_sales):
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='purple')
    plt.title('Monthly Sales')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.show()
