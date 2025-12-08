"""num_start=int(input("enter the starting number:"))
num_end=int(input("enter the ending number:"))

print(f"the prime {num_start} to {num_end} are:")

for numbers in range(num_start,num_end+1):
    if(numbers>1):
        for i in range(2,numbers):
            if(numbers%i==0):
               break
        else:
              print(numbers,end=" ")"""
              
              
              
              
starting= int(input("enter he startig num"))
ending=int(input("enter the ending num"))
count=0
sum=0
for num in range(starting,ending+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
             break
        else:
            count+=1
            sum+=num
            
            print(num)
print(count)
print(sum)