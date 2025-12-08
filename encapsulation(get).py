class Person:
    def __init__(self, age):
        self.__age = age   # private variable

    def get_age(self):     # getter
        return self.__age

p1 = Person(20)
print(p1.get_age())   # Output: 20
