import sys

print(" ")
print("-> Type of sys.argv : {}".format(type(sys.argv)))
print(" ")

for s1 in sys.argv:
    print(type(s1), end=" | ")
print(" ")
for s1 in sys.argv:
    print(s1, end=" | ")
print(" ")

# Try running below and see output.
# python F_arg.py Eckhart 49 True None