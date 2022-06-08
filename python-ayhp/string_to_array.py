'''
Write a function to split a string and convert it into an array of words.
Examples (Input ==> Output):

Inpu: "Robin Singh" 
Output: ["Robin", "Singh"]

Input "I love arrays they are my favorite" 
Output: ["I", "love", "arrays", "they", "are", "my", "favorite"]
'''

def string_to_array(str):
    return [""] if len(str) == 0 else str.split()
    

print(string_to_array("Robin Singh"))# Expected: ["Robin", "Singh"]
print(string_to_array("I love arrays they are my favorite")) # Expected: ["I", "love", "arrays", "they", "are", "my", "favorite"])
print(string_to_array("1 2 3")) # Expected: ["1", "2", "3"]
print(string_to_array("")) # Expected: [""]