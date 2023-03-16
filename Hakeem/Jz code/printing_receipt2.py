 # define the available products and their prices
import pandas

products = {
     "laptops"             : 300,
    "hard_disks"           : 250,
     "ram_chips"           : 150,
     "adapters"            : 100,
     "softwares"           : 7,
     "mouse"               : 5,
     "web_applications"    : 300,
     "mobile_applications" : 300,
     "hosting_services"    : 50
    
     }

#printing the list of the products and their prices.
print(".......Available Products.......")
for product, price in products.items():
    print("    "+ product + " ............. $" + str(price))

# prompt the buyer to create an account
email = input('Enter your email: ')
password = input('Enter your password: ')

# store the email and password in a dictionary called buyers
buyers = {
    email: password
}

# ask the user for login if they have a registered account else register
while True:
    choice = input('Do you have a registered account? (yes/no): ')
    if choice.lower() == 'yes':
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        if email in buyers and buyers[email] == password:
            print('Login successful.')
            break
        else:
            print('Invalid email or password. Please try again.')
    elif choice.lower() == 'no':
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        buyers[email] = password
        print('Registration successful.')
        break
    else:
        print('Invalid choice. Please try again.')

# allow the buyer to choose what to buy
cart = []
while True:
    choice = input('Enter the product name or q to quit: ')
    if choice.lower() == 'q':
        break
    elif choice.lower() in products:
        cart.append({'Product Name': choice.lower(), 'Price': products[choice.lower()]})
    else:
        print('Invalid choice. Please try again.')
        # calculate the total price of the products in the cart
total_price = sum([item['Price'] for item in cart])

# allow the buyer to pay for what they have bought
payment = 'q'
while payment.lower() != 'q':
    payment = input(f'Total price: {total_price}. Enter payment amount or q to quit: ')
    if payment.lower() == 'q':
        break
    payment_valid = True
    for char in payment:
        if char not in '0123456789.':
            payment_valid = False
            break
    if payment_valid:
        payment = float(payment)
        if payment >= total_price:
            print('Payment successful.')
            break
        else:
            print('Payment amount is less than the total price. Please try again.')
    else:
        print('Invalid payment amount. Please try again.')

# print a receipt for the buyer
print('Receipt:')
print('Product Name\tPrice')
for item in cart:
    print(f'{item["Product Name"]}\t{item["Price"]}')
print(f'Total\t{total_price}')
if payment.lower() != 'q':
    print(f'Payment\t{payment}')
    print(f'Change\t{payment - total_price}')

