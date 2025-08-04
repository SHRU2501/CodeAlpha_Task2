stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "RELIANCE": 2391.45,
    "HDFCBANK": 1625.70,
    "TCS": 3135.80,
    "INFY": 1515.70,
    "ICICIBANK": 1477.10,
    "SBIN": 806.55,
    "HINDUNILVR": 2415.40,
    "BAJFINANCE": 913.75,
    "ITC": 409.40,
    "LT": 3442.90,
    "AAPL": 180.00,
    "TSLA": 250.00
}


# Function to calculate total investment value
def calculate_total_investment(stock_portfolio):
    total_value = 0
    for stock, quantity in stock_portfolio.items():
        if stock in stock_prices:
            total_value += stock_prices[stock] * quantity
        else:
            print(f"Stock {stock} not found in the price list.")
    return total_value

# Function to get user input for stock names and quantities
def get_user_input():
    stock_portfolio = {}
    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ")
        if stock_name.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        stock_portfolio[stock_name] = quantity
    return stock_portfolio

# Function to save the result to a file
def save_to_file(total_value, filename):
    with open(filename, 'w') as file:
        file.write(f"Total Investment Value: ${total_value}\n")

# Main function
def main():
    stock_portfolio = get_user_input()
    total_value = calculate_total_investment(stock_portfolio)
    print(f"Total Investment Value: ${total_value}")
    
    save_option = input("Do you want to save the result to a file? (yes/no): ")
    if save_option.lower() == 'yes':
        filename = input("Enter the filename (with .txt or .csv extension): ")
        save_to_file(total_value, filename)
        print(f"Result saved to {filename}")

if __name__ == "__main__":
    main()