prison = []
lucky = []

# number of prisoners:
prisoners = 10

for i in range(0,prisoners):
    prison.append("O")


for i in range(1,prisoners,2):
    prison[i] = "C"

# print(prison)

for r in range(3,prisoners+1): # 3 -> 10
    for i in range(r-1,prisoners,r): # r-1 -> 9; r = 10, r-1 = 9
        if prison[i] == "C":
            prison[i] = "O"
        else:
            prison[i] = "C"
    # print(prison)


for i in range(0,prisoners):
    if prison[i] == "O":
        lucky.append(i+1)
print(lucky)