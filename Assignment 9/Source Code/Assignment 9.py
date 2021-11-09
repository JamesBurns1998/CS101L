##########################################################################################################################################################
## CS101 Lab
## Assignment 9
## James Burns
##
## PROBLEM: Create a program to ask the user for the file, use a try except so if the read_in_file function throws an error you can loop and ask for a filename again.  It should then output the month that has the highest crime rate.  The offense that occurs the most, and then ask for an offense and output a formatted report of the zip code and howmany times that offense occurs in that zip code. 
##
## ALGORITHM:
##  1. Import csv module
##  2. define function read_in_file with parameter file_name to open a csv file and create and return a list containing each row in the file as an element.
##  3. Define function create_reported_date_dict with a list as parameter. Creates a dictionary with keys as list element 1 and value as count of each key.
##  4. Define function create_reported_month_dict with a list as parameter. Creates a dictionary with keys as month (as an integer) and values as number of crimes in that month
##  5. Define function create_offense_dict with a list as parameter.  Creates dictionary with keys as offense name in list position 7, and values as number of each offense in list
##  6. Define function create_offense_by_zip_dict with parameter list.  Creates a nested dictionary with keys as offenses, and values as a dictionary containing zip code as keys and count as value
##  7. Define function convert_num_to_month with parameter integer to if num == 1, sets month to string "January", etc for each month
##  8. Define function zip_code_report to take parameter of offense and a list. calls create_offense_by_dict funciton and prints each key and value for input key offense;
## In Main:
##  9. create loop to try calling function read_in_file for input value except for FileNotFoundError. Sets output to variable "crime_list"
##  10. call function create_reported_month_dict for crime_list
##  11. find max value in reported_month_dict and call function convert_num_to_month
##  12. call function create_offense_dict for crime_list
##  13. find max value in create_offense_dict 
##  14. Call function zip_code_report for input offense and crime_list except for KeyError
##
####################################################################################################################################################################################################################################################################

import csv

def read_in_file(file_name):
    with open(file_name, encoding = "utf-8") as file:
        file_csv = csv.reader(file)
        crime_list = []
        for line in file:
            crime_list.append(line.split(","))
        return crime_list

def create_reported_date_dict(list1):
    reported_date_dict = {}
    for i in range(1,len(list1)):
        try:
            reported_date_dict[list1[i][1]] += 1
        except KeyError:
            reported_date_dict[list1[i][1]] = 1
    print(reported_date_dict)

def create_reported_month_dict(list1):
    date_list = []
    month_dict = {}
    for i in range(1,len(list1)):
        date_list.append(list1[i][1])
    for i in date_list:
        try:
            month_dict[int((i[0:2]).replace("/",""))] += 1
        except KeyError:
            month_dict[int((i[0:2]).replace("/",""))] = 1
    return month_dict

def create_offense_dict(list1):
    offense_dict = {}
    for i in range(1,len(list1)):
        try:
            offense_dict[list1[i][7]] += 1
        except KeyError:
            offense_dict[list1[i][7]] = 1
    return offense_dict

def create_offense_by_zip_dict(list1):
    offense_by_zip_dict = {}
    for i in range(1,len(list1)):
        offense = offense_by_zip_dict.get(list1[i][7], dict())
        try:
            offense[list1[i][13]] += 1
        except KeyError:
            offense[list1[i][13]] = 1
        offense_by_zip_dict[list1[i][7]] = offense
        '''if "" in offense_by_zip_dict[list1[i][7]]:
            del offense_by_zip_dict[list1[i][7]][""]'''
    return offense_by_zip_dict

def convert_num_to_month(num):
    if num == 1:
        month = "January"
    elif num == 2:
        month = "February"
    elif num == 3:
        month = "March"
    elif num == 4:
        month = "April"
    elif num == 5:
        month = "May"
    elif num == 6:
        month = "June"
    elif num == 7:
        month = "July"
    elif num == 8:
        month = "August"
    elif num == 9:
        month = "September"
    elif num == 10:
        month = "October"
    elif num == 11:
        month = "November"
    elif num == 12:
        month = "December"
    return month

def zip_code_report(offense, list1):
    offense_by_zip = create_offense_by_zip_dict(list1)
    offense_by_zip[offense]
    print()
    print(offense, "Offenses by Zip Code")
    print("{:<20}{:>3}".format("Zip Code", "# offenses"))
    print("==============================")
    for key in offense_by_zip[offense]:
        print("{:<20}{:>10}".format(key, offense_by_zip[offense][key]))
        


if __name__ == "__main__":
    while True:
        try:
            input_file = input("Enter the name of the crime data file ==> ")
            crime_list = read_in_file(input_file)
            break
        except FileNotFoundError:
            print("Could not find the file specified. " , input_file, " not found.")

    reported_month_dict = create_reported_month_dict(crime_list)
    max_crime_month = max(reported_month_dict, key=reported_month_dict.get)
    print("\nThe month with the highest # of crimes is {} with {} offenses.".format(convert_num_to_month(max_crime_month), reported_month_dict[max_crime_month]))

    offense_dict = create_offense_dict(crime_list)
    max_offense = max(offense_dict, key=offense_dict.get)
    print("The offense with the highest # of crimes is {} with {} offenses.".format(max_offense, offense_dict[max_offense]))

    while True:
        try:
            zip_code_report(input("\nEnter an offense ==> "), crime_list)
            break
        except KeyError:
            print("Not a valid offense found. Please try again.")

