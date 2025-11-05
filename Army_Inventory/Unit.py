from abc import ABC ,abstractmethod

class Unit(ABC):
    def __init__(self,unit_name:str,commander:"Soldier"
                 ,soldier:list["Soldier"],
                 strike_option:list["StrikeOption"] ):

        self.unit_name = unit_name
        self.commander = commander
        self.soldier = soldier
        self.strike_option =  strike_option

    def briefing(self):
        print(f"unit_name:{self.unit_name}, commander:{self.commander.name}")

    @abstractmethod
    def attack(self):
        pass



class Infantry(Unit):
    def attack(self):
        print("Infantry attack")

class Tanks(Unit):
    def attack(self):
        print("Tanks attack")

class Sniper(Unit):
    def attack(self):
        print("Sniper attack")
