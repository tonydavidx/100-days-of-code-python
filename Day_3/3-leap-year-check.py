print("welcome Leap year Checker")
year = int(input("Enter a year you want to check\n"))


if (year / 4).is_integer():
    if(year/100).is_integer():
        if(year / 400).is_integer():
            print('Leap Year')
        else:
            print("Not Leap year")
    else:
        print('Leap Year')
else:
    print('Not Leap Year')
