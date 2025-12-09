class father():
    def __init__(self,father_name):
        self.father_name=father_name
class mom():
     def __init__(self,father_name,mom_name):
         super().__init__(father_name)
         
         self.mom_name=mom_name
 
class son(father,mom):
    def __init__(self, father_name,mom_name,son_name):
        super().__init__(father_name)
        self.mom_name=mom_name
        self.son_name=son_name
    def fun(self):
        print(self.father_name,self.mom_name,self.son_name)
s1=son("bala","jaya","vijay")
s1.fun()