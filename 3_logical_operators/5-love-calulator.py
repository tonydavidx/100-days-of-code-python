print("welcome to love calculator")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

name1_count = 0

name1_count += name1.count("t")
name1_count += name1.count("r")
name1_count += name1.count("u")
name1_count += name1.count("e")

name2_count = 0

name2_count += name2.count("l")
name2_count += name2.count("o")
name2_count += name2.count("v")
name2_count += name2.count("e")

love_score = int(str(name1_count)+str(name2_count))

if love_score < 10 or love_score > 90:
    print(f"your scroe is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
    print(f"your love score {love_score}, You are okay")
else:
    print(f"Your love score is {love_score}")
