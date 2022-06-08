from itertools import groupby
from tokenize import group
persons = [{'name':'a','age':22}, {'name':'b','age':22}, {'name':'c','age':22}, {'name':'d','age':24}]
group_obj = groupby(persons, key = lambda x: x['age'])
# print(group_obj)
for key, value in group_obj:
    # print(key,list(value))
    print(key, list(value))