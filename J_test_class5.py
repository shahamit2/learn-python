class Parent:
    def __init__(self, eye_color):
        self.eye_color = eye_color
    def print_attributes(self):
        print("Your eye color is {}".format(self.eye_color))

class Child(Parent):
    pass

c1 = Child("Green")
c1.print_attributes()