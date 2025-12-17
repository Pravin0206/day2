#Tip Calculator

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tipval = float(input("How much tip would you like to give? 10,12 or 15?"))
tip = bill * (tipval /100)
split = int(input("How much people to split the bill?"))

contribution = ((bill + tip) / split)
finalbill = round(contribution, 2)
print(f"Each person should pay: ${finalbill}")