"""stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

total_investment = 0

while True:
  stock_name=input("Enter the stock name:").upper()
  quantity=int(input("Enter quantity:"))
  total=stocks[stock_name]*quantity
  total_investment = total_investment + total
  print("Current Total:",total_investment)
  choice=input("Add another stock? (y/n):")
  if choice.lower()== "n":
    break

print("\n------ STOCK PORTFOLIO ------")
print("Stock:", stock_name)
print("Price:", stocks[stock_name])
print("Quantity:", quantity)
print("Total Investment:", total)
print("\n------ PORTFOLIO SUMMARY ------")
print("Total Investment Value:",total_investment)"""


# ..............................................................................................

# Stock Portfolio Tracker
# CodeAlpha Internship Task 2

# Dictionary storing stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

# Variable to store total investment value
total_investment = 0

# Program Heading
print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

# Loop to allow multiple stock entries
while True:

    # Get stock name from user
    stock_name = input("\nEnter the stock name: ").upper()

    # Check if stock exists in dictionary
    if stock_name not in stocks:
        print("Stock not found!")
        continue

    # Get quantity from user
    quantity = int(input("Enter Quantity: "))

    # Calculate investment for selected stock
    total = stocks[stock_name] * quantity

    # Add investment to portfolio total
    total_investment += total

    # Display stock details
    print("\n------------------------------")
    print("Stock      :", stock_name)
    print("Price      :", stocks[stock_name])
    print("Quantity   :", quantity)
    print("Investment :", total)
    print("------------------------------")

    # Display running portfolio value
    print("Current Portfolio Value:", total_investment)

    # Ask user whether to continue
    choice = input("\nAdd another stock? (y/n): ")

    # Exit loop if user chooses no
    if choice.lower() == "n":
        break

# Display final portfolio summary
print("\n" + "-" * 40)
print("       PORTFOLIO SUMMARY")
print("-" * 40)

print("Total Investment Value:", total_investment)

print("\nThank you for using")
print("Stock Portfolio Tracker")

print("=" * 40)