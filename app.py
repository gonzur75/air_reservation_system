from pprint import pprint as pp


# IATA codes - BA127. LO123

class Flight:  # napisane Pascalcasem
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

        rows, letters = self.airplane.seating_plan()
        self.seats = [None] + [{letter: None for letter in letters} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_plane(self):
        return self.airplane.get_name()

    def _parse_seats(self, seat='12C'):
        rows, letters = self.airplane.seating_plan()

        letter = seat[-1]
        if letter not in letters:
            raise ValueError(f'Invalid seat letter: {letter}')

        row_text = seat[:-1]
        try:
            row = int(row_text)

        except ValueError:
            raise ValueError(f'Invalid row number: {row_text}')

        if row not in rows:
            raise ValueError(f' Row:{row} not in range')
        return row, letter

    def allocate_passenger(self, seat, passenger):
        row, letter = self._parse_seats(seat)

        if self.seats[row][letter] is not None:
            raise ValueError(f'Seat {seat} is already taken')

        self.seats[row][letter] = passenger

    def relocate_passenger(self, old_seat, new_seat):
        old_row, old_letter = self._parse_seats(old_seat)

        if self.seats[old_row][old_letter] is None:
            raise ValueError(f'Old seat is empty : {old_seat}')

        new_row, new_letter = self._parse_seats(new_seat)

        if self.seats[new_row][new_letter] is not None:
            raise ValueError(f'New seat {new_seat} is already taken')

        self.seats[new_row][new_letter] = self.seats[old_row][old_letter]
        self.seats[old_row][old_letter] = None

    def get_num_empty_seats(self):
        return sum(sum(1 for passenger in row.values() if passenger is None) for row in self.seats if row is not None)

        # empty_seats = 0
        #
        # for row in self.seats:
        #     if row is not None:
        #         for seat in row.values():
        #             if seat is None:
        #                 empty_seats += 1
        #
        # return empty_seats

        # return sum([len([seat for seat in row.values() if seat is None]) for row in self.seats if row is not None])

    def _get_passengers(self):
        rows, letters = self.airplane.seating_plan()

        for row in rows:
            for letter in letters:
                if self.seats[row][letter] is not None:
                    yield f'{row}{letter}'

    def print_cards(self, card_printer):
        for seat, passenger in self._get_passengers():
            card_printer(passenger, seat, self.flight_number, self.get_plane())


class Airplane:  # klasyczny zapis to 'class Airplane(object, metaclass=Type) , nowy zapis to syntactic sugar
    def get_num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)


class Boeing737Max(Airplane):
    @staticmethod
    def get_name():
        return "Boeing 737Max"

    def seating_plan(self):
        return range(1, 26), 'ABCDEG'


class AirBusA380(Airplane):
    @staticmethod
    def get_name():
        return "Airbus A370"

    def seating_plan(self):
        return range(1, 51), 'ABCDEGHJK'


def printer(passanger, seat, flight_number, airplane):
    text = f'| Passanger: {passanger}. seat: {seat}, {flight_number}/{airplane} |'
    border = f'+{"-" * (len(text) - 2)}+'
    line = f'|{" " * (len(text) - 2)}|'

    frame = '\n'.join([border, line, text, line, border])
    print(frame)


printer('Jarosław K', '12C', 'LO27', 'Cesna')

boeing = Boeing737Max()
airbus = AirBusA380()
print(airbus.get_num_seats())
f = Flight('BA128', boeing)
# print(f.get_number())
# print(f.get_airline())
# print(f.get_plane())
f.allocate_passenger('25G', 'Marcin')
f.allocate_passenger('1A', 'Gabi')
f.allocate_passenger('1B', 'Hania')
# f.relocate_passenger('1G', '1A')

pp(f.get_num_empty_seats())
pp(f.print_cards(printer))
pp(boeing.get_num_seats())
