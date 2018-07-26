class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def go(self):
        print('{} поехал'.format(self.name))
    def stop(self):
        print('{} остановился'.format(self.name))
    def turn_right(self):
        print('{} повернул направо'.format(self.name))

    def turn_left(self):
        print('{} повернул налево'.format(self.name))

class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

towncar = TownCar(80, 'red', 'Городской автомобиль', 0)
sportcar = SportCar(180, 'brown', 'Спортивный атвомобиль', 0)
workcar = WorkCar(150, 'green', 'Рабочий автомобиль', 0)
policecar = PoliceCar(150, 'white and blue', 'Полицейский автомобиль', 1)
policecar.go()
towncar.turn_right()
sportcar.turn_left()
workcar.stop()



