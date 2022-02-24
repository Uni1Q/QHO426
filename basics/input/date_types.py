print("What is your name human")
userName = input()
print("How old are you?")
userAge = int(input())
print("How tall are you?")
userHeight = float(input())
print("How much do you weight?")
userWeight = float(input())

bmi = userWeight/(userHeight**2)

print(f"{userName}, you are {userAge} years old and your BMI is {bmi:2f}")