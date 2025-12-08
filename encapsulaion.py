class Student:
    def __init__(self, name, age):
        self.__age = age  # private
        self.name = name

    def get_age(self):      # getter
        return self.__age

    def set_age(self, age): # setter
        if age > 0:
            self.__age = age

s1 = Student("Arun", 21)
print(s1.get_age())   # 21

s1.set_age(25)
print(s1.get_age())   # 25
