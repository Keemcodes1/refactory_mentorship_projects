import xlrd
import xlwt

# Load the product information from an Excel file
workbook = xlrd.open_workbook('products.xls')
sheet = workbook.sheet_by_index(0)

# Load the product information into a dictionary
products = {}
for product_row in range(1, sheet.nrows):
    name = sheet.cell(product_row, 0).value
    price = sheet.cell(product_row, 1).value
    products[name] = price

# Prompt the buyer to create an account
while True:
    email = input("Enter your email address: ")
    password = input("Choose a password: ")

    # Check if the email address already exists in the accounts file
    workbook = xlrd.open_workbook('accounts.xls')
    sheet = workbook.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        if sheet.cell(row, 0).value == email:
            print("An account with that email address already exists. Please try again.")
            break
    else:
        # Add the new account to the accounts file
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('accounts')
        row = sheet.nrows
        sheet.write(row, 0, email)
        sheet.write(row, 1, password)
        workbook.save('accounts.xls')
        break

# Prompt the buyer to login
while True:
    email_input = input("Enter your email address: ")
    password_input = input("Enter your password: ")

    # Check if the email and password match an account in the accounts file
    workbook = xlrd.open_workbook('accounts.xls')
    sheet = workbook.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        if sheet.cell(row, 0).value == email_input and sheet.cell(row, 1).value == password_input:
            break
    else:
        print("Invalid email or password. Please try again.")
        continue
    break

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
