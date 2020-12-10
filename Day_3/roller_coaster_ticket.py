height = int(input("what is your height "))

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("what is your age? "))
    if age < 12:
        print("Ticket Price $5")
    elif age <= 18:
        print("Ticket price $7")
    else:
        print("Ticker price $12")

else:
    print("Sorry! you have to be taller to ride the roller coaster")
