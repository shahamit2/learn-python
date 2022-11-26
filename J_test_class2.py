import sys
class Languages:
   def __init__(self, lang):
       print("Executing Constructor!!")
       self.lang = lang

# Instance variable
l1 = Languages("Go")
l2 = Languages("Python")

# Accessing attributes
print(l1.lang)
print(l2.lang)

# Assigning references
l3 = l1
l4 = l1

# Number of references to objects
print("No of references to object 'l1' :: {}".format(str(sys.getrefcount(l1)-1)))