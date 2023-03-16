# open the workbook and select the first worksheet
workbook = xlrd.open_workbook('wed.xlsx')
worksheet = workbook.sheet_by_index(0)

# get the number of rows in the worksheet
num_rows = worksheet.nrows

# create a new workbook and worksheet
new_workbook = xlsxwriter.Workbook('wed_price.xlsx')
new_worksheet = new_workbook.add_worksheet()

# iterate through each row in the worksheet and calculate the price
for row in range(num_rows):
    # get the email and password from the current row
    email = worksheet.cell_value(row, 0)
    password = worksheet.cell_value(row, 1)

    # calculate the price
    price = calculate_price(email, password)

    # write the email, password, and price to the new worksheet
    new_worksheet.write(row, 0, email)
    new_worksheet.write(row, 1, password)
    new_worksheet.write(row, 2, price)

# close the new workbook
new_workbook.close()
