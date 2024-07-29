from planes import Airplane


class Boeing737Max(Airplane):
    @staticmethod
    def get_name():
        return "Boeing 737Max"

    def seating_plan(self):
        return range(1, 26), 'ABCDEG'
