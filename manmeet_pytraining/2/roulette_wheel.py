pocket_number = int(input("Enter a packet no(0-36)"))
if(pocket_number<0 or pocket_number>36):
    print("enter a no in range of 0-36")
elif pocket_number == 0:
    print('Green')
elif pocket_number >= 1 and pocket_number <= 10:
    if pocket_number % 2 != 0:
        print('Red')
    else:
        print('Black')
elif pocket_number >= 11 and pocket_number <= 18:
    if pocket_number % 2 != 0:
        print('Black')
    else:
        print('Red')
elif pocket_number >= 19 and pocket_number <= 28:
    if pocket_number % 2 != 0:
        print('Red')
    else:
        print('Black')
elif pocket_number >= 29 and pocket_number <= 36:
    if pocket_number % 2 != 0:
        print('Black')
    else:
        print('Red')
