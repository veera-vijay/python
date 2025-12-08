number=[1,4,5,3,8]

largest_number=max(number)
number.remove(largest_number)
second_largest=max(number)
number.remove(second_largest)
third_largest=max(number)
print(largest_number)
print(second_largest)
print(third_largest)


numbers=[2,55,63,56,65,121]

largest_number=numbers[0]

for num in numbers:
    if num>largest_number:
        largest_number=num
        
print(largest_number)


a=23
b=43
largest_number=max(a,b)
print(largest_number)