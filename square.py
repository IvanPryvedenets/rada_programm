import io

import psycopg2


# The class 'Human'
class Human:
    def __init__(self, t):  # Second argument is tuple

        for i in t:
            i.title()

        self.name = t[0]
        self.last_name = t[1]
        self.age = t[2]
        self.briber = t[3]
        self.brib = 0
        self.height = t[5]
        self.mass = t[6]

        if self.briber == 'True':  # If a str in tuple is True when will call a Deputy class a give_tribute method
            Deputy.give_tribute(self)

    def __hash__(self):  # Take sum of hash values: name and last_name
        return hash(self.name) + hash(self.last_name)

    def __eq__(self, other):  # Compare items
        return self.name == other.name and \
                self.last_name == other.last_name

    def __str__(self):  # When Human copy will be call, this method will return a tuple with next content
        return self.name, self.last_name, self.age, self.briber, self.brib, self.height, self.mass


class Deputy(Human):  # This class checks have some deputy criminal money or not
    def give_tribute(self):

        if self.briber == False:  # If a variable in Human class __init__ method is False
            print('This person is not a briber')

        else:

            brib = int(input('How much money wold like to take this deputy? '))  # Input, how much money briber take's in his hands

            if brib > 10000:
                print('This deputy may to go to the police')
                self.brib = brib

            else:
                self.brib = brib


class Fraction:  # Fraction may to create, delete, show deputies, clear fraction and other things
    def __init__(self):

        self.conn = psycopg2.connect(host="localhost", database="oopadvance", user="ivan", password="password")  # Connect to Postgre db

        self.cur = self.conn.cursor()  # Create cursor

        self.fraction = input('Input fraction name: ')  # This input will be use quite often

        self.sql = "SELECT * FROM {}".format(self.fraction)  # This sql request will be use quite often

    def add_deputy(self):  # Add deputy and write him to the file

        print('Input deputy data')

        deputy = input('Name: '), input('Last name: '), input('Age: '), input('Briber: '), input('Height: '), input('Mass: ')

        deputy1 = Deputy(deputy)  # deputy tuple is an argument in Human class

        self.sql = """INSERT INTO {}(name, last_name, age, briber, brib, height, mass)
         VALUES(%s,%s,%s,%s,%s,%s,%s);""".format(self.fraction)  # Change a self.sql variable

        try:  # If fraction will be exist
            self.cur.execute(self.sql, deputy1.__str__())  # self.sql - inserting into db that user wrote to fraction variable
            print('Deputy was added successfully!')

        except Exception:
            print('Fraction {} does not exist or somethings wrong'.format(self.fraction))

        self.conn.commit()  # Commit changes to the db

        self.cur.close()  # Del cursor
        self.conn.close()  # Close connection to the db

    def del_deputy(self, criminal):  # Delete the deputy from a file, if name and last name the same with deputy data and data that typed the user

        self.conn = psycopg2.connect(host="localhost", database="oopadvance", user="ivan", password="password")  # Connect to Postgre db

        self.cur = self.conn.cursor()  # Create cursor

        mark = None  # This marker will change if some row will be delete from a table, else his "if" operator will print "does't not find similar data"

        self.cur.execute(self.sql)  # Insert commands that were wrote in __init__ method

        row = self.cur.fetchone()  # Get row from db

        if criminal is not None:  # If was called a police method what return criminal list

            i = len(criminal) - 1  # Create a counter / The counter will start from the end of criminal

            while row is not None:  # While row is something

                if criminal[i][:3] == row[:3]:  # If data in item of criminal list similar to data of row

                    self.cur.execute("DELETE FROM {} WHERE {}_id = %s".format(self.fraction, self.fraction), (row[0],))  # Delete row from the db
                    # self.conn.commit()  # Save changes in the db
                    self.cur.execute(self.sql)  # Insert commands that were wrote in __init__ method

                    print('Deputy {} was deleted successfully'.format(row))
                    row = self.cur.fetchone()  # Go to next row
                    i -= 1  # Subtract 1 in counter

                else:  # If data isn't similar, go check next row
                    row = self.cur.fetchone()

        else:  # If police method wasn't called
            print('Input data of deputy that you want to delete')
            data = input('Name: '), input('Last name: ')  # The user type some data

            # In this case actions are similar like in "if" block

            while row is not None:

                if row[1:3] == data:

                    self.cur.execute("DELETE FROM {} WHERE {}_id = %s".format(self.fraction, self.fraction), (row[0],))
                    self.conn.commit()
                    print('Deputy {} was deleted successfully'.format(row))
                    mark = 1
                    break  # If row was deleted from the db - break, because the fraction doesn't has a similar name and last name of person

                else:
                    row = self.cur.fetchone()

            if mark is None:
                print("does't not find similar data")

        self.cur.close()  # Delete cursor
        self.conn.close()  # Stop connection

    def show_deputies(self):  # Show deputies of fraction

        self.cur.execute(self.sql)  # Insert commands that were created in a __init__ method

        row = self.cur.fetchone()  # Get a first row

        deputies = list()  # Create a list that will include all deputies of fraction

        while row is not None:  # While row is somethings

            deputies.append(row)  # Append row to the list
            row = self.cur.fetchone()  # Go to next row

        self.cur.close()
        self.conn.close()

        return deputies  # Return a deputies list

    def show_bribers(self, deputies):  # Show all bribers / "deputies" argument take a show_deputies method

        bribers = list(filter(lambda x: x[4] == 'True', deputies))  # Add deputy to the bribers list if person has "briber" marker True

        return bribers  # Return a briber list

    def biggest_briber(self, bribers):  # Show a biggest briber / "bribers" argument take a show_bribers method

        money = [int(brib[5]) for brib in bribers]  # Add to a money list values of "brib" marker

        money.sort(reverse=True)  # Sort integers from biggest to small

        brib = list(filter(lambda x: x == money[0], money))  # Add to the list one item that has a "brib" marker like a first item in a money list

        print(brib[0])  # Will be show a briber that has a biggest value of "brib" marker

    def police(self, bribers):  # Will be deleted that persons what have more like 10000 in a "brib" marker

        criminal = [brib for brib in bribers if int(brib[5]) > 10000]  # Add to a criminal list persons what have a value of "brib" marker more like 10000

        return criminal  # Return criminal list

    def clear_fraction(self):  # Delete all deputies in the fraction

        self.sql = "TRUNCATE {}".format(self.fraction)  # Clear table in db

        self.cur.execute(self.sql)  # Insert commands

        self.conn.commit()  # Save changes

        print('{} fraction was cleared'.format(self.fraction))  # Print that was done

        self.cur.close()
        self.conn.close()

    def are_deputies(self):  # The fraction has any deputies or not

        self.cur.execute(self.sql)  # Insert commands that were created in a __init__ method

        row = self.cur.fetchone()  # Get a first row in table

        if row:  # If table has any rows
            while row is not None:  # While row is somethings
                print(row)  # Show row
                row = self.cur.fetchone()  # Go to the next row

        else:  # If table is clear
            print('Fraction {} are clear'.format(self.fraction))

        self.cur.close()
        self.conn.close()
