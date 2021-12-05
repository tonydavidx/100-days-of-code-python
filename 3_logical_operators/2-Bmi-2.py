# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = int(weight) / (float(height) ** 2)

bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} you are under weight")
elif bmi < 25:
    print(f"Your BMI is {bmi} you are Normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} you are over weight")
elif bmi < 35:
    print(f"Your BMI is {bmi} you are obese")
else:
    print(f"Your BMI is {bmi} you are clinically obese")
