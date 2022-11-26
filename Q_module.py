# For testing create below directory
# present working directory: /Users/amitshah
# mkdir -p org/ashah/personal
# Create file welcome.py with function greet
# File: org/ashah/personal/welcome.py
# Add below function greet to welcome.py
def greet():
    print("Hello, World!!!")

# To test module
# present working directory: /Users/amitshah
# Go to python prompt
# python
# >>> import org.ashah.personal.welcome as w
# >>> w.greet()
# >>> from org.ashah.personal import welcome
# >>> welcome.greet()
# >>> from org.ashah.personal.welcome import greet
# >>> greet()