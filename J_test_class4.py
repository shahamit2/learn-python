class Greet:
   def __init__(self):
       self.message = "Welcome!"
   def _morning(self):
       self.message = "Good Morning"
       print(self.message)
   def __afternoon(self):
       self.message = "Good Afternoon"
       print(self.message)
   def __add__(self, a):
       return 5 + a
   def __repr__(self):
        quote = "Whatever you accept completely will take you to peace."
        return "Quote: " + quote

g1 = Greet()

# Representation string
print(g1)

# Convention for Protected:: "Single dash"
g1._morning()

# Prevent accidental access: It has real meaning.
# Still can be accessed using Class name.
g1._Greet__afternoon()

# -> Convention: Way to avoid conflict with user defined function/attribute name.
# -> Python adds some real functionality for it. __add__ allows to use plus sign with
#    instance variable. (Magic mathod)
print(g1.__add__(3))
# Some inbuilt method that python suppose to call and not us.
print(g1 + 3)

# Print members
print(Greet.__dict__)

##
# for k,v in Greet.__dict__.items():
#    print(k, " : ", v)