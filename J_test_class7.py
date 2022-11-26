class IndianCuisine:
    def __repr__(self):
        return "Welcome to Indian Cuisine!!"
    @classmethod
    def Menu(cls):
        c = cls()
        print(c)


class Sweets(IndianCuisine):
   def __repr__(self):
       return "Check sweet options!!"
   @staticmethod
   def price():
       print("All sweets are 200rs per kg")


# Class method: -
# It is having class as first argument.
# It is bound to class.
i = IndianCuisine()
i.Menu()
s = Sweets()
s.Menu()

# Static method: -
# Know nothing about a class.
# It is an indication that class access not required.
# It's a way of putting function into a class.
s.Price()
