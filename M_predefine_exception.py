# Example 1
print("First try-except block.")
try:
  x = open("abc.txt")
except FileNotFoundError as fnfe:
  print("*** Error!!!")
  print(fnfe)
else:
  print("** Success **")
finally:
  print("File block execution is completed..")

print("--------")
print(" ")

# Example 2
print("Second try-except block.")
try:
  x = open("M_predefine_exception.py")
except FileNotFoundError as fnfe:
  print("*** Error!!!")
  print(fnfe)
else:
  print("** Success **")
finally:
  print("File block execution is completed..")