#Data Structures

l = [1,2,3]
l.append(4)
l.pop(2)
print(l.copy())

tup = (*l,)
print(tup)

try:
    tup[0] = 100 
except Exception as e:
    print("Exception because tuple is immutable")

s = set(tup)
print(s)
s2 = {2,3,4,5}

print("union:",s|s2)
print("intersection:",s&s2)
print("difference", s-s2)
print("exor",s^s2)

dct = {x: x**2 for x in range(1,10)}  
print(dct)
print(dct[2])
print(11 in dct)