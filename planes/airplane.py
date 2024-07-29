class Airplane:  # klasyczny zapis to 'class Airplane(object, metaclass=Type) , nowy zapis to syntactic sugar
    def get_num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)
