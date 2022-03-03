h = input("Are you happy?")
k = input("Do you know it")
if h.lower() == "yes" and k.lower() == "yes":
  print("clap your hands!")
elif h.lower() == "yes" and k.lower() == "no":
  print("Show it")
else:
  print("Help is available")