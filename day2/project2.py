print("Welcome to the tip Calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
result = (total * (tip / 100 + 1) / people)
print(f"Each person should pay: ${round(result, 2)}")