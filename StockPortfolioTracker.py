import yfinance as yf
import tkinter as tk
from tkinter import messagebox

# Fetch stock data
def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period=period)
    return stock_data

# Add stocks
def add_stock(portfolio, ticker_entry, shares_entry, price_entry):
    ticker = ticker_entry.get().upper()
    shares = int(shares_entry.get())
    purchase_price = float(price_entry.get())
    
    portfolio[ticker] = {
        'shares': shares,
        'purchase_price': purchase_price
    }
   
    messagebox.showinfo("Success", f"Added {shares} shares of {ticker} to portfolio at {purchase_price}$ per share.")
    ticker_entry.delete(0, tk.END)
    shares_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

# Remove stock
def remove_stock(portfolio, ticker_entry):
    ticker = ticker_entry.get().upper()
    if ticker in portfolio:
        del portfolio[ticker]
        messagebox.showinfo("Success", f"Removed {ticker} from the portfolio.")
        ticker_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Error", f"{ticker} not found in portfolio.")
        ticker_entry.delete(0, tk.END)

# View portfolio
def view_portfolio(portfolio):
    if not portfolio:
        messagebox.showinfo("Portfolio", "Your portfolio is empty.")
        return
    
    portfolio_str = ""
    for ticker, data in portfolio.items():
        portfolio_str += f"{ticker}: {data['shares']} shares at {data['purchase_price']}$ per share\n"
    
    messagebox.showinfo("Portfolio", portfolio_str)

# Track portfolio value
def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")["Close"].iloc[-1]

def calculate_portfolio_value(portfolio):
    total_value = 0
    for ticker, data in portfolio.items():
        current_price = get_current_price(ticker)
        total_value += data['shares'] * current_price
    return total_value

# Calculate gains/losses
def calculate_gains(portfolio):
    gains = 0
    for ticker, data in portfolio.items():
        current_price = get_current_price(ticker)
        purchase_price = data['purchase_price']
        gain = (current_price - purchase_price) * data['shares']
        gains += gain
    return gains

# View performance
def view_performance(portfolio):
    gains = calculate_gains(portfolio)
    portfolio_value = calculate_portfolio_value(portfolio)

    if gains > 0:
        messagebox.showinfo("Performance", f"Total Portfolio Value: {portfolio_value:.2f} $\nTotal Portfolio Gains: {gains:.2f} $")
    elif gains < 0:
        messagebox.showinfo("Performance", f"Total Portfolio Value: {portfolio_value:.2f} $\nTotal Portfolio Losses: {gains:.2f} $")
    else:
        messagebox.showinfo("Performance", f"Total Portfolio Value: {portfolio_value:.2f} $\nNo Gains or Losses")

def main():
    portfolio = {}

    # Create the main window
    root = tk.Tk()
    root.title("Stock Portfolio Manager")
    root.geometry("400x300")  # Increased size to accommodate larger buttons

    # Ticker
    tk.Label(root, text="Stock Ticker:").grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
    ticker_entry = tk.Entry(root)
    ticker_entry.grid(row=0, column=1, padx=10, pady=5)

    # Shares
    tk.Label(root, text="Number of Shares:").grid(row=1, column=0, padx=10, pady=5, sticky='nsew')
    shares_entry = tk.Entry(root)
    shares_entry.grid(row=1, column=1, padx=10, pady=5)

    # Purchase Price
    tk.Label(root, text="Purchase Price:").grid(row=2, column=0, padx=10, pady=5, sticky='nsew')
    purchase_price_entry = tk.Entry(root)
    purchase_price_entry.grid(row=2, column=1, padx=10, pady=5)

    # Buttons
    tk.Button(root, text="Add stock", width=20, height=2, command=lambda: add_stock(portfolio, ticker_entry, shares_entry, purchase_price_entry)).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(root, text="Remove Stock", width=20, height=2, command=lambda: remove_stock(portfolio, ticker_entry)).grid(row=3, column=1, padx=10, pady=10)
    tk.Button(root, text="View Portfolio", width=20, height=2, command=lambda: view_portfolio(portfolio)).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(root, text="View Performance", width=20, height=2, command=lambda: view_performance(portfolio)).grid(row=4, column=1, padx=10, pady=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
