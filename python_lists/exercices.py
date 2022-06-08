"""
Extend nested list by adding the sublist
You have given a nested list. Write a program to extend it by
adding the sublist ["h", "i", "j"] in such a way that it will
look like the following list.
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
"""


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
list_index = []
def find_list_index(given_list):
    for i, element in enumerate(given_list):
        if isinstance(element,list):
            list_index.append(i)
            print("a",given_list[i])
            if element == ['f', 'g']:
                print(element + sub_list)
                return element + sub_list
            given_list[i] = find_list_index(element)
    return given_list
print(find_list_index(list1))
    