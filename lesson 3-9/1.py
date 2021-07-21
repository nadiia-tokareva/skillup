class Device:
    def __init__(self, name= None, brand= None, power = 0):
        self.name = name
        self.brand = brand
        self.power = power
        self.work = ''

    def __str__(self):
        return f'The {self.name}, {self.brand} has a power of {self.power} watts'

    def work_check(self):
        return self.work
    
class CoffeeMashine(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.work = 'Device is working correctly'

    def description(self):
        return 'I am a Coffee machine, I can make a coffee'

class Blender(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.work = 'Sorry, device is not working correctly. We change it.'

    def description(self):
        return 'I am a blender, I can make coctails'

    
class MeatGrinder(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.work = 'Device is working correctly'

    def description(self):
        return 'I am a meat grinder, I am a dood helper!'
    

coffee_mashine = CoffeeMashine(name='coffee machine' , brand= 'Bosh', power = 1700)
blender = Blender(name='blender' , brand= 'Braun', power = 1300)
meat_grinder = MeatGrinder(name='meat grinder', brand= 'Zelmer', power = 1900)

print(coffee_mashine)
print(coffee_mashine.description())
print(coffee_mashine.work_check())

print(blender)
print(blender.description())
print(blender.work_check())

print(meat_grinder)
print(meat_grinder.description())
print(meat_grinder.work_check())

