#Welcome to the unrefined rock paper scissors game. Enjoy

import random
#Users input
while True:
    choice = input("Alright lets play rock paper scissors : ")
    choice = choice.lower()

    print("You chose", choice)

    #Computers Turn
    choices = ["rock","paper","scissors"]
    cc = choices[random.randint(0, len(choices)-1)]
    print("Zehahaha! I've chosen", cc)

    #Results
    if choice in choices:
        if choice == cc:
            print("bro we got the same")
        if choice == "rock":
            if cc == "paper":
                print("Seems you've lost.")
            elif cc == "scissors":
                print("damn it you defeated me!!")

        if choice == "paper":
            if cc == "paper":
                print("damn it you defeated me!!")
            elif cc == "rock":
                print("Ill be learning from this loss.")

        if choice == "scissors":
            if cc == "paper":
                print("You beat me?")
            elif cc == "rock":
                print("Ok realistically I could beat you with scissors, but fine I guess I lose.")
    else:
        print(".... you know we're playing rock paper scissors right.")

        print()
