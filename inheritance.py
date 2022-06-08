#inheritance

class Vehicle:

    # wheels = 2
    # load = 120
    name = "Generic Vehicle"

    def __init__(self, wheels:int, load:int):
        self.wheels = wheels
        # self.name = name
        self.load = load
        # self.load(self)

    def describe(self):
        print("Name :", self.name)
        print("Wheels :", self.wheels)
        print("Max Load :", str(self.load) + ' KGs')




class Car(Vehicle):
    name = "Car"
    model = "Generic 4 Wheeler"
    def __init__(self, passengers):
        super().__init__(4, passengers * 85)
        self.passengers = passengers
        self.speed = 100

    def describe(self):
        super().describe()
        print("Model :", self.model)

        print("Passengers :", self.passengers)
        print("Max Speed :", str(self.speed) + ' MPH')

class Mustang(Car):

    def __init__(self, passengers):
        super().__init__(passengers)
        self.__maker = "Ford"
        self.model = "Mustang GT"
        self.load = 800
        self.speed = 240

    @property
    def maker(self):
        return self.__maker

    @maker.setter
    def maker(self, val):
        self.__maker = val

    @maker.deleter
    def maker(self):
        del self.__maker

    def describe(self):
        print("Maker : ", self.maker)
        super().describe()




if __name__=='__main__':

    mgt = Mustang(2)
    mgt.describe()