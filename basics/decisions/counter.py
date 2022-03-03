n1 = int(input("Please enter first number "))
n2 = int(input("Please enter second number "))
n3 = int(input("Please enter third number "))

even = 0
odd = 0

if n1 % 2 == 0:
  even += 1
else:
  odd += 1
if n2 % 2 == 0:
  even += 1
else:
  odd += 1
if n3 % 2 == 0:
  even += 1
else:
  odd += 1
print(f"There are {even} even numbers and {odd} odd numbers")