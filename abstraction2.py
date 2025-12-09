from abc import ABC ,abstractmethod

class one(ABC):
    def __init__(self,first_name):
        self.first_name=first_name
    @abstractmethod
    def fun(self):
        pass
class two(one):
    def __init__(self, first_name,second_name):
        super().__init__(first_name)
        self.second_name=second_name
        
    def fun(self):
        print("the 1 name is",self.first_name,"the 2 name is",self.second_name)
        
class three(one):
    def __init__(self, first_name,thirdname):
        super().__init__(first_name)
        self.thirdname=thirdname
    def f(self):
        print("first name is :",self.first_name,"third name is :",self.thirdname)
t=two("vijay","veera")
th=three("vijay","vijay")
t.fun()
th.fun()