
import csv
from prettytable import PrettyTable

with open('Employee.csv') as CSVR:
    emp_details = csv.reader(CSVR)

    prtTbl = PrettyTable(next(emp_details))

    for rec in emp_details:
        prtTbl.add_row(rec)

print(prtTbl)


#    colnames = next(emp_details)
    # print(colnames)
    # for rec in emp_details:
    #     print(*rec)
