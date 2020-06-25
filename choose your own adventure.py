
answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":
    
    answer = input("You reached a crossroad, would you like to go right or left?").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, would you like to fight or run away?")

        if answer == "fight":
            print("That wasn't the greatest coice, you lost")
        else:
            print("Good choice, you made it away")
            
    elif answer == "right":
        print("You walk endlessly to the right, you lost")

else:
    print("Bye Bye")
       


