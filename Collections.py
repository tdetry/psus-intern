# Counter
from collections import Counter, namedtuple, defaultdict, deque

array = [1, 2, 3, 4, 5, 3, 4, 2, 1, 4, 6]
print("The original array: ", array)
count = Counter(array)
print("Count number of times each element occurs in the array: ", count)
print("The two most common element is: ", count.most_common(2), " the element that occurs the most is: ", count.most_common(1)[0][0])

# namedTuple: creates a custiomized class
Point = namedtuple('Point', 'x, y')
pt = Point(1, 2)
print("The Point object has values: ", pt)

# defaultDict
store = defaultdict(int)
store['a'] = 1
store['b'] = 2
print("Current state of the store: ", store)
print("Defaultdict lets us access a non-existent key instead of throwing an error, eg. store['c'] = ", store['c'])

# deque
dq = deque()
dq.append(9)
dq.append(8)
dq.append(7)
print("Initial deque")
dq.append(3)
print("Adding 3 at the back: ", dq)
dq.appendleft(2)
print("Adding 2 at the start: ", dq)
dq.popleft()
print("Removing the first element: ", dq)
dq.pop()
print("Removing the last element: ", dq)
dq.rotate(2)
print("Rotating elements to the right by 2 :", dq)
dq.clear()
print("Clearing the deque: ", dq)