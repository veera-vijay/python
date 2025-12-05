a=["car","bike","flower"]
print(a)
# use append to store the new value

a=["car","bike","flower"]
a.append("rose")
a[0]="rose"
print(a)

#pop delete the last index and delete particular index also
a=["car","bike","bus","fruits"]
a.pop()
a.pop(1)
print(a)

# remove the particualr
a = ["apple", "banana", "cherry", "banana", "kiwi"]
a.remove("banana")
print(a)

#clear 

a=["apple", "banana", "cherry", "banana", "kiwi"]
a.clear()
print(a)

#extended
a=["apple", "banana", "cherry", "banana", "kiwi"]
b=["roman","cena"]
a.extend(b)
print(b)

#sort the list
a=[2,4,6,8]
a.sort()
print(a)

#sort decending orderer
a=[3,5,2,5,2]
a.sort(reverse=True)
print(a)

#SORT lower 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#insert the list
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.insert(2,"grapes")
print(fruits)