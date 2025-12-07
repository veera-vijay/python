class dad():
    def phone(self):
        print("dad phone")

class mom():
    def sweet(self):
        print("eat sacks")
    
class son(dad,mom):
    def laptop(self):
        print("son laptop")
        
vijay=son()
vijay.laptop()
vijay.sweet()
vijay.phone()

