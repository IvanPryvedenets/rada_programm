import psycopg2.errors

from square import Fraction


class Rada:
    def __init__(self):

        self.conn = psycopg2.connect(host="localhost", database="oopadvance", user="ivan", password="password")

        self.cur = self.conn.cursor()

        self.sql = """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"""

    def add_fraction(self):

        fraction = input('Input fraction name: ')

        self.sql = """CREATE TABLE {} (
                {}_id SERIAL PRIMARY KEY, 
                name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                age VARCHAR(3) NOT NULL,
                briber VARCHAR(5) NOT NULL,
                brib VARCHAR(6) NOT NULL,
                height VARCHAR(4) NOT NULL,
                mass VARCHAR(4) NOT NULL
            )""".format(fraction, fraction)

        try:
            self.cur.execute(self.sql)

        except Exception:
            print('Similar fraction was already exist\n')

        self.conn.commit()

        self.cur.close()
        self.conn.close()

        print('Fraction {} was add successfully\n'.format(fraction))

    def del_fraction(self):

        fraction = input('Input fraction name: ')

        self.sql = "DROP TABLE {}".format(fraction)

        try:
            self.cur.execute(self.sql)
            print('Fraction {} was delete successfully\n'.format(fraction))

        except Exception:
            print('Table {} does not exist\n'.format(fraction))

        self.conn.commit()

        self.cur.close()
        self.conn.close()

    def show_fractions(self):

        self.cur.execute(self.sql)

        row = self.cur.fetchone()

        while row is not None:
            print(row[0])
            row = self.cur.fetchone()

    def all_deputies(self):

        self.cur.execute(self.sql)

        fraction = self.cur.fetchone()

        deputies = list()

        while fraction is not None:

            deputies.append('\n' + fraction[0])

            self.sql = "SELECT * FROM {}".format(fraction[0])

            fraction = self.cur.fetchone()

            self.cur.execute(self.sql)

            deputy = self.cur.fetchone()

            while deputy is not None:

                deputies.append(deputy)

                deputy = self.cur.fetchone()

        return deputies

    def rada_biggest_briber(self, bribers):

        for brib in bribers:
            if type(brib) == str:
                bribers.remove(brib)

        money = [int(brib[5]) for brib in bribers]

        money.sort(reverse=True)

        brib = [brib for brib in bribers if int(brib[5]) == money[0]]

        print(brib[0])


