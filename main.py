# класс автотранспорт
class MotorTransport(object):
    def __init__(self, color, year, auto_type):
        self.color = color
        self.year = year
        self.auto_type = auto_type

    # тормозить
    def stop(self):
        print("Pressing the brake pedal")

    # ехать
    def drive(self):
        print('WRRRRRUM!')

ferrari_testarossa = MotorTransport('Red', 1987, 'passenger car')
# жмём на газ и вперёд!
ferrari_testarossa.drive()




class bycycle(object):
    def __init__(self, color, year, auto_type):
        self.color = color
        self.year = year
        self.auto_type = auto_type

    # тормозить
    def stop(self):
        print("Pressing the brake pedal")

    # ехать
    def drive(self):
        print('NIIIIIIUU!')

sport_bike = bycycle('Black', 2020, 'sport bike')
# жмём на газ и вперёд!
sport_bike.drive()
