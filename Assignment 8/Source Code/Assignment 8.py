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




    

