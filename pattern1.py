n= 10
for i in range(1, n):
    # print spaces
    for j in range(n-i):
        print(" ", end="")
    # print stars
    for k in range(i):
        print("*", end=" ")
    print() 