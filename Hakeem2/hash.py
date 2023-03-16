import xlwt
import pandas as pd
import hashlib

# Create a new Excel workbook and worksheet for products
products_wb = xlwt.Workbook()
products_ws = products_wb.add_sheet("Products")

# Add product information to the worksheet
products_ws.write(0, 0, "Name")
products_ws.write(0, 1, "Price")
products_ws.write(1, 0, "Product A")
products_ws.write(1, 1, 10.99)
products_ws.write(2, 0, "Product B")
products_ws.write(2, 1, 5.99)

# Save the products workbook
products_wb.save("products.xls")

# Load the product information into a dictionary
products_df = pd.read_excel("products.xls")
products = {}
for index, row in products_df.iterrows():
    products[row["Name"]] = row["Price"]
# Create a new Excel workbook and worksheet for products
accounts_wb = xlwt.Workbook()
accounts_ws = accounts_wb.add_sheet("accounts")
# Add account information to the worksheet
accounts_ws.write(0, 0, "Name")
accounts_ws.write(0, 1, "Price")
accounts_ws.write(1, 0, "Product A")
accounts_ws.write(1, 1, 10.99)
accounts_ws.write(2, 0, "Product B")
accounts_ws.write(2, 1, 5.99)

# Save the products workbook
accounts_wb.save("accounts.xls")

# Load the account information into a DataFrame
accounts_df = pd.read_excel("accounts.xls", index_col="email@gmail.com")

# Prompt the buyer to create an account
while True:
    email = input("Enter your email address: ")
    if email in accounts_df.index:
        print("An account with that email address already exists. Please try again.")
        continue
    else:
        password = input("Choose a password: ")
        # Hash the password before storing it in the DataFrame
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        accounts_df.loc[email] = hashed_password
        accounts_df.to_excel("accounts.xls")
        break

# Prompt the buyer to log in
while True:
    email_input = input("Enter your email address: ")
    password_input = input("Enter your password: ")
    # Hash the input password to compare it to the stored password
    hashed_input_password = hashlib.sha256(password_input.encode()).hexdigest()
    if email_input in accounts_df.index and accounts_df.loc[email_input, "password"] == hashed_input_password:
        break
    else:
        print("Invalid email or password. Please try again.")

# Show the available products
print("Available products:")
for name, price in products.items():
    print(f"{name}: ${price:.2f}")

# Let the buyer choose what to buy
cart = {}
while True:
    item = input("Enter a product name to add to your cart, or 'done' to checkout: ")
    if item == "done":
        break
    if item not in products:
        print("Invalid product name. Please try again.")
        continue
    quantity = int(input(f"How many {item}s would you like to buy? "))
    cart[item] = quantity

# Calculate the total price
total_price = sum(products[item] * quantity for item, quantity in cart.items())

# Ask the buyer to pay
while True:
    payment = float(input(f"Your total is ${total_price:.2f}. Enter your payment amount: "))
    if payment < total_price:
        print("Insufficient payment. Please try again.")
    else:
        break

# Print the receipt
print("Receipt:")
for item, quantity in cart.items():
    print(f"{item} x {quantity}: ${products[item] * quantity:.2f}")
print(f"Total: ${total_price:.2f}")
print(f"Payment: ${payment:.2f}")
print(f"Change: ${payment - total_price:.2f}")
