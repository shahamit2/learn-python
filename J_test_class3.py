class Languages:
   # Class variable
   counter = 1
   def __init__(self,lang):
       print("Constructor {}".format(str(Languages.counter)))
       self.lang = lang
       Languages.counter = Languages.counter + 1

l1 = Languages("Go")
l2 = Languages("Python")

# Access class variable.
print(Languages.counter)