class car1():
    def __init__(self,car1_name):
        self.car1_name=car1_name
    
    def fun(self):
        print("f{self.car1_name} this a car1 name")
class car2(car1):
    def __init__(self, car1_name,car2_name):
        super().__init__(car1_name)
        self.car2_name=car2_name
    def fun(self):
        print(f"{self.car1_name} :this is a car1 name  AND {self.car2_name} :this car 2 name")
class car3(car1):
    def __init__(self, car1_name,car3_name):
        super().__init__(car1_name)
        self.car3_name=car3_name
    def fun(self):
        print(f"{self.car1_name}:this is car name 1 AND {self.car3_name}: this is a car3_name")
c2=car2("kiya","scorpio")
c3=car3("venue","balleno")
c2.fun()
c3.fun()
