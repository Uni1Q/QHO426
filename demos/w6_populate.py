def populate(path):
  with open(path, "w") as f:
    while True:
      sauce = input("Enter a sauce (or stop): ")
      if sauce.lower() == "stop":
        break
      else:
        f.write(sauce + "\n")

def read_sauce(path):
  with open(path, "r")as f:
    print(f.readlines())
    
read_sauce("s1.txt")