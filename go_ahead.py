from rada import Rada
from square import Fraction


def main():
    print('Operations with rada')
    print('*' * 20)

    print('1 - Add fraction to the rada\n'
          '2 - Drop fraction\n'
          '3 - Show fractions\n'
          '4 - Show all deputies\n'
          '5 - Show a biggest briber in rada\n\n')

    print('Operations with fraction')
    print('*' * 24)

    print('6 - Add deputy to the fraction\n'
          '7 - Delete the deputy\n'
          '8 - Show deputies in the fraction\n'
          '9 - Show bribers in the fraction\n'
          '10 - Police activation\n'
          '11 - Show a biggest briber\n'
          '12 - Clear the fraction\n'
          '13 - Are deputies in the fraction or not?\n')

    command = int(input('Chose your command: '))

    rada = Rada()

    if command >= 6:
        fraction = Fraction()

    if command == 1:
        rada.add_fraction()

    elif command == 2:
        rada.del_fraction()

    elif command == 3:
        rada.show_fractions()

    elif command == 4:
        deputies = rada.all_deputies()

        i = 0

        while i < len(deputies):
            print(deputies[i])
            i += 1

    elif command == 5:
        rada.rada_biggest_briber(rada.all_deputies())

    elif command == 6:
        fraction.add_deputy()

    elif command == 7:
        fraction.del_deputy(None)

    elif command == 8:
        deputies = fraction.show_deputies()
        for dep in deputies:
            print(dep)

    elif command == 9:
        bribers = fraction.show_bribers(fraction.show_deputies())
        for brib in bribers:
            print('The briber {} has {} money'.format(brib[1:3], brib[5]))

    elif command == 10:
        fraction.del_deputy(fraction.police(fraction.show_bribers(fraction.show_deputies())))

    elif command == 11:
        fraction.biggest_briber(fraction.show_bribers(fraction.show_deputies()))

    elif command == 12:
        fraction.clear_fraction()

    elif command == 13:
        fraction.are_deputies()

    else:
        print('Try again')
        main()


main()
