class dad():
   
    def phone(self):
        
        print("dad phone",self.phn)

class mom(dad):
    def sweet(self):
        print("eat snacks")
    
class son(mom):
    def laptop(self):
        print("son laptop")
        
vijay=son()
vijay.laptop()
vijay.sweet()
vijay.phone()
vij=mom()
vij.phone()
d=dad()
d.phn="samsung"
d.phone()

"""class animal():
    def __init__(self,name):
        self.name=name
        
class birds(animal):
    def __init__(self,name,birdname):
        super().__init__(name)
        self.birdname=birdname
    
    def fun(self):
        print(self.name,self.birdname)

class cow(birds):
    
    def __init__(self, name,birdname,kick):
       super().__init__(name,birdname)
       
       self.kick=kick
        
    def call(self):
        print(self.name,self.birdname,self.kick)
        
        
           
        
b1=birds("dog","hen")
b1.fun()
c1=cow("buffalo","c","c")
c1.call()


        
    
    """