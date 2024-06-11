# The Tip Calculator

print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $")

tip = input("How much tip would you like to give? 10, 12, or 15? ")

number_people = input("How many people to split the bill? ")

price_per_person = (int(total_bill) + int(tip)) / int(number_people)

print(f"Each person should pay: ${price_per_person}")

