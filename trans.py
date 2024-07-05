print("Lets play a game \n in this game you are to pick a number perform some operations \n with your choosen number and i will guess that number.")
def trick():
    import random
    x = random.randint(1,12)
    
    print("Pick a number in your mind. \nNow multiply it by 3. ")
    print("Now add", x, "to it" '\n' "then subtract your actual number from the result.")
    
    reslt = input("enter your final result")
    number = (reslt - x)/2
    if reslt == x:
        print("Your number is",number)

x = trick()
print(x)
