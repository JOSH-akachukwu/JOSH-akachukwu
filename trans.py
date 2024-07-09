print("Lets play a game \nin this game you are to pick a number perform some operations \nwith your choosen number and i will guess that number.")
def game():
    import random
    x = random.randint(1,12)
    
    print("Pick a number in your mind. \nNow multiply it by 3. ")
    print("Now add", x, "to it" '\n' "then subtract your actual number from the result.")
    try:
        reslt = float(int(input("enter your final result :")))
        number = (reslt - x)/2
    except:
        print("invalid result. Try playing with numbers")
    else:
        print("Your number is",number)
    re_play = input("Press enter to play again.")
    if re_play == '':
        return game()
    else:exit()

x = game()
print(x)
