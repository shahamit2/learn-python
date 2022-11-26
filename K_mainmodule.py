def demo():
   print(" ")
   print("*****************************************")
   print("Demo of how module works -> ")
   print("** Observe the name of module **")
   print("Module name is {}.".format(__name__))
   print("*****************************************")
   print(" ")

if __name__ == "__main__":
   demo()

# Execute in two ways.
# Way 1) on $ prompt
# $ python K_mainmodule.py

# Way 2) on python prompt
# >>> import K_mainmodule as kmm
# >>> kmm.demo()

# In both notice output for print(__name__) to see module name.
