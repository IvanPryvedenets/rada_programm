import psycopg2.errors


class Rada:
    def __init__(self):  # Create an __init__ method

        self.conn = psycopg2.connect(host="localhost", database="oopadvance", user="ivan", password="password")  # Connect to the db

        self.cur = self.conn.cursor()  # Create a cursor

        self.sql = """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"""  # Input the command that will be use quite often

    def add_fraction(self):  # Add table to the db

        fraction = input('Input fraction name: ')  # Input name of a table

        self.sql = """CREATE TABLE {} (
                {}_id SERIAL PRIMARY KEY, 
                name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                age VARCHAR(3) NOT NULL,
                briber VARCHAR(5) NOT NULL,
                brib VARCHAR(6) NOT NULL,
                height VARCHAR(4) NOT NULL,
                mass VARCHAR(4) NOT NULL
            )""".format(fraction, fraction)  # Type the command and fields while will be in the table

        try:
            self.cur.execute(self.sql)  # Try to create a new table

        except Exception:  # If the table is already exist than catch an exception
            print('Similar fraction was already exist\n')

        self.conn.commit()  # Save changes

        self.cur.close()  # Del the cursor
        self.conn.close()  # Del the connection

        print('Fraction {} was add successfully\n'.format(fraction))  # If all was ok

    def del_fraction(self):  # Delete a table in the db

        fraction = input('Input fraction name: ')  # Input a table name

        self.sql = "DROP TABLE {}".format(fraction)  # Type the command

        try:  # Try do delete a table
            self.cur.execute(self.sql)
            print('Fraction {} was delete successfully\n'.format(fraction))

        except Exception:  # If table doesn't not exist print next message
            print('Table {} does not exist\n'.format(fraction))

        self.conn.commit()  # Save changes

        self.cur.close()
        self.conn.close()

    def show_fractions(self):  # Show all tables in the db

        self.cur.execute(self.sql)  # Do commands that was created in an __init__ method

        row = self.cur.fetchone()  # Take a row

        while row is not None:  # While row is somethings
            print(row[0])  # Show a table name
            row = self.cur.fetchone()  # Go to the next row

    def all_deputies(self):  # Show all persons in a rada

        self.cur.execute(self.sql)  # Do commands that was created in an __init__ method

        fraction = self.cur.fetchone()  # Get a name of fraction

        deputies = list()  # Generate a list that will contain persons

        while fraction is not None:  # Check all names of the fractions

            deputies.append('\n' + fraction[0])  # Append name of a fraction to a list

            self.sql = "SELECT * FROM {}".format(fraction[0])  # Generate command which help us to get persons in a fraction

            fraction = self.cur.fetchone()  # Get a row

            self.cur.execute(self.sql)  # Insert commands

            deputy = self.cur.fetchone()  # Get a first row that has person data

            while deputy is not None:  # Check all rows

                deputies.append(deputy)  # Add person data to the list

                deputy = self.cur.fetchone()  # Go to a next row

        return deputies  # Return a list

    def rada_biggest_briber(self, bribers):  # Show a biggest briber in a rada

        for brib in bribers:  # For person in list
            if type(brib) == str:  # If "fraction name" - delete this thing because a list contain tuple - person data and str - name of fractions
                bribers.remove(brib)  # Delete a fraction name

        money = [int(brib[5]) for brib in bribers]  # Get value of "brib" marker

        money.sort(reverse=True)  # Sort integers from biggest to smallest

        brib = [brib for brib in bribers if int(brib[5]) == money[0]]  # Find person that has a biggest "brib" marker

        print(brib[0])  # Show this person


