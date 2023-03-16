import pandas as pd
from getpass import getpass

# Load products from Excel sheet

try:
    products_df = pd.read_excel('products.xlsx')
except FileNotFoundError:
    print('Products file not found. Please make sure the file exists.')

# Create users DataFrame to store registered users
users_df = pd.DataFrame(columns=['email', 'password'])

# Define functions to handle user registration and login
def register():
    email = input("Enter your email address: ")
    password = getpass("Enter your password: ")
    users_df.loc[len(users_df)] = [email, password]
    print("Registration successful!")
    
def login():
    email = input("Enter your email address: ")
    password = getpass("Enter your password: ")
    if len(users_df.loc[(users_df['email'] == email) & (users_df['password'] == password)]) == 0:
        print("Invalid email or password")
        return None
    else:
        print("Login successful!")
        return email

# Define function to display available products
def display_products():
    print("Available products:")
    print(products_df)

# Define function to calculate total cost of items in cart
def calculate_total_cost(cart):
    total_cost = 0
    for index, row in cart.iterrows():
        total_cost += row['Price'] * row['Quantity']
    return total_cost

# Define function to handle the checkout process
def checkout(email):
    # Create empty cart DataFrame
    cart = pd.DataFrame(columns=['Product', 'Price', 'Quantity'])
    
    # Loop to allow user to add items to cart
    while True:
        display_products()
        product = input("Enter the name of the product you want to buy (or 'done' to finish): ")
        if product == 'done':
            break
        elif product not in products_df['Product'].tolist():
            print("Invalid product name")
            continue
        else:
            price = products_df.loc[products_df['Product'] == product, 'Price'].iloc[0]
            quantity = int(input("Enter the quantity you want to buy: "))
            cart.loc[len(cart)] = [product, price, quantity]
    
    # Calculate total cost and display to user
    total_cost = calculate_total_cost(cart)
    print("Total cost: $", total_cost)
    
    # Loop to handle payment process
    while True:
        payment = float(input("Enter payment amount: $"))
        if payment < total_cost:
            print("Payment amount insufficient")
        else:
            break
    
    # Print receipt to terminal
    print("----- RECEIPT -----")
    print("Buyer email:", email)
    print("Items purchased:")
    print(cart)
    print("Total cost: $", total_cost)
    print("Change: $", payment - total_cost)
    print("-------------------")

# Main program loop
while True:
    print("Welcome to the shop!")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        register()
    elif choice == '2':
        email = login()
        if email is not None:
            checkout(email)
    elif choice == '3':
        break
    else:
        print("Invalid choice")
import pandas as pd
from getpass import getpass

# Load products from Excel sheet
products_df = pd.read_excel('products.xlsx')

# Create users DataFrame to store registered users
users_df = pd.DataFrame(columns=['email', 'password'])

# Define functions to handle user registration and login
def register():
    email = input("Enter your email address: ")
    password = getpass("Enter your password: ")
    users_df.loc[len(users_df)] = [email, password]
    print("Registration successful!")
    
def login():
    email = input("Enter your email address: ")
    password = getpass("Enter your password: ")
    if len(users_df.loc[(users_df['email'] == email) & (users_df['password'] == password)]) == 0:
        print("Invalid email or password")
        return None
    else:
        print("Login successful!")
        return email

# Define function to display available products
def display_products():
    print("Available products:")
    print(products_df)

# Define function to calculate total cost of items in cart
def calculate_total_cost(cart):
    total_cost = 0
    for index, row in cart.iterrows():
        total_cost += row['Price'] * row['Quantity']
    return total_cost

# Define function to handle the checkout process
def checkout(email):
    # Create empty cart DataFrame
    cart = pd.DataFrame(columns=['Product', 'Price', 'Quantity'])
    
    # Loop to allow user to add items to cart
    while True:
        display_products()
        product = input("Enter the name of the product you want to buy (or 'done' to finish): ")
        if product == 'done':
            break
        elif product not in products_df['Product'].tolist():
            print("Invalid product name")
            continue
        else:
            price = products_df.loc[products_df['Product'] == product, 'Price'].iloc[0]
            quantity = int(input("Enter the quantity you want to buy: "))
            cart.loc[len(cart)] = [product, price, quantity]
    
    # Calculate total cost and display to user
    total_cost = calculate_total_cost(cart)
    print("Total cost: $", total_cost)
    
    # Loop to handle payment process
    while True:
        payment = float(input("Enter payment amount: $"))
        if payment < total_cost:
            print("Payment amount insufficient")
        else:
            break
    
    # Print receipt to terminal
    print("----- RECEIPT -----")
    print("Buyer email:", email)
    print("Items purchased:")
    print(cart)
    print("Total cost: $", total_cost)
    print("Change: $", payment - total_cost)
    print("-------------------")

# Main program loop
while True:
    print("Welcome to the shop!")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        register()
    elif choice == '2':
        email = login()
        if email is not None:
            checkout(email)
    elif choice == '3':
        break
    else:
        print("Invalid choice")
