
def print_tables_user_input():
    startNum = int(input("Enter start number: "))
    endNum = int(input("Enter end number: "))
    print("\n")

    for i in range(startNum, endNum+1):
        num = i
        extension = ".txt"
        filename = str(num) + extension

        f = open("py/q1/" + filename, 'w')
        for j in range(1,11):
            product = i * j
            info = str(i) + " * " + str(j) + " = " + str(product)

            f.write(info)
            f.write("\n")
        print()
    f.close()
print_tables_user_input()