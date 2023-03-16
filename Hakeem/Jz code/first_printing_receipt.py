'''1)printing receipts after shopping
Create a small shop with some products and prices where a buyer can view the list of a vailable products and their prices.
'''
#A dictionary of products and their prices
import openpyxl
products = {
     "laptops"             : 'negotiable',
    "hard_disks"           : 250,
     "Ram_chips"           : 150,
     "Adapters"            : 100,
     "Softwares"           : 7,
     "mouse"               : 5,
     "web_applications"    : 'negotiable',
     "mobile_applications" : 'negotiable',
     "Hosting_services"    :'negotiable'
    
     }
#printing the list of the products and their prices.
print(".......Available Products.......")
for product, price in products.items():
    print("    "+ product + " ............. $" + str(price))

    '''when program runs, it should prompt buyer to create account using password and email and store this in an excel sheet.
................................................................................
Then ask user for login if he has registered account else register
'''
#prompt the buyer to create an account
while True:
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    #check if the email alraedy exists in excel sheet 
    account_workbook = openpyxl.load_workbook('accounts.xlsx')
    account_worksheet = account_workbook.active
    existing_emails = [cell.value for cell in account_worksheet['A'][1:]]
    if email in existing_emails:
        print('This email address already exists.Please login.')
        break
    else:
        #add the email and password to the excel sheet
        next_row = account_worksheet.max_row + 1
        account_worksheet[f'A{next_row}'] = email
        account_worksheet[f'B{next_row}'] = password
        account_workbook.save('accounts.xlsx')
        print('Account created successfully')
        break
    #prompt the buyer to login or register a new account

#while True:
    
      
