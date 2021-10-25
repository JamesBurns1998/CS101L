##################################################################################################################################################
## CS101 Lab
## James Burns
## jrbgmf@umsystem.edu
## 
## PROBLEM: This program will ask user for a minimum mpg and a txt file to be read.  The program will loop using try and except until valid file entry is provided. File will be read and an output file will be created containing information for vehicles with mpg >= minimum mpg. 
## 
## ALGORITHM:
##  1. define function get_minimum_mpg() to optain user input, an integer between 1 and 100, looping until valid entry is given.
##  2. define function open_input_file() to obtain input for file name.  Reads file except if FileNotFound Error occurs.
##  3. define function open_outpu_file() to obtain input for outfile name.  Writes file except if IO Error.
##  4. Call get_minimum_mpg() and set to variable min_mpg
##  5. Call open_input_file() and readlines of file
##  6. iterate through lines in file, splitting by "\t"
##  7.  for each line in file, if combined mpg > min_mpg, Year, make, model, combined mpg are written to output file, except for value error.
##
## Error Handling: min_mpg must be number - ValueError; input file name must be in folder - FileNotFoundError; output file name must be valid, IOError
##
#########################################################################################################################################################################

def get_minimum_mpg():
    while True:
        try:
            min_mpg = int(input("Enter the minimum mpg: "))
            if min_mpg < 0:
                print("Fuel economy given must be greater than 0.")
            elif min_mpg > 100:
                print("Fuel economy given must be less than 100.")
            else:
                return min_mpg
        except ValueError:
            print("You must enter a number for the fuel economy.")

def open_input_file():
    while True:
        try:
            input_file = input("Enter the name of the input vehicle file: ")
            file = open(input_file, "r")
            return file
        except FileNotFoundError:
            print("Could not open file" , input_file)   

def open_output_file():
    while True:
        try:
            output_file = input("Enter the name of the file to output to: ")
            file = open(output_file, "w")
            return file
        except IOError:
            print("There is an IO Error for the file name" , output_file)


if __name__ == "__main__":

    min_mpg = get_minimum_mpg()
    print()

    file1 = open_input_file()
    file1.readline()
    print()

    out_file = open_output_file()
    print()

    for line in file1:
        list_values = line.split("\t")
        try:
            mpg = float(list_values[-3])
            if mpg >= min_mpg:
                output_string = "{:<5}{:<20}{:40}{:>10}\n".format(list_values[0], list_values[1], list_values[2] , mpg)
                out_file.write(output_string)
        except ValueError:
            print("Could not convert value" , list_values[-3] , "for" , list_values[0] , list_values[1] , list_values[2])