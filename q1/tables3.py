
f1 = open('py/q1/in2.txt','r')
content = f1.read()
print(content)

# getting rid of the comma
content = content.split(",") 
print(content)

f2 = open("py/q1/out2.txt","w")

def tables(startNum,endNum):
    for i in range(startNum,endNum+1):
        for j in range(1,11):
            product = i * j
            info = str(i) + " * " + str(j) + " = " + str(product)
            print(info)
            f2.write(info)
            f2.write("\n")
        print()
        f2.write("\n")
    f2.close()
tables(int(content[0]),int(content[1]))