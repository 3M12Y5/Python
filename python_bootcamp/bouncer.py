age = input("What is your age?\n")

if age!="":
    if int(age)>=21:
        print("You can enter")
    elif int(age)>=18 and int(age)<21:
        print("You need to wear this band")
    else:
        print("You cannot enter")
else:
    print("You did not enter your age")