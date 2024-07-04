class Temp:
    def __init__(self, _temperature, _unit = 'c'):
        self.__temperature = _temperature
        self.__unit = _unit

    def __str__(self):
        return "{}{}".format(self.__temperature, self.__unit)

    def set_temperature(self, newTemperature):
        self.__temperature = newTemperature

    def setUnit(self, newUnit):
        if newUnit == 'c' or newUnit == 'f':
            self.__unit = newUnit
        else:
            raise Exception("unit must be 'c' or 'f'")

    def get_temperature(self):
        return self.__temperature

    def to_fahrenheit(self):
        if self.__unit == 'f':
            return self.__temperature
        elif self.__unit == 'c':
            return self.__temperature*9/5 +32
        else:
            return("unit must be 'c' or 'f'")

    def to_celsius(self):
        if self.__unit == 'c':
            return self.__temperature
        elif self.__unit == 'f':
            return (self.__temperature-32)*5/9
        else:
            return("unit must be 'c' or 'f'")

    @property
    def Unit(self):
        return self.__unit

    @Unit.setter
    def Unit(self, new_unit):
        self.__unit = new_unit

    @property
    def Temperature(self):
        return self.__temperature

    @Temperature.setter
    def Temperature(self, new_temperature):
        self.__temperature = new_temperature

    @property
    def Celsius(self):
        if self.__unit == 'c':
            return self.__temperature
        elif self.__unit == 'f':
            return (self.__temperature-32)*5/9
        else:
            return("unit must be 'c' or 'f'")
        

    @property
    def Fahrenheit(self):
        if self.__unit == 'f':
            return self.__temperature
        elif self.__unit == 'c':
            return self.__temperature*9/5 +32
        else:
            return("unit must be 'c' or 'f'")
        
