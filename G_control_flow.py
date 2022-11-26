# if, elif, else
age = int(input("Enter your age: "))

if age < 6:
   print("You are in preschool..")
elif age >= 6 and age <= 18:
   print("You are in school..")
elif age >= 18 and age <= 21:
   print("You are in college..")
else:
   print("Life over!!")

# while
i = 1
while i <= 5:
   print(i)
   i = i + 1

# For loop
# List example is given.. Similarly other class type will work.
l1 = ["go", "r", "python"]
for l in l1:
    print(l)