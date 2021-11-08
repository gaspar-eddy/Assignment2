# Program Cat and Mouse Game 
# Description: 
#   This program is a simple cat and mouse game
# Author: Eddy Gaspar
# Date: 5 November 2021
# Revised: 
#   <revision date> 

# import library modules here
import catAndMouseFunctions
# Define global constants (name in ALL_CAPS)

def main():

    # Declare Variable types (EVERY variable used in this main program)
    playAgain = str()

    playAgain = str(input('Welcome to my cat and mouse game! To play, enter yes. To exit, enter any other key. '))

    if playAgain == 'yes':
        while playAgain == 'yes':

            catAndMouseFunctions.catMouseGameplay()

            playAgain = str(input('Would you like to play again? Enter yes to continue, or enter any other key to quit. '))
    
    else:

        print('Ok byeeeeee.')

# End Program

main()