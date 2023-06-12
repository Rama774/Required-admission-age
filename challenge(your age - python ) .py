# How old are you and Have you ever joined python bootcamp
age=int(input("How old are you?"))

if age > 18 :
 b=str(input("Have you ever joined python bootcamp?"))
 if b=="yes":
     print("Ther are other interesting programs you can join")
 elif b=="no":
     print("Welcome to python bootcamp")
elif age==18:
    b = str(input("Have you ever joined python bootcamp?"))
    if b == "yes":
     print("Ther are other interesting programs you can join")
    elif b == "no":
        print("Welcome to python bootcamp")
else:
    print("Sorry you can’t joined See you next years")