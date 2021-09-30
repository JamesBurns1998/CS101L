#James Burns
#Lab Assignment 3

print("Welcome to the Flarsheim Guesser!\n")

play = 'y'

# initiate while loop to continue while user input is equal to "y" or "Y"
while play == 'Y' or play == 'y':
    print("\nPlease think of a number between and including 1 and 100.\n")

    # obtain input for remainder when number is divided by 3, assign to variable rem_3
    # initiate while loop to obtain input until remainder is between 0 and 2.
    rem_3 = int(input("What is the remainder when your number is divided by 3?")) 
    while rem_3<0 or rem_3>2:
        if rem_3 < 0:
            print("The value entered must be 0 or greater.")
            rem_3 = int(input("What is the remainder when your number is divided by 3?"))
        if rem_3 > 2:
            print("The value entered must be less than 3.")
            rem_3 = int(input("What is the remainder when your number is divided by 3?"))
    print(rem_3)

    # obtain input for remainder when number is divided by 5, assign to variable rem_5
    # initiate while loop to obtain input until remainder is between 0 and 4.
    rem_5 = int(input("What is the remainder when your number is divided by 5?"))
    while rem_5<0 or rem_5>4:
        if rem_5 < 0:
            print("The value entered must be 0 or greater.")
            rem_5 = int(input("What is the remainder when your number is divided by 5?"))
        if rem_5 > 4:
            print("The value entered must be less than 5.")
            rem_5 = int(input("What is the remainder when your number is divided by 5?"))
    print(rem_5)

    # obtain input for remainder when number is divided by 7, assign to variable rem_7
    # initiate while loop to obtain input until remainder is between 0 and 6.
    rem_7 = int(input("What is the remainder when your number is divided by 7?"))
    while rem_7<0 or rem_7>6:
        if rem_7 < 0:
            print("The value entered must be 0 or greater.")
            rem_7 = int(input("What is the remainder when your number is divided by 7?"))
        if rem_7 > 6:
            print("The value entered must be less than 7.")
            rem_7 = int(input("What is the remainder when your number is divided by 7?"))
    print(rem_7)

    #initiate loop for all integers [1,100]
    for i in range(1,101):
        if i%3 == rem_3 and i%5 == rem_5 and i%7 == rem_7:
            print("Your number was" , i)
            print("How amazing was that?\n")

    play = input("Do you want to play again? Y to continue, N to quit.")
    while play != 'Y' and play !='y' and play != 'N' and play !='n':
        play = input("Do you want to play again? Y to continue, N to quit.")