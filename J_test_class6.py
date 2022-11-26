class Parent:
    def __init__(self, eye_color):
        self.eye_color = eye_color
    def print_attributes(self):
        print("Your eye color is {}".format(self.eye_color))

class Child(Parent):
    def __init__(self, eye_color, hair_style):
        super().__init__(eye_color)
        self.hair_style = hair_style
    def print_attributes(self):
        super().print_attributes()
        print("Your style of hair is {}".format(self.hair_style))

c1 = Child("Green", "spike")
c1.print_attributes()