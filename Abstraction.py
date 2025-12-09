from abc import ABC,abstractmethod
class bike(ABC):
    def __init__(self,bikename):
        self.bikename=bikename
    @abstractmethod
    def  bikee(self):
        pass
class Car(bike):
    def __init__(self, bikename,carname):
        super().__init__(bikename)
        self.carname=carname
    def bikee(self):
        print("This is a car.")
    def cname(self):
        print("bikename is =",self.bikename,"car name is:--",self.carname)
class bus(bike):
    def __init__(self, bikename,busname):
        super().__init__(bikename)     
        self.busname=busname
    def bikee(self):
        print("This is a bus.")
    def bname(self):
        print("it is name of bike:---",self.bikename,"it  is a name of bus:----",self.busname) 
c=Car("hero","kiya")
b=bus("r15","neyveli")
b.bname()
c.cname()

