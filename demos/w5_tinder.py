def interests():
  print("Enter your interests, one after the other \"stop\" when you are done")
  s1 = set()
  while True:
    interest = input()
    if interest.lower == "stop":
      break
    else:
      s1.add(interest)
  return s1

def tinder2():
  print("First Person: ")
  p1 = interests()
  print("First Person: ")
  p2 = interests()
  common = p1.intersection(p2)
  if len(common) >= 3:
    print(f"You have {len(common)} interesets in common")
  else:
    print(f"Best of luck next life, you only have {len(common)} interest in common")

tinder2()