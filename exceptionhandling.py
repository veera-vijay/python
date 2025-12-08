

try:
   a=int(input("enter value a:"))
   b=int(input("enter value b:"))
   print(a+b)
   
except Exception as e:
                 print("something",e)
finally:
   print("done")
   
    