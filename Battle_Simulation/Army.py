

class Army:
    total_attacks = 0

    def __init__(self,units:list["Units"],):
        self.units = units

    def attack_all(self):
        for unit in self.units:
            unit.attack()
            Army.total_attacks += 1
