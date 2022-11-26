# Explain how address cannot be retained
# - Inside function
# - Without function.. Just with simple increment..

# Without function.. Just with simple increment..
num = 556
print("-> BEFORE :: Address of Variable 'num': {}".format(id(num)))
num = num + 1
print("-> AFTER :: Address of Variable 'num': {}".format(id(num)))

# Inside function
def sum(num):
    print("Before(sum) :: Address of Variable 'num': {}".format(id(num)))
    num = num + 1
    print("After(sum) :: Address of Variable 'num': {}".format(id(num)))

n = 555
print("Address of Variable 'n': {}".format(id(n)))
sum(n) # Passing reference from n to num

# Ask WHY?
# It is because everything is OBJECT.


# Way to copy reference
x = 512
y = x

# Note: When you manipulate values of basic class object then it will be assigned to new objects.