class Swift:
    def start(self):
        print("swift car starts")
    def accelerate(self):
        print("swift car accelarating functionality")
    def breaks(self):
        print("swift car break method")
    def stop(self):
        print("swift car stopping")
class Seltos:
    def start(self):
        print("seltos car starts")
    def accelerate(self):
        print("seltos car accelarating functionality")
    def breaks(self):
        print("seltos car break method")
    def stop(self):
        print("seltos car stopping")
class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()
p=Person()
sw=Swift()
p.drive(sw)