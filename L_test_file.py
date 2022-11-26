def read_file(instance, mode):
    print("-----------")
    print("Instance : {} :: Mode : {}".format(instance, mode))
    f = open("quotes.txt", "r")
    data = f.read()
    print(data)
    f.close()
    print("-----------")
    print(" ")

def write_file(quote, mode):
    f = open("quotes.txt", mode)
    quote = quote + "\n"
    f.write(quote)
    f.close()

# Write mode 1
quote = "Anything you accept fully will take you into peace."
write_file(quote, "w")
read_file(1, "write")

# Write mode 2
quote = "Worry pretends to be necessary but serves no useful purpose."
write_file(quote, "w")
read_file(2, "write")

# Write+ mode 1
quote = "Give up defining yourself."
write_file(quote, "w+")
read_file(3, "write+")

# Write+ mode 2
quote = "All problems are illusions of mind."
write_file(quote, "w+")
read_file(4, "write+")

# Append mode 1
quote = "Life isn’t as serious as the mind makes it out to be."
write_file(quote, "a")
read_file(5, "append")

# Append mode 2
quote = "Whatever you fight, you strengthen, and what you resist, persists."
write_file(quote, "a")
read_file(6, "append")

# Append+ mode 1
quote = "Anything that you resent and strongly react to in another is also in you."
write_file(quote, "a+")
read_file(7, "append+")

# Append+ mode 2
quote = "The primary cause of unhappiness is never the situation but your thoughts about it."
write_file(quote, "a+")
read_file(8, "append+")

# Read+ mode 1
quote = "Learn to disidentify from your mind."
write_file(quote, "r+")
read_file(9, "read+")

# Read+ mode 2
quote = "It is not uncommon for people to spend their whole life waiting to start living."
write_file(quote, "r+")
read_file(10, "read+")


# Read file line by line
f = open("L_test_file.py", "r")
# type(f)
# o.p: <class '_io.TextIOWrapper'>
# (__iter__ and __next__ are implemented in _io.TextIOWrapper.)
for f1 in f:
    print(f1, end = "")