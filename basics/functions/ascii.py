print("Program started")
x = abs(int(input("Please enter an ASCII code: ")))
if x in range(32, 127):
  print(f"The charcter represented by the ASCII code {x} is {chr(x)}")
else:
  print("Oh no, cannot convert")
print("Program ended")