num=int(input("enter the number"))
if(num>1):
    for i in range(2,num+1):
        if num%i==0:
            print("it is not prime")
            break
        else:
          print("it is a prime",num)
          break  
      