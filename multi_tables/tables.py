def print_tables(startNum, endNum):
    for i in range(startNum, endNum+1):
        for j in range(1,11):
            product = i * j
            print(f"{i} x {j} = {product}") 
        print()

# printing tables from 3 to 20
print_tables(3,20)

def print_tables_user_input():
    startNum = int(input("Enter start number: "))
    endNum = int(input("Enter end number: "))
    print("\n")

    for i in range(startNum, endNum+1):
        for j in range(1,11):
            product = i * j
            print(f"{i} x {j} = {product}") 
        print()
# printing tables from 3 to 20
print_tables_user_input()
