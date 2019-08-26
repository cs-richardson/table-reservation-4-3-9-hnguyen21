'''
This code searches to match the inputted name with the "reserved" name, and if it does, it says "Right this way!". If it doesn't match, it says "Sorry, we don't have a reservation under that name."
by Ben
'''
name = input("What is your name? ")
reservationName = "Albert"


if name == reservationName:
    print("Right this way!")
else: 
    print("Sorry, we don't have a reservation under that name.")

