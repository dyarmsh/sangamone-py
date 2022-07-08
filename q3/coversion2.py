

def convert():
    LHSValue = int(contents[0])
    RHSValue = int(contents[3])
    equals = contents[2]

    spacer = " "
    LHSUnits = contents[1]
    RHSUnits = contents[4]

    line1 = str(1) + spacer + LHSUnits + spacer + equals + spacer + str(RHSValue/LHSValue) + spacer + RHSUnits
    line2 = str(1) + spacer + RHSUnits + spacer + equals + spacer + str(LHSValue/RHSValue) + spacer + LHSUnits

    print(line1)
    print(line2)

f1 = open("py/q3/inConvert.txt",'r')
f2 = open("py/q3/inConvert.txt",'r')

for i in range(0,len(f1.readlines())):
    contents = f2.readline()
    
    contents = contents.split(" ")
    contents[4] = contents[4].replace("\n","")
    convert()



