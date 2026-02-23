from movies import show_movies, select_movie
from booking import Seat, Card
from users import get_user

def show_available_seats():
    import sqlite3
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()

    cursor.execute("SELECT seat_id FROM Seat WHERE taken=0")
    seats = cursor.fetchall()

    print("Available seats:")
    for seat in seats:
        print(seat[0])

    connection.close()
    show_available_seats()
def main():
    name = get_user()

    show_movies()
    movie = select_movie()

    if not movie:
        return

    seat_id = input("Preferred seat number: ")
    seat = Seat(seat_id)

    if not seat.is_free():
        print("Seat is taken!")
        return

    price = seat.get_price()
    print("Price:", price)

    number = input("Your card number: ")
    cvc = input("Your card cvc: ")

    card = Card(number, cvc)

    if card.validate(price):
        seat.occupy()
        print("🎉 Booking successful!")
    else:
        print("❌ Payment failed!")

main()
