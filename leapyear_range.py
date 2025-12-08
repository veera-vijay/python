starting_year=int(input("enter the starting year:"))
ending_year=int(input("enter the ending year:"))

for num in range(starting_year,ending_year+1):
    if(num % 4==0 and num % 100 !=0) or (num % 400==0):
        print(num,end=" ")
    