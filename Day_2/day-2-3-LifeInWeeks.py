# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
days = 365
weeks = 52
months = 12

age = int(age)
remaining_age = (90 - age)

days *= remaining_age
weeks *= remaining_age
months *= remaining_age

print(
    f"Warning you have {days} days, {weeks} weeks, and {months} months left.")
