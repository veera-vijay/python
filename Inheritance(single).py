"""class dad():
    def phone(self):
        print("dad phone")
    
class son(dad):
    def laptop(self):
        print("son laptop")
        
vijay=son()
vijay.laptop()
vijay.phone()
"""

class father():
    def __init__(self,name):
        self.name=name
class mom():
     def __init__(self,age):
         self.age=age
         
    
class son(father,mom):
   
        
      
    def cash(self):
       print(self.name,self.age)
        
s1=son("vijay",23)
s1.cash()
    
    
    

    