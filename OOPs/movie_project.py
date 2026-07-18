"""
Create a class Movie with the following attributes:

Attributes:
- movie_name -> name of the movie (string)
- total_seats -> total number of seats in the movie theater (integer)
- ticket_price -> price of a single ticket (float)
- booked_seats -> number of seats already booked (integer) (starts at 0)

Methods:
- book_ticket(num_tickets) - books the given number of tickets. if enough seats are available, confirm the booking, and show the amount of pay. if not
, show a message that the booking cannot be done due to insufficient seats.
- show_status() - displays movie name, seats available, and seats booked so far.
"""

class Movie:
    def __init__(self, movie_name: str, total_seats: int, ticket_price: float) -> None:
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets: int) -> None:
        if num_tickets <= 0:
            print(f"Invalid number of tickets passed: {num_tickets}")
        elif num_tickets <= (self.total_seats - self.booked_seats):
            self.booked_seats += num_tickets
            amount_to_pay = num_tickets * self.ticket_price
            print(f"Booking confirmed for {num_tickets} tickets. Amount to pay: ${amount_to_pay:.2f}")
        else:
            print("Booking cannot be done due to insufficient seats.")

    def show_status(self) -> None:
        available_seats = self.total_seats - self.booked_seats
        print(f"Movie Name: {self.movie_name}, Seats Available: {available_seats}, Seats Booked: {self.booked_seats}")

# Example usage
movie1 = Movie("Inception", 100, 12.5)
movie1.show_status()
movie1.book_ticket(5)
movie1.show_status()
movie1.book_ticket(200)  # Attempt to book more tickets than available  
