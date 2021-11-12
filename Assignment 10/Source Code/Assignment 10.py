#######################################################################################################################
## CS101 Lab
## Assignment 10
## James BUrns
##
## PROBLEM: Create a program that asks the user for a text file to read.  Program will read all the words and output a count of the words that are used the most, concerned only with words that have a length greater than 3.  Punctuation will be cleaned from the beginning and ending of words. Program will output the top 10 words that are used most, with the most frequently used words at the top. All words that are 3 characters or less will be excluded.Program will output the number of words that appear only once and output how many unique words there are.
##
## ALGORITHM:
##  1. Define function open_file() to try opening and returning an input file except for file not found error.  If not found, loops until valid input.
##  2. Define function clean_words() with parameter list to iterate through strings in a list. If punctuation is present, removes from string. Returns new list.
##  3. Define funciton word_frequency_dict() with parameter list to return a dictionary with unique words as keys and number of occurances as values. Removes keys length 3 and shorter. Increments each occurence of key and sets as value 
##  4. Define function sort_dict() with parameter dictionary to sort keys in dicitonary according to value in reverse. 
##  5. Define function output_top_ten() with parameter dictionary to print first ten keys and values of sorted dictionary. If shorter than 10 keys, prints length of dictionary.
##  6. Define function output_occurs_once() with parameter dictionary. Iterates through dictionary, increments by one for each key with value 1. Prints count of incremented values.  
##  7. Define funciton output_uniques() with parameteter dictionary to print the length of dictionary
## In Main:
##  8. Call funciton open_file()
##  9. Read file as a string and set to variable "str_file"
##  10. Split string by " ". Iterate through string, removing each occurance of "\n"
##  11. Call function clean_words() for str_file, set to variable clean_list
##  12. call funciton word_frequency_dict() for clean_list, set to variable word_count
##  13. Call function output_top_ten() for word_count
##  14. Call funciton output_occurs_once() for word_count
##  15. Call function output_uniques() for word_count
##
## ERROR HANDLING:
##  1. Exception for FileNotFoundError for input file
##  2. Exception for KeyError when creating new dictionary. 
##
######################################################################################################################################################################

def open_file():
    while True:
        try:
            input_file = input("Enter name of the file to open ==> ")
            file = open(input_file, "r")
            return file
            break
        except FileNotFoundError:
            print("Could not find" , input_file, "\n")

def clean_words(list1):
    punctuation = ".,!?-:;"
    clean_list = []
    for i in list1:
        for j in i:
            if j in punctuation:
                i = i.replace(j,"")
        clean_list.append(i.lower())
    return clean_list

def word_frequency_dict(list1):
    new_list = []
    word_dict = {}
    for i in list1:
        if (len(i) > 3):
            new_list.append(i)
    for i in new_list:
        try:
            word_dict[i] += 1
        except KeyError:
            word_dict[i] = 1
    return (word_dict)

def sort_dict(words_dict):
    sorted_values = sorted(list(set(words_dict.values())), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for key in words_dict:
                if words_dict[key] == i:
                    sorted_dict[key] = i
    return (sorted_dict)

def output_top_ten(words_dict):
    sorted_dict = sort_dict(words_dict)
    count = 0
    print("\nMost frequently used words")
    print("{:<2}{:>17}{:>10}".format("#", "Word" , "Freq."))
    print("==============================")
    for key in sorted_dict:
        print("{:<2}{:>17}{:>10}".format((count+1), key, sorted_dict[key]))
        count += 1
        if count == 10: 
            break

def output_occurs_once(words_dict):
    count = 0
    for key in words_dict:
        if words_dict[key] == 1:
            count += 1
    print("\nThere are" , count , "words that occur only once.")

def output_uniques(words_dict):
    unique = len(words_dict)
    print("There are" , unique , "unique words in the document.\n")


   
if __name__ == "__main__":
    user_file = open_file()
    str_file = user_file.read()
    str_file = str_file.replace("\n", " ")

    word_list = str_file.split(" ")
    clean_list = clean_words(word_list)
    word_count = word_frequency_dict(clean_list)
    output_top_ten(word_count)
    output_occurs_once(word_count)
    output_uniques(word_count)
