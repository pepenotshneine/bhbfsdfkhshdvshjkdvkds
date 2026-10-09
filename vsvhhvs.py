class Engine:

 def start(self):
    print("Двигун запущено")

class Car:
   def __init__(self, brand):
     self.brand = brand
     self.engine = Engine()


def drive(self):
    print(f"Автомобіль {self.brand} їде")
    self.engine.start()

car = Car("BMW")
car.drive()
