import datetime as dt

today = dt.datetime.now()
year1 = today.year
month1 = today.month
day1 = today.day
hour1 = today.hour
min1 = today.minute
sec1 = today.second

def print_tables_user_input():
    startNum = int(input("Enter start number: "))
    endNum = int(input("Enter end number: "))
    print("\n")
    
    extension = ".txt"
    filename = str(startNum) + "_" + str(year1) + str(month1).zfill(2) + str(day1).zfill(2) + "_" + str(hour1).zfill(2) + str(min1).zfill(2) + str(sec1).zfill(2) + extension
    f = open("py/q1/" + filename, 'w')

    for i in range(startNum, endNum+1):
        for j in range(1,11):
            product = i * j
            info = str(i) + " * " + str(j) + " = " + str(product)
            print(info)
            f.write(info)
            f.write("\n")
        print()
        f.write("\n")
    f.close()
    
# printing tables from 3 to 20
print_tables_user_input()