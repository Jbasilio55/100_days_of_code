print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
total = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        total += 5
        print("Please pay $5.")
    elif age < 18:
        total += 7
        print("Please pay $7.")
    else:
        total += 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo? Y(yes) or N(no)").lower

    if wants_photo == "yes" or wants_photo == "y":
        total += 3
    print(f"your total is ${total}")
    
else:
    print("Can't ride the rollercoaster.")