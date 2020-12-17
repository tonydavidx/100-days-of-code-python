# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

if size == "s":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
    if extra_cheese == "y":
        bill += 1

if size == "m":
    bill = 20
    if add_pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1

if size == "l":
    bill = 25
    if add_pepperoni == "y":
        bill += 3
    if extra_cheese == "y":
        bill += 1

print(f"Your final bill is: {bill}")
