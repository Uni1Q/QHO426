import random
def guess_the_number: 
  min_value = int(input("please enter minimum value: "))
  max_value = int(input("Please enter the maximum value: "))
  
  x = random.randrange(min_value, max_value)
  
  print(f"I am thinking of a number between {min_value} and {max_value}, can you guess what it is")
  
  while True:
    guess = int(input("Have a guess: "))
    if guess < x:
      print("your guess is too low")
      print("Try again")
    elif guess > x:
      print("Your guess is too high")
      print("Try again")
    elif guess == x:
      break
    else:
      print("your guess is invalid")

print("You guessed my number!")