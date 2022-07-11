prison = []
luckyPrisoners = []

# number of prisoners:
prisoners = 100

for i in range(0,prisoners):
    prison.append("O")

# print(prison)

for i in range(1,prisoners,2):
    prison[i] = "C"

# print(prison)

for r in range(3,prisoners+1):
    for i in range(r-1,prisoners,r):
        if prison[i] == "C":
            prison[i] = "O"
        else:
            prison[i] = "C"
    # print(prison)

for i in range(0,prisoners):
    if prison[i] == "O":
        luckyPrisoners.append(i+1)
print(luckyPrisoners)