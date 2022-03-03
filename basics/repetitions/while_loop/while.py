phrase = input("please enter a phrase: ")
i = 0
while i < len(phrase):
  print("Bop", end = " ")
  i += 1

for i in phrase: #exact same as range(len(phrase))
  print("Beep", end = " ")