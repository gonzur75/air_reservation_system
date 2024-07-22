# IATA codes - BA127. LO123

class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_plane(self):
        return self.airplane.get_name()


class Airplane():  # klasyczny zapis, nowy zapis to syntactic sugar
    def get_num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)


class Boeing737Max(Airplane):
    @staticmethod
    def get_name():
        return "Boeing 737Max"

    def seating_plan(self):
        return range(26), 'ABCDEG'


class AirBusA380(Airplane):
    @staticmethod
    def get_name():
        return "Airbus A370"

    def seating_plan(self):
        return range(50), 'ABCDEGHJK'


boeing = Boeing737Max()
airbus = AirBusA380()
print(airbus.get_num_seats())
f = Flight('BA128', boeing)
print(f.get_number())
print(f.get_airline())
print(f.get_plane())
