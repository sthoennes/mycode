#!/usr/bin/python3
round = 0
answer = " "
#ans = answer.lower()


while round < 3 and answer != "brian":
#while round < 3 and answer.lower() != "brian":
    round += 1     # increase the round counter by 1
    #answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ').lower()
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ').lower()
    if answer == "shrubbery":
        print("That's super secret answer'")
        break
    #ans = answer.lower()
    if answer == "brian": # logic to check if user gave correct answer
    #if answer.lower() == "brian": # logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    #elif answer.lower() == "shrubbery":
     #   print("You gave the super secret answer!")
      #  break
    else:                 # if answer was wrong
        print("Sorry. Try again!")

