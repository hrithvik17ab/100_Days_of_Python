bill = input("What is yout total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tip_amount = float(bill) * (float(tip) / 100)
total_amount = float(bill) + tip_amount

split_amount = total_amount / int(people)

print(f"Each person should pay: ${split_amount}")
