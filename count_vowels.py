letters="helloo"
vowels="a,e,i,o,u,A,E,I,O,U"
count=0
for char in letters:
    for v in vowels:
        if char==v:
            count=count+1
print("total count is:",count)