########################################################################
## CS 101 Lab
## Program # 4
## James Burns
## Email: jrbgmf@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. import random module
##      2. define function play_again() prompting user to input a string to playing. If yes, return boolean TRUE, else, return False
##      3. Define function get_wager(), prompting user to input an integer greater than 0. Validate input is valid, loop until valid.
##      4. Define funtion get_slot_results() to return three integers between 0 and 10 using random module
##      5. Define function get_reels() to return integer for number of matches betweeen parameters reela, reelb, reelc
##      6. Define function get_bank() to return input integer between 1 and 100. Loop until input is valid.
##      7. Define function get_payout() with parameters wager,matches to return calculated winnings (10*wager if 3 matches; 3*wager if 2 matches; -1*wages if 0 matches)
##   in Main:
##      8. initiate while loop to play only while play = True
##      9. Initiate while loop to run while bank > 0
##      10. call function get_bank() and set to variable bank
##      11. call variable get_slot_results() and set to variables reel1, reel2, reel3
##      12. call function get_matches() for args reel1, reel2, reel3. Set to variable matches
##      13. call function get_payout() for args matches, wagers
##      14. set variable bank to bank+payout
##      15. Print results 
##      16. call funciton play_again() 
## 
## ERROR HANDLING:
##      Wager not less than 0, not greater than bank. Bank not less than 1. Playing equal to Y/y/Yes/yes/YES/N/n/No/NO/no. 
##
########################################################################

#import modules needed
import random


def play_again() -> bool:
  play = input("Do you want to play again?")
  while play != "Y" or play != "y" or play != "YES" or play != "yes" or play != "Yes" or play != "N" or play != "n" or play != "NO" or play != "No" or play != "no":
      if play == "Y" or play == "y" or play == "YES" or play == "Yes" or play == "yes":
        return True
      elif play == "N" or play == "n" or play == "NO" or play =="No" or play == "no":
        return False
      else:
        print("You must enter Y/YES/N/No to continue. Please try again")
        play = input("Do you want to play again?")
     
def get_wager(bank : int) -> int:
    wager = int(input("How many chips would you like to wager?"))
    while wager < 0 or wager > bank:
        if wager < 0:
            print("The wager amount must be greater than 0. Please try again.")
            wager = int(input("How many chips would you like to wager?"))
        elif wager > bank:
            print("The wager amount cannot be greater than the amount you have.")
            wager = int(input("How many chips would you like to wager?"))
    return wager

def get_slot_results() -> tuple:
    spin1 = random.randint(1,10)
    spin2 = random.randint(1,10)
    spin3 = random.randint(1,10)
    return (spin1 , spin2 , spin3)

def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb == reelc:
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    else:
        return 0

def get_bank() -> int:
    chips = int(input("How many chips would you like to start with?"))
    while chips < 1 or chips > 100:
        if chips < 1:
            print("Too low a value, you can only choose 1-100 chips")
            chips = int(input("How many chips would you like to start with?"))
        elif chips > 100:
            print("Too high a value, you can only choose 1-100 chips")
            chips = int(input("How many chips would you like to start with?"))
    return chips

def get_payout(wager, matches):
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1     


if __name__ == "__main__":
    
    playing = True
    while playing == True:

        bank = get_bank()
        initial_bank = bank
        max_bank = [bank]
        spins = 0

        while bank > 0:  
            
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            spins += 1
            max_bank.append(bank)

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
 
        print("You lost all", initial_bank, "in", spins, "spins")
        print("The most chips you had was", max(max_bank))
        playing = play_again()