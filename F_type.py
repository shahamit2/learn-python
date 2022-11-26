################################################################
i = int()
f = float()
c = complex()
s = str()
b = bytes()
ba = bytearray()
bl = bool()
l = list()
t = tuple()
s = set()
fs = frozenset()
d = dict()
n = None

class c1:
    pass

print(type(int))
print(type(c1))
################################################################
# Generate Sequence
r = range(10,30,3)
print(type(r))
for r1 in r:
    print(r1)


################################################################
# short notation (Infer)
i = 1
f = 1.1
c = 3 + 2j
s = 'abc'
b = b'abc'
bl = True
l = []
t = 1, # ..OR..  t = i,f, ..OR.. t = (1,3,5,)
s = {1,2,2} # OR Compulsory set()
d = {}


################################################################
# String
# '', "", """ """
# split to list -> <str>.split()
# - e.g.: "am,is,are".split(",")
# join list elements with separator and return string -> ''.join(<list>)
# - e.g.: ",".join(["am","is","are"])
s = "123abcd45egh"
s[1:8:2]
s.upper()
s.lower()
s.swapcase()
s.capitalize()
s.isalnum()
s.isalpha()
s.isdigit()
s.islower()
s.isupper()
s.istitle()
s.isspace()

name = "Eckhart"
surname = "Tolle"
age = 49
print("Most humble man on planet is {} {}, his age is {}".format(name, surname, age))
print("Most humble man on planet is {0} {2}, his age is {1}".format(name, age, surname))
print("Most humble man on planet is {n} {s}, his age is {a}".format(s=surname, n=name, a=age))
print("Most humble man on planet is {} {:>7}, his age is {:03d}".format(name, surname, age))
print("Most humble man on planet is {} {:<7}, his age is {:03d}".format(name, surname, age))

fullname = name + "," +  surname
fullname.split(",") # Returns list.
name * 2
length_of_name = len(name)
name in fullname
name == "Eckhart"
name != "Tolle"
fullname.split()

name = "  Eckhart  "
name.lstrip()
name.rstrip()
name.strip()

name = "Baba"
name.startswith("Ba")
name.endswith("ba")
name.find("a")
name.index("a")
name.rfind("a")
name.rindex("a")
name.count("a")
name.replace("a","i")

books = ['power-of-now','new-earth']
' ::: '.join(books)


#--------------
# List (Mutable)
l = [101,'list']
print(l[0])
l[1] = 'string'
l[2] = 'tuple' # Throws error
l.append('dict')
l.insert(1,'bytes') # Positional insert.
# Discuss slicing.
l2 = ['float','int']
l.extend(l2)
l.remove('list')
l.pop() # Removes last element.
l = [1,3,9,5]
l.reverse()
l.sort()
l.clear()

country1 = ['japan', 'china', 'hongkong']
country2 = ['usa', 'israel']

asia_country = country1 # copies reference
asia_country = country1[:] # copies value

# Math with list
list1 = [1,2,3]
list2 = [3,4,5]
list3 = list1 + list2
list4 = list1 * 10
list1 == list2
10 in list1 # IN operator.

# List comprehension.
squares = []
squares = [a*a for a in range(1,10)]
squares = [a*a for a in range(1,10) if a > 5]

#--------------
# Tuple
# Hello brother to LIST
# Immutable
t = (101,102,103,104,'abc')

# Tupple comprehension not supported.
# It will generate "GENERATOR" object.
squares = ()
squares = (a*a for a in range(1,10))
squares = (a*a for a in range(1,10) if a > 5)
next(squares)
for s1 in squares:
    print(s1)


#--------------
# Set (Duplicate not allowed, order not preserved.)
s = {'list', 101, 'string', 'tuple', 102}
s.add('dict')
s.remove(101) # If item not present it will throw error
s.discard(101) # It will not throw any error if item not present.
s.update({104,105})
snew = s.copy()
s.pop() # Will remove any item randomly
s.clear()

# Set comprehension
squares = {a*a for a in range(1,10)}

# Mathematical operations.
s1 = {1,2,3,4}
s2 = {3,4,5,6}
# union
print(s1 | s2)
s1.union(s2)
# intersection
print(s1 & s2)
s1.intersection(s2)
# Difference
print(s1 - s2)
s1.difference(s2)
# Symmetric difference
print(s1^s2)
s1.symmetric_difference(s2)

#--------------
# Fronzenset
# Hello brother to SET
# Immutable
s = {'list', 101, 'string', 'tuple', 102}
fs = frozenset(s)

#--------------
# dict
d = {101: "Python", 102: "Go", 103: "R" }
d[104] = "Java"
d[104] = "Ruby"

d.keys()
d.values()
d.items()
d.pop(102)
d.popitem() # Any random value will be removed
del d[101]
d.clear()

dl = {"Python": 101, "Go": 102, "R": "ABCD"}

for key,val in dl.items():
    print("{} : {}".format(key,val))

# Dictionary comprehension
squares = {a:a*a for a in range(1,10)}

#--------------
# None
def add(a,b):
    print("Sum of a + b = {}".format(a+b))

total = add(2,3)
print(total)

################################################################
# Special case of bytes
s1 = 'abc'
b1 = b'abc'

print(s1[0])
print(b1[0])

print(type(s1))
print(type(b1))

# b1 = bytes(s1) This will give error.
b1 = bytes(s1, encoding='utf-8')
print(b1)
ss1 = str(b1, encoding='utf-8')
print(ss1)


s2 = '漢'
b2 = bytes(s2, encoding='utf-8')
print(b2)
ss2 = str(b2, encoding='latin-1') # This will return incorrect string.
ss3 = str(b2, encoding='utf-8')

################################################################
# Passing desire type in input.
l = eval(input("Please provide list of countries: "))
t = eval(input("Please provide tuple of countries: "))

# -> See what value is stored without eval
l = input("Please provide list of countries: ")

