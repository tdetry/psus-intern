Enter Python code here and hit the Run button.

for i in range(1,6):
    for j in range(6-i,0,-1):
        print(i, end=' ')
    print()
   
def outer(x,y):
    def inner():
        return x + y
    return inner() + 'Developer'
   
result = outer('Emma', 'Kelly')
print(result)

str = 'My Name is Jessa'
rev_list = [x[::-1] for x in str.split()]
print(" ".join(rev_list))

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
s = set()
dups = set()
for e in sample_list:
    if (e in s):
        dups.add(e)
    else:
        s.add(e)
print(dups)

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict = {}
for e in sample_list:
    if e not in dict:
        dict[e] = 1
    else:
        dict[e] += 1
print(dict)

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
list = [x for x in roll_number if x in sample_dict.values()]
print(list)

str1 = "Apple"
dict = {}
for ch in str1:
    dict[ch] = str1.count(ch)
print(dict)
