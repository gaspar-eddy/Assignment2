# Library Cat and Mouse Game Functions 
# Functions Included in Library: 
#   catMouseGameplay()
#   startingPositions()
#   distanceCalc()
#   columnMoves()
#   rowMoves()
#   display()
# Author: Eddy Gaspar
# Date: 6 November 2021
# Revised: 
#   <revision date> 

# import library modules here
import random

# Define global constants (name in ALL_CAPS)
MAXROWS = int(10)
MAXCOLUMNS = int(10)
CATSPEED =  int(4)
MOUSESPEED = int(2)
CATCHDISTANCE = int(3)
MAXMOVES = int(15)

# Function catMouseGameplay()
# Description:
#   Performs the actual gameplay functions of the cat 
#   and mouse game
# Calls:
#   startingPositions()
#   distanceCalc()
#   columnMoves()
#   rowMoves()
#   display()
# Parameters:
#   none
# Returns:
#   none

def catMouseGameplay():

    # Declare Local Variable types (NOT parameters)
    turns = int()

    turns = 0

    # Generate random positions for cat and mouse
    catColumn, catRow, mouseColumn, mouseRow = startingPositions()

    # Calculate distance
    distance = distanceCalc(catColumn, catRow, mouseColumn, mouseRow)

    # While loop executes gameplay within max moves or until
    # mouse is caught
    while turns < MAXMOVES and distance > CATCHDISTANCE:

        turns += 1
        
        # Move cat and mouse columns
        catColumn, mouseColumn = columnMoves(catColumn, mouseColumn)

        # Move cat and mouse rows
        catRow, mouseRow = rowMoves(catRow, mouseRow)

        # Calculate distance
        distance = distanceCalc(catColumn, catRow, mouseColumn, mouseRow)

        # Display the situation
        display(catColumn, catRow, mouseColumn, mouseRow, distance)

    # Display result of the game
    if distance <= CATCHDISTANCE:
        print('The cat ate the mouse!')

    else:
        print('The cat got tired and gave up!')


    # Return the return variable, if any

#} Function catMouseGameplay()

# Function startingPositions()
# Description:
#   Creates random starting positions for cat and mouse
# Calls:
#   randint()
# Parameters:
#   none
# Returns:
#   none

def startingPositions():

    # Declare Local Variable types (NOT parameters)
    catColumn = int()
    catRow = int()
    mouseColumn = int()
    mouseRow = int()

    # Generate random cat and mouse positions
    catColumn = random.randint(0, MAXCOLUMNS)
    catRow = random.randint(0, MAXROWS)

    mouseColumn = random.randint(0, MAXCOLUMNS)
    mouseRow = random.randint(0, MAXROWS)

    # Return the return variable, if any
    return catColumn, catRow, mouseColumn, mouseRow

#} Function startingPositions()

# Function distanceCalc()
# Description:
#   Calculates distance between cat and mouse coordinates
# Calls:
#   none
# Parameters:
#   catColumn, catRow, mouseColumn, mouseRow
# Returns:
#   distance

def distanceCalc(catColumn, catRow, mouseColumn, mouseRow):

    # Declare Local Variable types (NOT parameters)
    distance = int()

    # Calculates distance apart
    distance = int(((catRow - mouseRow)**2 + (catColumn - mouseColumn)**2) **(1/2))

    # Return the return variable, if any
    return distance

#} Function distanceCalc()

# Function columnMoves()
# Description:
#   Determines move distance for cat and mouse columns
# Calls:
#   randint()
# Parameters:
#   catColumn, mouseColumn
# Returns:
#   catColumn, mouseColumn

def columnMoves(catColumn, mouseColumn):

    # Declare Local Variable types (NOT parameters)

    # Generate random moves for cat and mouse columns
    catColumn = catColumn + random.randint((-CATSPEED), CATSPEED)
    mouseColumn = mouseColumn + random.randint((-MOUSESPEED), MOUSESPEED)

    # Make sure cat is still on game board
    if catColumn > 10:
        catColumn = MAXCOLUMNS

    elif mouseColumn < 0:
        mouseColumn = 0

    else:
        catColumn = catColumn

    # Make sure mouse is still on game board
    if mouseColumn > 10:
        mouseColumn = MAXCOLUMNS

    elif mouseColumn < 0:
        mouseColumn = 0

    else:
        mouseColumn = mouseColumn

    # Return the return variable, if any
    return catColumn, mouseColumn

#} Function columnMoves()

# Function rowMoves()
# Description:
#   Determines move distance for cat and mouse rows
# Calls:
#   randint()
# Parameters:
#   catRow, mouseRow
# Returns:
#   catRow, mouseRow

def rowMoves(catRow, mouseRow):

    # Declare Local Variable types (NOT parameters)

    # Generate random moves for cat and mouse rows
    catRow = catRow + random.randint((-CATSPEED), CATSPEED)
    mouseRow = mouseRow + random.randint((-MOUSESPEED), MOUSESPEED)
    
    # Make sure cat is still on game board
    if catRow > 10:
        catRow = MAXROWS

    elif catRow < 0:
        catRow = 0

    else:
        catRow = catRow

    # Make sure mouse is still on game board
    if mouseRow > 10:
        mouseRow = MAXROWS

    elif mouseRow < 0:
        mouseRow = 0

    else:
        mouseRow = mouseRow

    # Return the return variable, if any
    return catRow, mouseRow

#} Function rowMoves()

# Function display()
# Description:
#   Displays game status
# Calls:
#   none
# Parameters:
#   catColumn, catRow, mouseColumn, mouseRow, distance
# Returns:
#   none

def display(catColumn, catRow, mouseColumn, mouseRow, distance):

    # Declare Local Variable types (NOT parameters)

    # Print game status
    print('\nCat:', catColumn, ',', catRow, '\tMouse:', mouseColumn, ',', mouseRow, '\tDistance:', distance)

#} Function display()

# End Module catAndMouseFunctions 