class LightBulb:
    def turnOn(self):
        print("LightBulb: turned on...")

    def turnOff(self):
        print("LightBulb: turned off...")

class ElectricPowerSwitch:

    def __init__(self, l: LightBulb):
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turnOff()
            self.on = False
        else:
            self.lightBulb.turnOn()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()