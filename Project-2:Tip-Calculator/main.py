# The Tip Calculator

print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
tip_in_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip = bill * (tip_in_percent/100)
total_bill = bill + tip
final_bill_per_person = round(total_bill / number_of_people, 2)

print(f"Each person should pay: ${final_bill_per_person}")

