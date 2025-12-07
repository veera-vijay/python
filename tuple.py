fruits = ("banana", "Orange", "Kiwi", "cherry")
print(type(fruits))

#lenth of tuple
fruits = ["banana", "Orange", "Kiwi", "cherry"]
print(len(fruits))

# change the tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#remove the tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

