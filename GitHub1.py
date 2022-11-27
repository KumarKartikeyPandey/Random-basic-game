import random
print("\t\t\t\t\t   GUESS THE NUMBER")
print("..........................................Welcome to the game..........................................")
print('''Level 1. Basic
Level 2. Intermidiate
Level 3. Advance
Level 4. Expert''')
level=input("Enter the level you want to play:")
if (level == "Basic"):
    print("GAME BEGIN")
    print("Rules:-\n1. You will be given only THREE chances.\n2. Each time you have to enter a new number is previous falis.")
    num=random.randint(5,50)
    for i in range(3):
        x=int(input("Enter the your answer:"))
        if (x == num):
            print("YES You Are RIGHT")
            Y="YES You Are RIGHT"
            break
        else:
            print("SORRRY BETTER LUCK NEXT TIME")
    if(x == num):
        print("HURRAY!!!! YOU WON")
    else:
        print("SORRY!!!! TRY YOUR LUCK NEXT TIME")
if (level == "Intermidiate"):
    print("GAME BEGIN")
    print("Rules:-\n1. You will be given only THREE chances.\n2. Each time you have to enter a new number is previous falis.")
    num=random.randint(5,250)
    for i in range(3):
        x=int(input("Enter the your answer:"))
        if (x == num):
            print("YES You Are RIGHT")
            Y="YES You Are RIGHT"
            break
        else:
            print("SORRRY BETTER LUCK NEXT TIME")
    if(x == num):
        print("HURRAY!!!! YOU WON")
    else:
        print("SORRY!!!! TRY YOUR LUCK NEXT TIME")
if (level == "Advance"):
    print("GAME BEGIN")
    print("Rules:-\n1. You will be given only THREE chances.\n2. Each time you have to enter a new number is previous falis.")
    num=random.randint(5,5000)
    for i in range(3):
        x=int(input("Enter the your answer:"))
        if (x == num):
            print("YES You Are RIGHT")
            Y="YES You Are RIGHT"
            break
        else:
            print("SORRRY BETTER LUCK NEXT TIME")
    if(x == num):
        print("HURRAY!!!! YOU WON")
    else:
        print("SORRY!!!! TRY YOUR LUCK NEXT TIME")
if (level == "Expert"):
    print("GAME BEGIN")
    print("Rules:-\n1. You will be given only THREE chances.\n2. Each time you have to enter a new number is previous falis.")
    num=random.uniform(-2,2)
    for i in range(3):
        x=float(input("Enter the your answer:"))
        if (x == num):
            print("YES You Are RIGHT")
            Y="YES You Are RIGHT"
            break
        else:
            print("SORRRY BETTER LUCK NEXT TIME")
    if(x == num):
        print("HURRAY!!!! YOU WON")
    else:
        print("SORRY!!!! TRY YOUR LUCK NEXT TIME")
