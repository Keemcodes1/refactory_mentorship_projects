
import xlwt
from xlwt import Workbook
keem = Workbook ()
sheet1 = keem.add_sheet("my excel sheet")
sheet1.write(1, 0, 'products')
sheet1.write(2, 0, 'accounts')
keem.save("products.xls")

# Load the product information from an Excel file
#products_df = pd.read_excel(r'C:\Users\KEEM\Documents\products.xls')




# Convert the product information to a dictionary
products = {}
for _, row in Workbook():
    products[row['name']] = row['price']

# Load the account information from an Excel file
accounts_df = sheet1.read('accounts.xls', index_col='email')

# Prompt the buyer to create an account
while True:
    email = input("Enter your email address: ")
    if email in accounts_df.index:
        print("An account with that email address already exists. Please try again.")
        continue
    else:
        password = input("Choose a password: ")
        accounts_df.loc[email] = password
        accounts_df.to_excel('accounts.xls')
        break

# Prompt the buyer to login
while True:
    email_input = input("Enter your email address: ")
    password_input = input("Enter your password: ")

    if email_input in accounts_df.index and accounts_df.loc[email_input, 'password'] == password_input:
        break
    else:
        print("Invalid email or password. Please try again.")

# Show the available products
print("Available products:")
for name, price in products.items():
    print(f"{name}: ${price}")

# Let the buyer choose what to buy
cart = {}
while True:
    item = input("Enter a product name to add to your cart, or 'done' to checkout: ")
    if item == 'done':
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
    payment = float(input(f"Your total is ${total_price}. Enter your payment amount: "))
    if payment < total_price:
        print("Insufficient payment. Please try again.")
    else:
        break

# Print the receipt
print("Receipt:")
for item, quantity in cart.items():
    print(f"{item} x {quantity}: ${products[item] * quantity}")
print(f"Total: ${total_price}")
print(f"Payment: ${payment}")
print(f"Change: ${payment - total_price}")