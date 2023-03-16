import xlwt
from xlwt import Workbook
keem = Workbook()
sheet1 = keem.add_sheet("my excel sheet")
sheet1.write(1, 0, 'student_names')
sheet1.write(2, 0, 'student numbers')
keem.save("names.xls")