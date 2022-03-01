name = input("Enter your name: ")

#len() - funtion that returns the length of string*

if len(name) > 9:
  print("Your name is too long, what else are you called by?")
else:
  print("Oh your name is pretty short!")

print("Nice to meet you anyway, {}".format(name))
