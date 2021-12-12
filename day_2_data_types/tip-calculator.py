print("welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give 10, 12 or 15? "))
persons = int(input("How many persons to split the bill? "))

tip = tip / 100

tip = tip * bill

bill_with_tip = tip + bill

result = bill_with_tip / persons
result = round(result, 2)

print(f"Each person should Pay: ${result}")
