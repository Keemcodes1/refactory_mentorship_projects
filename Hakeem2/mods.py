import xlwt
import xlrd
import random

# Create a workbook and add a sheet for accounts and wallets
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('accounts')
sheet.write(0, 0, 'Email')
sheet.write(0, 1, 'Password')
sheet.write(0, 2, 'Wallet Balance')
workbook.save('accounts.xls')

# Add product information to the sheet
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('products')
sheet.write(0, 0, 'Index')
sheet.write(0, 1, 'Name')
sheet.write(0, 2, 'Price')
sheet.write(1, 0, 1)
sheet.write(1, 1, 'Laptop')
sheet.write(1, 2, 1000)
sheet.write(2, 0, 2)
sheet.write(2, 1, 'Phone')
sheet.write(2, 2, 500)
workbook.save('products.xls')

# Load the product information into a dictionary
products = {}
workbook = xlrd.open_workbook('products.xls')
sheet = workbook.sheet_by_index(0)
for product_row in range(1, sheet.nrows):
    index = int(sheet.cell(product_row, 0).value)
    name = sheet.cell(product_row, 1).value
    price = sheet.cell(product_row, 2).value
    products[index] = (name, price)

# Load the account information into a dictionary
accounts = {}
workbook = xlrd.open_workbook('accounts.xls')
sheet = workbook.sheet_by_index(0)
for account_row in range(1, sheet.nrows):
    email = sheet.cell(account_row, 0).value
    password = sheet.cell(account_row, 1).value
    wallet_balance = sheet.cell(account_row, 2).value
    accounts[email] = (password, wallet_balance)

# Display wallet details
for email, (password, wallet_balance) in accounts.items():
    print(f"Email: {email}, Wallet Balance: ${wallet_balance:.2f}")

# Prompt the buyer to create an account
while True:
    email = input("Enter your email address: ")
    password = input("Choose a password: ")
    wallet_balance = 0

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
        sheet.write(row, 2, wallet_balance)
        workbook.save('accounts.xls')
        accounts[email] = (password, wallet_balance)
        print(f"Account created successfully. Email: {email}, Password: {password}, Wallet Balance: ${wallet_balance:.2f}")
        break

# Prompt the buyer to login
while True:
    email_input = input("Enter your email address: ")
    password_input = input("Enter your password: ")
# Check if the email and password match an account in the accounts file

    workbook = xlrd.open_workbook('accounts.xls')
    sheet = workbook.sheet_by_index(0)
    account_found = False
    for row in range(1, sheet.nrows):
        if sheet.cell(row, 0).value == email_input and sheet.cell(row, 1).value == password_input:
            account_found = True
        wallet = sheet.cell(row, 2).value
        break

    if account_found:
        print("Login successful.")
    break
else:
print()
