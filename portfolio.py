# Stock Portfolio Tracker
# Simple program to calculate total investment in stocks

# Hardcoded stock prices


stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 130, "MSFT": 320}
portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker!")
#Take user input
while True: #---->Starts an infinite loop (while True) to take multiple inputs.
    stock = input("Enter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    # Add quantity instead of overwriting
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
total_investment = sum(stock_prices[s] * q for s, q in portfolio.items())

# Display portfolio summary
print("\n💰 Portfolio Summary:")
for s, q in portfolio.items():
    print(f"{s}: {q} shares × ${stock_prices[s]} = ${stock_prices[s] * q}")

print(f"\nTotal Investment: ${total_investment}")

# Save summary to file
with open("portfolio_summary.txt", "w") as file:
    for s, q in portfolio.items():
        file.write(f"{s}: {q} × ${stock_prices[s]} = ${stock_prices[s]*q}\n")
    file.write(f"\nTotal Investment: ${total_investment}")

print("Data saved to portfolio_summary.txt ✅")
