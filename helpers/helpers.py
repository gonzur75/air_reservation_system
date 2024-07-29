from pprint import pprint as pp

from flight import Flight
from planes import Boeing737Max, AirBusA380


def printer(passanger, seat, flight_number, airplane):
    text = f'| Passanger: {passanger}. seat: {seat}, {flight_number}/{airplane} |'
    border = f'+{"-" * (len(text) - 2)}+'
    line = f'|{" " * (len(text) - 2)}|'

    frame = '\n'.join([border, line, text, line, border])
    print(frame)


def make_flight():

    boeing = Boeing737Max()
    airbus = AirBusA380()
    f = Flight('BA128', boeing)
    # print(f.get_number())
    # print(f.get_airline())
    # print(f.get_plane())
    f.allocate_passenger('25G', 'Marcin')
    f.allocate_passenger('1A', 'Gabi')
    f.allocate_passenger('1B', 'Hania')
    # f.relocate_passenger('1G', '1A')
    printer('Jarosław K', '12C', 'LO27', 'Cesna')
    pp(f.get_num_empty_seats())
    pp(f.print_cards(printer))
    pp(boeing.get_num_seats())
