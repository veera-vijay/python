start=int(input("enter the starting number:"))
end=int(input("enter the ending number:"))

for num in range(start,end+1):
    if str(num)==str(num)[::-1]:
        print(num,end="  ")