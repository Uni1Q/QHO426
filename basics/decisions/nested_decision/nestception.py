userResponse = input("where should I look?")

if userResponse.lower() == "in the bedroom":
  userResponse2 = input("Where in the bedroom should I look?")
  if userResponse2.lower() == "under the bed":
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery")
elif userResponse.lower() == "in the bathroom":
  userResponse2 = input("Where in the bathroom should I Look?")
  if userResponse2.lower() == "in the bathroom":
    print("found rubber ducky but no battery")
  else:
    print("Found wet surface but no battery")
elif userResponse.lower() == "in the lab":
  userResponse2 = input("Where in the lab should I Look?")
  if userResponse2.lower() == "on the table":
    print("Yes, I found my battery")
  else:
    print("Found some tools but no battery")
else:
  print("I do not know where that is but I will keep looking")