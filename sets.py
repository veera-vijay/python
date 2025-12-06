# set add

fruits ={"banana", "Orange", "Kiwi", "cherry"}
fruits.add("apple")
print(fruits)

#update
fruits = {"banana", "Orange", "Kiwi", "cherry"}
veg={"onion","tomato"}
fruits.update(veg)
print(fruits)

# set union
fruits = {"banana", "Orange", "Kiwi", "cherry"} 
veg={"onion","tomato","orange"}
set3=fruits.union(veg)
print(set3)

#set intesection

a={2,4,6,8}
b={4,5,9}
c=a.intersection(b)
print(c)