# when using 'with', no need for close()
with open('py/q1/in.txt','r') as f1:
    # splitlines() omits /n when concatenating to contents[]
    # contents = f.read().splitlines()
    startNum = int(f1.readline())
    endNum = int(f1.readline())

f2 = open('py/q1/out1.txt','w')

def print_tables(startNum, endNum):
    for i in range(startNum, endNum+1):
        for j in range(1,11):
            product = i * j
            info = str(i) + " x " + str(j) + " = " + str(product)
            print(info) 
            f2.write(info)
            f2.write("\n")
        print()
        f2.write("\n")

print_tables(startNum,endNum)
f2.close()