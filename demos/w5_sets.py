s = set()
s1 = {}
print(type(s))

colors = {"Blue", "Purple", "Cyan", "Orange", "Green"}

print(colors)
#
colors.add("Magenta")
colors.add("Turquoise")
print(colors)
#Remove items from set
colors.remove("Yellow")
print(colors)
#uniqueness of items within a set
colors.add("Red")
colors.add("Purple")
#check membership
if "blue" in colors:
  print("Cool")
else:
  print("Where blu")