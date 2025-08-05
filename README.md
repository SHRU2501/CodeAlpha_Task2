# CodeAlpha_Task2
A Python-based CLI tool designed to help users monitor and analyze their stock investments. It calculates total portfolio value, individual stock performance, and visualizes asset allocation with dynamic pie charts.  This project showcases modular coding practices, data preprocessing, and backend integration with scope for expanding into real-time.


Input CSV format:
Stock,Quantity,Buy_Price,Current_Price
AAPL,10,120,150
TSLA,5,600,720

Output:
Total Portfolio Value: ₹[calculated amount]
Gain/Loss: [percentage or absolute value]


## Features
1)Portfolio Valuation Calculates total portfolio value based on user-input stock data.

2)Individual Stock Analysis Computes gain/loss percentage and value for each stock.

3)Modular Financial Computations Cleanly separated functions for readability and scalability.

4)CSV File Handling Reads portfolio data from structured .csv files for flexible input.

5)Data Preprocessing Ensures robust handling of incomplete or malformed entries.

6)CLI Interface Simple command-line interaction with options to update or rerun analyses.

7)Extendable Design Built with modular structure for easy integration of real-time stock APIs like Yahoo Finance or Alpha Vantage.


## Challenges Faced

- Addressed data type mismatches during CSV parsing
- Optimized pie chart rendering for edge cases with limited assets
- Debugged encoding issues during file saving on Windows environments

  
## Testing

Tested with multiple portfolio CSV formats to validate:
- Correct calculation of total value
- Accurate gain/loss computation

## Learning Outcomes

- Strengthened understanding of CLI tool development using Python
- Gained experience in modular function design and CSV data handling

 ## Version History

- **v1.0** Initial release with CLI, CSV support, pie chart visualization
- **v1.1** Added data validation checks and clean output formatting

  git clone https://github.com/SHRU2501/CodeAlpha_Task2.git
cd CodeAlpha_Task2
python3 portfolio_tracker.py

├── portfolio_tracker.py
├── assets/
│   └── sample_portfolio.csv
├── README.md
licesnce MIT


 
