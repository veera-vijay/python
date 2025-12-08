import array

numbers=array.array("i",[1,2,3,4,5])

print(numbers)
print(type(numbers))

#add
numbers.append(99)
print(numbers)
#remove
numbers.remove(1)
print(numbers)
#inseet
numbers.insert(3,66)
print(numbers)

