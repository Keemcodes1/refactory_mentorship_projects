import json
import os
print(os.getcwd())

# Load products data from file
try:
    with open('products.json') as file:
        products_data = json.load(file)
except FileNotFoundError:
    print("Products file not found. Please make sure the file exists.")
    exit()

# Load users data from file
try:
    with open('users.json') as file:
        users_data = json.load(file)
except FileNotFoundError:
    print("Users file not found. Please make sure the file exists.")
    exit()

# Function to validate user input for integer choices
def validate_input(prompt):
    while True:
        try:
            choice = int(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return choice

# Function to handle user registration
def register():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    name = input("Enter your name: ")

    # Check if email already exists
    if email in users_data:
        print("User with this email already exists. Please try again.")
        return

    # Add new user to users data
    users_data[email] = {'password': password, 'name': name}

    # Save updated users data to file
    with open('users.json', 'w') as file:
        json.dump(users_data, file)

    print("Registration successful.")

# Function to handle user login
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    # Check if email exists in users data
    if email not in users_data:
        print("User with this email does not exist. Please try again.")
        return

    # Check if password is correct
    if users_data[email]['password'] != password:
        print("Invalid password. Please try again.")
        return

    print(f"Welcome, {users_data[email]['name']}!")

    # Allow user to shop
    shop()

# Function to display all available products
def display_products():
    print("Available products:")
    for product in products_data:
        print(f"{product['name']} - {product['price']}")

# Function to handle shopping
def shop():
    while True:
        print("Select an option:")
        print("1. Display available products")
        print("2. Checkout")
        print("3. Quit")
        choice = validate_input("Enter your choice: ")

        if choice == 1:
            display_products()
        elif choice == 2:
            print("Thank you for shopping with us!")
            break
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to handle program flow
def main():
    print("Welcome to the shop!")

    while True:
        print("Select an option:")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = validate_input("Enter your choice: ")

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
