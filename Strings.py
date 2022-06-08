# Initialize a string
s = "abcdefghijklm"
print("Original string: ", s)

# Slicing
print("Sliced string: ", s[5:])

# Reversed
print("Reversed string: ", s[::-1])

# Concatination
print("Concatinate strings: " + "this is concatinated")

# Access each character in the string
print("Accessing each char in the stirng")
print(letter for letter in s)

# Check if a substring exists in string
print("Checking if mno is present in our string: ", True if "mno" in s else False)

# Check if a char is present in a string:
print("Check if a is a vowel: ", True if "a" in "aeiou" else False)

# Removing all the extra spaces
a = "         f f f         "
x = a.strip()
print("Removing extra whitespaces from          f f f         : ", x)

# Getting all the words from a sentence:
sentence = "I want to get all the words from this sentence"
words = [word for word in sentence.split()]
# f"These are the words from " + {sentence} + " all of them separated: " + {words}
print("These are the words from " + sentence + " all of them separated: ", words)

# Capitalise, upper, lower, startswith, endswith
print("Capitalize heLLO: ", "heLLO".capitalize())
print("Upper case heLLO", "heLLO".upper())
print("Lower case heLLO", "heLLO".lower())
print("Check if heLLO starts with A", "heLLO: ".startswith("A"))
print("Check if heLLO ends with A", "heLLO: ".endswith("A"))

# Replace a substring
print("Replacing World in Hello World with Heaven: ", "Hello World".replace("World", "Heaven"))

# Join words to form a single string
words = ["Hey", "lets", "join", "ourselves", "together"]
print("Joining all the words from ", words, " to form a new string :", " ".join(words))

# f-strings
print("Fstrings: ", f"trying this out for fun {22} as it doesnt matter {True}")