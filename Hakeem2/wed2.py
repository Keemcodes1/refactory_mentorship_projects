import xlwt
import xlrd

# Create a workbook and add a sheet
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('accounts')

# Add column headers to the sheet
sheet.write(0, 0, 'Email')
sheet.write(0, 1, 'Password')

# Save the workbook to a file
workbook.save('accounts.xls')

# Load the product information from an Excel file
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('products')
sheet.write(0, 0, 'Name')
sheet.write(0, 1, 'Price')
sheet.write(1, 0, 'laptops')
sheet.write(1, 1, 10)
sheet.write(2, 0, 'Phones')
sheet.write(2, 1, 20)
workbook.save('products.xls')

# Load the product information into a dictionary
products = {}
workbook = xlrd.open_workbook('products.xls')
sheet = workbook.sheet_by_index(0)
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
    payment = float(input(f"Your total is ${total_price:.2}"))
