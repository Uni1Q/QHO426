def box():
  l = len(word)
  print("#"*(l+4))
  print("#"+word+"#")
  print("#"*(l+4))

def low(word):
  print(word.lower())

def up(word):
  print(word.upper())

def reverse(word):
  print(word, "|", word[::-1])

def repeat(word):
  n = int(input("Number of times to repeat"))
  for times in range(n):
    if times % 2 == 0:
      up(word)
    else:
      low(word)

def run():
  w = input("Enter a word")
  opt = int(input("Choose an option: 1 - box\n2-lower\n3-upper\n4-mirror\n5-repetition"))
  if opt == 1:
    
    