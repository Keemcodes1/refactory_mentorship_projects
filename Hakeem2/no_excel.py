import xlwt
from xlwt import Workbook


# Define a dictionary to store the buyer information
buyer_info = {}

# Define a function to prompt the buyer to create an account
def create_account():
    email = input("Enter your email address: ")
    password = input("Enter a password: ")
    buyer_info[email] = password

# Define a function to prompt the buyer to login
def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    if email in buyer_info and buyer_info[email] == password:
        return True
    else:
        return False

# Define a function to print the available products and prices

def products():
    products = Workbook()
    sheet1 = products.add_sheet("products")
    sheet1.write(0, 0, 'name')
    sheet1.write(0, 1, 'price')
    sheet1.write(1, 0, 'apple')
    sheet1.write(1, 1, 20.8)
    sheet1.write(2, 0, 'banana')
    sheet1.write(2, 1, 50.5)
    sheet1.write(3, 0, 'rice')
    sheet1.write(3, 1, 30)
    products.save("products.xls")
    print("Available products:")
    for products, price in products.items():
        print(f"{products}: ${price}")

# Define a function to allow the buyer to choose what to buy
def buy():
    cart = {}
    while True:
        product = input("Enter the name of the product you want to buy (or 'done' to finish shopping): ")
        if product == 'done':
            break
        elif product in products:
            quantity = int(input("Enter the quantity you want to buy: "))
            cart[product] = quantity
        else:
            print("Invalid product name.")
    return cart

# Define a function to calculate the total price of the items in the cart
def calculate_total(cart):
    total = 0
    for product, quantity in cart.items():
        total += products[product] * quantity
    return total

# Define a function to print a receipt for the buyer
def print_receipt(cart, total):
    print("Receipt:")
    for product, quantity in cart.items():
        print(f"{product}: {quantity} x ${products[product]} = ${products[product] * quantity}")
    print(f"Total: ${total}")

# Main program
while True:
    if login():
        break
    else:
        print("You need to create an account first.")
        create_account()

products()
cart = buy()
total = calculate_total(cart)
print_receipt(cart, total)

