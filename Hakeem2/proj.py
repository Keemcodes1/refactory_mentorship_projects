import pandas as pd
import getpass
import random

# Create an Excel sheet called “products” with the list of available products and their prices
Products_df = pd.DataFrame({
    'Product': ['Product A', 'Product B', 'Product C'],
    'Price': [100, 200, 300]
})
Products_df.to_excel('products.xlsx', index=False)

# Create an Excel sheet called “accounts” to store user information
Accounts_df = pd.DataFrame(columns=['Email', 'Password', 'Wallet'])
Accounts_df.to_excel('accounts.xlsx', index=False)

# Function to validate user input
def validate_input(input_str, choices):
    while True:
        user_input = input(input_str)
        if user_input in choices:
            return user_input
        else:
            print('Invalid input. Please try again.')

# Function to generate a random transaction ID
def generate_transaction_id():
    return random.randint(100000, 999999)

# Function to display the products
def display_products():
    products_df = pd.read_excel('products.xlsx')
    print(products_df.to_string(index=False))

# Function to calculate the total bill
def calculate_total_bill(cart):
    products_df = pd.read_excel('products.xlsx')
    total_bill = 0
    for item in cart:
        total_bill += products_df.loc[item]['Price']
    return total_bill

# Function to print the receipt
def checkout(cart, total_bill):
    print('------ RECEIPT ------')
    print('Transaction ID:', generate_transaction_id())
    print('Items Purchased: ')
    products_df = pd.read_excel('products.xlsx')
    total_price =0
    for item in cart:
        total_price += item[2] * item[1]
        print("your total is: {:.2f}".format(total_price))
        if total_bill > wallet_balance:
            print("your wallet balance is not enough to pay for your cart.would you like to remove some items from your cart or top up your wallet balance?")
            response = input("enter'1' to remove items, '2' to top up your wallet balance, or '3' to cancel: ")
            if response == '1':
                #cart = remove_items_from_cart(cart)
                checkout(cart,wallet_balance,total_bill)
            elif response == '2':
               # wallet_balance = top_up_wallet(wallet_balance)
                checkout(cart,wallet_balance,total_bill)
            else:
                print("Checkout cancelled.")
        else:
            print("your wallet balance is enough to pay for your cart.")
            wallet_balance == total_bill          
                 # Update_wallet_balance(wallet_balance)         
        print(products_df.loc[item]['Product'], '-', products_df.loc[item]['Price'])
    print('Total Bill:', total_bill)
    print('---------------------')

# Main program
while True:
    # Ask the user for login credentials
    Email = input('Enter your email address: ')
    Password = getpass.getpass('Enter your password: ')

    # Check if the user’s email and password are correct
    accounts_df = pd.read_excel('accounts.xlsx')
    account = accounts_df.loc[(accounts_df['Email'] == Email) & (accounts_df['Password'] == Password)]
    if len(account) == 1:
        print('Welcome back,', email)
        wallet_balance = account.iloc[0]['Wallet']
    else:
        # If the user doesn’t have an account, prompt them to create one
        print('Incorrect email or password. Would you like to create an account?')
        create_account = validate_input('Enter Y for Yes or N for No: ', ['Y', 'N'])
        if create_account == 'Y':
            email = input('Enter your email address: ')
            password = getpass.getpass('Enter your password: ')
            wallet_balance = 0
            new_account = pd.DataFrame({
                'Email': [email],
                'Password': [password],
                'Wallet': [wallet_balance]
            })
            accounts_df = pd.concat([accounts_df, new_account], ignore_index=True)
            accounts_df.to_excel('accounts.xlsx', index=False)
        else:
            continue

    # Display the user’s wallet balance
    print('Your wallet balance:', wallet_balance)

    # Display the products
    print('Available products:')
    display_products()

    # Ask the user what they want to buy
    cart = []
    while True:
        item = input('Enter the index of the product you want to buy (or Q to quit): ')
        if item == 'Q':
            break
        
    # Display the receipt to the buyer
    print("\nThank you for shopping with us! Here's your receipt:\n")
    print("===================================================")
    print("{:<10s}{:>10s}{:>10s}".format("Product", "Quantity", "Price"))
    print("---------------------------------------------------")
    for i in range(len(cart)):
        print("{:<10s}{:>10d}{:>10.2f}".format(cart[i][0], cart[i][1], cart[i][2]))
    print("---------------------------------------------------")
    print("{:<20s}{:>10.2f}".format("Total:", checkout(cart,total_bill='')))
    print("===================================================")

