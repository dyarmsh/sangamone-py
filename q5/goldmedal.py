f = open("py/q5/data.txt", 'r')

names = []
eng = []
maths = []
phy = []
chem = []
bio = []

subjects = [eng, maths, phy, chem, bio]
sums = []

engToppersIndex = []
mathsToppersIndex = []
phyToppersIndex = []
chemToppersIndex = []
bioToppersIndex = []

for line in f:
    # formatting data 
    line1 = line.splitlines()
    line1 = line1[0].split(",")
    for i in range(3,8):
        line1[i] = line1[i].split(":")

    # sorting subject scores
    engScore = int(line1[3][1])
    mathsScore = int(line1[4][1])
    phyScore = int(line1[5][1])
    chemScore = int(line1[6][1])
    bioScore = int(line1[7][1])

    # appending to appropriate lists
    names.append(line1[0])
    eng.append(engScore)
    maths.append(mathsScore)
    phy.append(phyScore)
    chem.append(chemScore)
    bio.append(bioScore)

    # for calculating average
    summ = engScore + mathsScore + phyScore + chemScore + bioScore
    sums.append(summ)

# determining subject toppers
for i in range(0,len(names)):
    if eng[i] == max(eng):
        engToppersIndex.append(i)
    if maths[i] == max(maths):
        mathsToppersIndex.append(i)
    if phy[i] == max(phy):
        phyToppersIndex.append(i)
    if chem[i] == max(chem):
        chemToppersIndex.append(i)
    if bio[i] == max(bio):
        bioToppersIndex.append(i)

# printing subject toppers
toppersIndex = [engToppersIndex, mathsToppersIndex, phyToppersIndex, chemToppersIndex, bioToppersIndex]
messages = ["English toppers:", "Maths toppers:", "Physics toppers:", "Chemistry toppers: ", "Biology toppers:"]
for i in range(0,len(toppersIndex)):
    print(messages[i])
    for j in range(0,len(toppersIndex[i])):
        print(names[(toppersIndex[i])[j]] + " (" + str(max(subjects[i])) + "%)")
    print()

# determining Gold medalist
# determining average grade for each student
avg = []
for i in range(0,len(names)):
    avg.append(sums[i]/5)

highestOverallMark = max(avg)
goldMedalist = names[avg.index(highestOverallMark)]

print("Gold medalist: " + goldMedalist + " (" + str(highestOverallMark) + "%)")

f.close()