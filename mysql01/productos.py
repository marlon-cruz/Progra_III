myArray = [2,1,3,1,4,2,1,1,2,4]

for i in range(1,6):
    print(i, ": ",end="")
    for j in range(10):
        if myArray[j] == i:
            print("*",end="")
    print("\n")
