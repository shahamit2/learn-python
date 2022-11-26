# Note
# Except class everything is object.

# Basic instance type
num = 5
name = "Five"
flag = True
print(id(num))
print(id(name))
print(id(flag))


# Function object
def greet(msg):
    print("Hello, {}!!!".format(msg))

print("id(greet): {}".format(id(greet)))
print("type(greet): {}".format(type(greet)))
print("greet.__class__: {}".format(greet.__class__))
print("greet.__class__.__mro__: {}".format(greet.__class__.__mro__))
# mro : method resolution order.


# Class
class parent:
      pass

class child(parent):
      pass

print("child.mro(): {}".format(child.mro()))
c = child()
print(c.__class__.__mro__)
