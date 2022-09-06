def main():

    import csv

    infile = open("EmployeePay.csv",'r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile:
        print("ID: ", record[0])
        print("First name: ", record[1])
        print("Last Name: ", record[2])
        salary = (float(record[3])) * float(record[4]) + float(record[3])
        print('Total Pay: ', '$' ,format(salary, ',.2f'),sep = '')
        input('Press enter for next employee')
main()
