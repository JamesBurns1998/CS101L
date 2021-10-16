#################################################################################################################################################################################################################################################################################################
## CS101 Lab
## Lab Assignment 6
## James Burns
## Email: jrbgmf@umsystem.edu
##
## PROBLEM: This program must encode and decode an input string according to the Caesar Cipher.  It should ask the user to enter 1,2, or Q to encode, decode, or quit.  The user will enter a string and a number to shift by. The program must print the encoded/decoded text.
##
## ALGORITHM: 
##      1. Define function Print_Menu() to print options for the user: 1 to encode, 2 to decode, Q to quit.
##      2. Define funciton Get_Input() to prompt user to input choice 1, 2, or Q.  Loops until input is valid.
##      3. Define function Encode(string_text , shift) to return encoded text. Iterates through input string for each character.  Converts char to ascii value, adds shift value, adjusts for end of alphabet if ascii value is > 90.
##      4. Define funciton Decode(string_text , shift) to return decoded text. Iterates through input string for each character. Converts char to ascii value, subtracts shift value, adjusts for begining of alphabet if ascii value is < 65.
##  in Main:
##      5. Initiate while loop to continue while Again = True
##      6. Call function Print_Menu()
##      7. Call function Get_Input. Set to variable choice
##      8. If choice 1, prompt user for input string, convert to uppercase. Prompt user for shift value, convert to integer.
##      9. Call function Encode()
##      10. If choice 2, prompt user for input string, convert to uppercase. Prompt user for shift value, convert to integer.
##      11. If choice Q or q, print "Have a nice day!". Again = False (breaks loop
##
## ERROR HANDLING: User choice equal to '1', '2', 'Q', or 'q'
##      
################################################################################################################################################################################################################################################################################################

def Print_Menu():
  print("\nWould you like to:")
  print("   1 - Encode a string")
  print("   2 - Decode a string")
  print("   Q - Quit")

def Get_Input():
  user_choice = input("Enter 1, 2, or Q: ")
  while ((user_choice != '1') and (user_choice != '2') and (user_choice != "Q") and (user_choice!= "q")):
      user_choice = input("Your choice must be 1, 2, or Q. Try again: ")
  return user_choice

def Encode(string_text, shift):
  encoded_string = ''
  for character in string_text:
    if character == " ":
      new_char = " "
    else:
      new_value = ord(character) + shift
      if new_value > 90:
        new_value -= 26
      new_char = chr(new_value)
    encoded_string += new_char
  return (encoded_string)

def Decode(string_text, shift):
  new_string = ''
  for character in string_upper:
    if character == " ":
      new_char = " "
    else:
      new_value = ord(character) - shift
      if new_value < 65:
        new_value += 26
      new_char = chr(new_value)
    new_string = new_string + new_char
  return (new_string)


if __name__ == "__main__":
    print("\nWelcome to Caesar Cipher!")
    Again = True
    while Again:
        Print_Menu()
        choice = Get_Input()
        if choice == '1':
            string_upper = input("Enter brief text to encode: ").upper()
            shift = int(input("Enter the number to shift letters by: "))
            encoded_text = Encode(string_upper , shift)
            print("Encoded:" , encoded_text)
    
        elif choice =='2':
            string_upper = input("Enter brief text to decode: ").upper()
            shift = int(input("Enter the number to shift letters by: "))
            decoded_text = Decode(string_upper , shift)
            print("Decoded:" , decoded_text)
    
        elif (choice == "Q" or choice == "q"):
            print("Have a nice day!")
            Again = False
