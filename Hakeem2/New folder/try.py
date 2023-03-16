import pandas as pd

def display_products():
    products_df = pd.read_csv("products.csv")
    print("Available products:")
    print(products_df.to_string(index=False))
def checkout(product_df):
    print('Checkout')
    total = 0
    while True:
        product_id = input("Enter product ID to add to cart, or 'q' to checkout: ")
        if product_id.lower() == 'q':
            break
        quantity = int(input("Enter quantity: "))
        product_df = product_df.loc[product_df['id'] == int(product_id)]
        price = product_df['price'].values[0]
        total += price * quantity
    print(f'Total: {total}')   
    checkout(product_df)


def register():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    with open("users.txt", "a") as f:
        f.write(email + "," + password + "\n")
    print("Registration successful!")

def login():
    print('Login')
    email = input('Enter your email address: ')
    password = input('Enter your password: ')
    # authenticate user
    print('Login successful!')  
    #checkout(product_df)
     # pass product_df to checkout function

'''def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as f:
        for line in f:
            line = line.strip()
            user_email, user_password = line.split(",")
            if user_email == email and user_password == password:
                print("Login successful!")
                checkout()
                break
        else:
            print("Invalid email or password.")
'''



while True:
    print("\nWelcome to the shop!")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
