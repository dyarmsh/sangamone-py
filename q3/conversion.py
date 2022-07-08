
def convert():
    contents = str(input("Enter in format 'x unit = y unit' WITHOUT QUOTES: "))
    contents = contents.split(" ")
    print(contents)
    LHS = int(contents[0])
    RHS = int(contents[3])

    flip_LHS = str(RHS/RHS)
    flip_RHS = str(LHS/RHS)
    convert_flip = flip_LHS + " " + contents[4] + " " + contents[2] + " " + flip_RHS + " " + contents[1]

    print(convert_flip)
convert()