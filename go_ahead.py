from rada import Rada
from square import Fraction


def main():  # Function that take accepts a number in calls methods of the class
    print('Operations with rada')
    print('*' * 20)

    print('1 - Add fraction to the rada\n'  # Print all operations available in a Rada class
          '2 - Drop fraction\n'
          '3 - Show fractions\n'
          '4 - Show all deputies\n'
          '5 - Show a biggest briber in rada\n\n')

    print('Operations with fraction')
    print('*' * 24)

    print('6 - Add deputy to the fraction\n'  # Print all operations available in a Rada class
          '7 - Delete the deputy\n'
          '8 - Show deputies in the fraction\n'
          '9 - Show bribers in the fraction\n'
          '10 - Police activation\n'
          '11 - Show a biggest briber\n'
          '12 - Clear the fraction\n'
          '13 - Are deputies in the fraction or not?\n')

    command = int(input('Chose your command: '))  # User inputs a command

    rada = Rada()  # Create a copy of a Rada class

    if command >= 6:  # If a command variable is rome like 6 than create a Fraction class copy
        fraction = Fraction()

    if command == 1:  # Add a table to the db
        rada.add_fraction()

    elif command == 2:  # Delete a table in the db
        rada.del_fraction()

    elif command == 3:  # Show all tables in the db
        rada.show_fractions()

    elif command == 4:  # Show all persons in the db
        deputies = rada.all_deputies()

        i = 0  # Create a marker

        while i < len(deputies):  # Do this while a marker isn't equal to length of a list
            print(deputies[i])
            i += 1  # + 1 to a marker

    elif command == 5:  # All persons in the table
        rada.rada_biggest_briber(rada.all_deputies())

    elif command == 6:  # Add person to the table
        fraction.add_deputy()

    elif command == 7:  # Delete person in the table
        fraction.del_deputy(None)

    elif command == 8:  # Show all persons in a table
        deputies = fraction.show_deputies()
        for dep in deputies:
            print(dep)

    elif command == 9:  # Show all bribers in the table
        bribers = fraction.show_bribers(fraction.show_deputies())
        for brib in bribers:
            print('The briber {} has {} money'.format(brib[1:3], brib[5]))

    elif command == 10:  # Delete persons in the table that have "brib" marker bigger like 100000
        fraction.del_deputy(fraction.police(fraction.show_bribers(fraction.show_deputies())))

    elif command == 11:  # Show biggest briber in the table
        fraction.biggest_briber(fraction.show_bribers(fraction.show_deputies()))

    elif command == 12:  # Clear table
        fraction.clear_fraction()

    elif command == 13:  # Are table some rows or not
        fraction.are_deputies()

    else:  # If command are bigger or smaller like 1 and 13 print next
        print('Try again')
        main()  # Call the a function again


main()  # Call a function
