age = int(input("What is your age? "))
numberOfChild = int(input("How many children do you have? "))

if age > 25 and numberOfChild > 0:
  print("You are a young parent!")
  print(f"Next year you will be {age+1} years old!")
elif age > 55 and numberOfChild > 0:
  print("Your children will support you when you're old!")
  print(f"Next year you will be {age+1} years old!")
elif afe < 18 or numberOfChild == 0:
  print("There is still time for child")
else:
  print("You are not so young: ")
  print("We are going to live long anyways!")