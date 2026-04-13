from decimal import Decimal


class Temperature:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return f'{self._temperature}°C'

    @temperature.setter
    def temperature(self, value):
        if not isinstance(value, (int, float, Decimal)):
            raise TypeError(f'Invalid type: {type(value).__name__}')
        if value < - 273.15:
            raise ValueError('too_low')
        self._temperature = value

    @property
    def temperature_f(self):
        return f'{self._temperature * 1.8 + 32} °F'

    @temperature_f.setter
    def temperature_f(self, value):
        self.temperature = (value - 32) * (5 / 9)

    @property
    def temperature_k(self):
        return f'{self._temperature + 273.15}K'

    @temperature_k.setter
    def temperature_k(self, value):
        self.temperature = value - 273.15


t = Temperature(-50)
print(t.temperature)
t.temperature_k = "0"
print(t.temperature)
print(t.temperature_k)
# t._temperature = -65432
# print(vars(t))
# print(dir(t))
# print(t.__dict__)
