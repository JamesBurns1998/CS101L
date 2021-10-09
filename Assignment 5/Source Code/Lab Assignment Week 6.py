
##########################################################################################################################################
##  ## CS 101 Lab
## Program # 5
## James Burns
## Email: jrbgmf@umsystem.edu
##
## PROBLEM : Create a program to check whether input library card numbers are valid. Must include 5 letters A-Z followed by digit (1,2,3) followed by a digit(1,2,3,4) followed by two digits (0-9) followed by a check digit.
##
## ALGORITHM :
##      import string module 
##      1. define function get_school() with parameter for input string idnumber to return college for (1,2,3) in idnumber[5]
##      2. define function get_grade() with parameter idnumber to return student's grade for (1,2,3,4) at idnumber[6] 
##      3. Define function character_valu() to convert string character to ascii value
##      5. Define function get_check_digit() to calculate check digit
##      6. Define function verify_check_digit() to verify for all conditions
##    In Main:
##      8. Format Title centered 60 spaces
##      9. Initiate while loop to run while user input is not "ENTER"
##      10. Prompt user for input string set to variable card_num
##      10. Set preconditions result = True adn error = ''
##      11. call function verify_check_digit() for argument card_num and set to variables result, error
##      12. If result == True, pring results, calling functions get_grade adn get_school
##      13. If result == False, print statement for invalid card and print error
##      
##
########################################################################

import string

def get_school(idnumber):
    if (int(idnumber[5])) == 1:
        school = "School of Computing and Engineering SCE"
    elif ((idnumber[5])) == 2:
        school = "School of Law"
    elif (int(idnumber[5])) == 3:
        school = "Collge of Arts and Sciences"
    return school

def get_grade(idnumber):
    if (int(idnumber[6])) == 1:
        grade = "Freshman"
    elif(int(idnumber[6])) == 2:
        grade = "Sophomore"
    elif (int(idnumber[6])) == 3:
        grade = "Junior"
    elif (int(idnumber[6])) == 4:
        grade = "Senior"
    return grade

def character_value(character):
    val = ord(character)-65
    return val

def get_check_digit(idnumber):
    x = 0
    for i in idnumber[0:5]:
        x += ((character_value(i)) * (idnumber.index(i)+1))
    for i in idnumber[5:9]:
        x += (string.digits.index(i) * (idnumber.index(i)+1))
    check_digit = (x % 10)
    return check_digit


def verify_check_digit(idnumber):
    if len(idnumber) != 10:
        result = False
        error = "The length of the number given must be 10"
    elif ((idnumber[0] not in string.ascii_uppercase) or (idnumber[1] not in string.ascii_uppercase) or (idnumber[2] not in string.ascii_uppercase) or (idnumber[3] not in string.ascii_uppercase) or (idnumber[4] not in string.ascii_uppercase)):
        result = False
        for i in idnumber[0:5]:
            if (i not in string.ascii_uppercase):
                print(i)
                error = "The first 5 characters must be A-Z, the invalid character at {} is {}.".format(idnumber.index(i) , i)
    elif (idnumber[8] or idnumber[9] or idnumber[10] or idnumber[11]) not in string.digits:
        result = False
        for i in idnumber[8:11]:
            if i not in string.digits:
                error = "The last 3 characters must be 0-9, the invalid character at {} is {}.".format(idnumber.index(i) , i)
    elif (idnumber[5] != "1" and idnumber[5] != "2" and idnumber[5] != "3"):
        result = False
        error = "The sixth character must be 1, 2, or 3"
    elif (idnumber[6] != "1" and idnumber[6] != "2" and idnumber[6] != "3" and idnumber[6] != "4"):
        result = False
        error = "The seventh character must be 1, 2, 3, or 4"
    elif ((get_check_digit(idnumber)) != int(idnumber[9])):
        result = False
        error = "Check Digit {} does not match calculated value {}.".format(idnumber[9] , (get_check_digit(idnumber)))
    else:
        result = True
        error = ""
    
    return result , error



if __name__ == "__main__":
    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:
        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break

        result = True
        error = ''

        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)

