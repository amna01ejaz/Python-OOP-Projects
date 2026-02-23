import sqlite3

class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.database = "cinema.db"

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT taken FROM Seat WHERE seat_id=?",
            (self.seat_id,)
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return False

        return row[0] == 0

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT price FROM Seat WHERE seat_id=?",
            (self.seat_id,)
        )

        row = cursor.fetchone()
        connection.close()

        if row:
            return row[0]
        return None

    def occupy(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE Seat SET taken=1 WHERE seat_id=?",
            (self.seat_id,)
        )

        connection.commit()
        connection.close()


class Card:   # ✅ MUST BE OUTSIDE Seat class
    database = "banking.db"

    def __init__(self, number, cvc):
        self.number = number
        self.cvc = cvc

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT balance FROM Card WHERE number=? AND cvc=?",
            (self.number, self.cvc)
        )

        row = cursor.fetchone()

        if row:
            balance = row[0]

            if balance >= price:
                new_balance = balance - price

                cursor.execute(
                    "UPDATE Card SET balance=? WHERE number=? AND cvc=?",
                    (new_balance, self.number, self.cvc)
                )

                connection.commit()
                connection.close()
                return True

        connection.close()
        return False