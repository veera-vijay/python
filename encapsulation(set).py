class Person:
    def __init__(self, age):
        self.__age = age   # private variable

    def set_age(self, age):   # setter
        if age > 0:
            self.__age = age
    def get_age(self):
        return(self.__age)

p1 = Person(20)
p1.set_age(25)            # updating value
print(p1.get_age())       # Output: 25
