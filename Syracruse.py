#   This program takes an integer as input and returns the Syracruse
#   Sequence printed in an organized list.
#   Author: Joseph Prostko
#   Project: Assignment 2: Python; Question 3
#   Version: October 2019
def main():
    # The user is prompted to enter an integer value.
    print("This program outputs a Syracruse sequence.")

    # The integer value is initially entered as a String.
    tempString = input("Enter the initial value (an int => 1):")

    # temp holds the value of tempString as an integer.
    temp = int(tempString)

    # tempArray holds each value of the sequence.
    tempArray = []

    # temp is added to tempArray.
    tempArray.append(temp)

    # This while loop continues the sequence as long as temp does not equal 1.
    while (temp != 1.0):

        # The if statement below executes when temp is even.
        if (temp % 2 == 0):

            # temp is divided by 2.
            temp = temp / 2

            # temp is added to tempArray.
            tempArray.append(temp)
        
       # The else statement below executes when temp is odd.
        else:
            
            # temp is multiplied by 3 and incremented by 1.
            temp = 3*(temp) + 1

            # temp is added to tempArray.
            tempArray.append(temp)
    
    # Each value of the sequence is printed.
    print (tempArray)

# The main method is invoked.
main()