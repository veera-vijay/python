num=int(input("enter the number"))
 
temp=num
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if(temp==reverse):
    print("it ia a palindrome")
else:
    print("it is a not palindrome")