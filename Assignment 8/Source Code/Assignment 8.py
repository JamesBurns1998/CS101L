
##########################################################################################################################################
## CS101 Lab
## Assignment 8
## James Burns
## 
##
## PROBLEM: Create a program which allows the user to enter 2 types of grades; Tests and Programs.  Each of our scores is assumed to be out of 100, so we only need the users score.  The tests are 60% of a student’sgrade, while the assignments are 40%. Program will print a menu of options: add test, remove test, clear tests, add assignment, remove assignment, clear assignments, display grades, quit.  Display will show number of each type, minimum and maximum scores, average, standard deviation, and weighted average.
## 
## ALGORITHM:
##  1. import math module
##  1. Create function print_menu() to display 8 options: add test, remove test, clear tests, add assignment, remove assignment, clear assignments, display grades, quit. 
##  2. Define function get_new_score() with argument (prompt) to return a score to add. Try converts argument to float zero or greater except value error. 
##  3. Define function remove_score() with two parameters list1 and prompt to remove a score from list1.  
##  4. Define function avg() with parameter list1 to compute average of values in list1 and return as a float with 2 decimals
##  5. Define function std() with parameter list1 to compute standard deviation. Iterates through list, subtracts each value from average (calling funciton avg()), and computes std, returns as a float with 2 decimals.
##  6. Define function weighted_average() with parameters list1 and list2. calls function avg() for each list, multiplies list 1 by .6, list 2 by .4. Returns weighted average to two decimals
##  7. Define function display_scores() with 2 parameters list1 and list2. Formats results into rows containing score type (Test/Assignment), length of each list, min in each list, max in each list, average of list (calling avg()), std (calling std()), and weighted average (calling weighted_average()).
##  In Main:
##  8. create empty list "tests" and empty list"assignments"
##  9. Create while loop to break with "q" or "Q"
##  10. Call funciton print_menu()
##  11. Prompt user for input from menu
##  12. Initiate while loop to run until valid input is given for choice
##  13. If choice 1: call get_new_score() for user input and append value to tests.
##  14. If choice 2: call remove_score() for argument tests and user input 
##  15. If choice 3: clear list tests.
##  16. If choice 4: call get_new_score() for user input and append value to assignments.
##  17. If choice 5: call remove_score() for argument assignments and user input 
##  18. If choice 6: clear list assignments.
##  19. If choice d or D: call display() for tests and assignments
##  20. If choice q or Q: break
##
###############################################################################################################################################################

import math

def print_menu():
    print("\n{:^40}".format("Grade Menu"))
    print("1 - Add Test")
    print("2 - Remove Test")
    print("3 - Clear Tests")
    print("4 - Add Assignment")
    print("5 - Remove Assignment")
    print("6 - Clear Assignment")
    print("D - Display Scores")
    print("Q - Quit\n")

def get_new_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            while score < 0:
                score = float(input("Score must be 0 or greater. Try again: "))
            return score
            break
        except ValueError:
            print("Score must be a number. Try again")

def remove_score(list1, prompt):
    score_to_remove = int(input(prompt))
    if score_to_remove not in list1:
        print("Could not find that score to remove.")
    else:
        list1.remove(score_to_remove)

def avg(list1):
    if len(list1) != 0:
        avg = (sum(list1))/(len(list1))
    else:
        avg = 0
    return "{:.2f}".format(avg)

def std(list1):
    sum = 0
    for i in list1:
        sum += ((i - float(avg(list1)))**2)
    std = math.sqrt(sum/len(list1))
    return "{:.2f}".format(std)

def weighted_total(list1, list2):
    if len(list1) == 0:
        weighted_average = (float(avg(list2))) * (0.4)
    elif len(list2) == 0:
        weighted_average = (float(avg(list1))) * (0.6)
    else:
        weighted_average = (float(avg(list1)) * 0.6) + (float(avg(list2)) * 0.4)
    return "{:.2f}".format(weighted_average)

    

def display_scores(list1, list2):
    print("\n{:<20}{:<8}{:<10}{:<10}{:<10}{:>5}".format("Type" , "#" , "min" , "max" , "avg" , "std"))
    print("{:=^63}".format(""))
    if len(list1) == 0:
        print("{:<20}{:<8}{:<10}{:<10}{:<10}{:>5}".format("Tests" , "0" , "n/a" , "n/a" , "n/a" , "n/a"))
    else:
        print("{:<20}{:<8}{:<10}{:<10}{:<10}{:>5}".format("Tests" , len(list1) , min(list1) , max(list1) , avg(list1) , std(list1)))
    if len(list2) == 0:
        print("{:<20}{:<8}{:<10}{:<10}{:<10}{:>5}".format("Assignments" , "0" , "n/a" , "n/a" , "n/a" , "n/a"))
    else:
        print("{:<20}{:<8}{:<10}{:<10}{:<10}{:>5}".format("Assignments" , len(list2) , min(list2) , max(list2) , avg(list2) , std(list2)))
    print("\nWeighted Score: {}".format(weighted_total(list1, list2)))


if __name__ == "__main__":

    tests = []
    assignments = []

    while True:
        print_menu()
        choice = input("==> ")

        while (choice != '1') and (choice != '2') and (choice != '3') and (choice != '4') and (choice != '5') and (choice != '6') and (choice != 'D') and (choice != 'd') and (choice != 'q') and (choice != 'Q'):
            choice = input("Please enter a valid option from Grade Menu ==> ")
        if choice == '1':
            new_score = get_new_score("\nEnter the new Test score: ")
            tests.append(new_score)
        elif choice == '2':
            remove_score(tests, "\nEnter the Test score to remove: ")
        elif choice == '3':
            tests.clear()
        elif choice == '4':
            new_score = get_new_score("\nEnter the new Assignment score: ")
            assignments.append(new_score)
        elif choice == '5':
            remove_score(assignments, "\nEnter the Assignment score to remove: ")
        elif choice == '6':
            assignments.clear()
        elif (choice == 'D') or (choice == 'd'):
            display_scores(tests, assignments)
        elif (choice == 'q') or (choice == 'Q'):
            break




    

