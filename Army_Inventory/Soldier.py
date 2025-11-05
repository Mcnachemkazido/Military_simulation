

class Soldier:
    def __init__(self,name:str,rank:str,weapon:"Weapon"):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def report(self)->None:
        print(f"name:{self.name}, rank:{self.rank}, weapon:{self.weapon.name}")
