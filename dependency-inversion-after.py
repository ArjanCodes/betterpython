from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass

class LightBulb(Switchable):
    def turnOn(self):
        print("LightBulb: turned on...")

    def turnOff(self):
        print("LightBulb: turned off...")

class Fan(Switchable):
    def turnOn(self):
        print("Fan: turned on...")

    def turnOff(self):
        print("Fan: turned off...")

class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turnOff()
            self.on = False
        else:
            self.client.turnOn()
            self.on = True

l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()