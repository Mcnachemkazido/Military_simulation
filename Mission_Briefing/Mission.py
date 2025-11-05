


class Mission:
    def __init__(self,mission_name:str,target:str,assigned_agent:"Agent",unit:list["Unit"]):
        self.mission_name = mission_name
        self.target = target
        self.assigned_agent = assigned_agent
        self.unit = unit

    def briefing(self)->None:
        print(f"mission_name:{self.mission_name}"
              f"\ntarget:{self.target},\n"
              f"assigned_agent:{self.assigned_agent.codename}")


class ReconMission(Mission):
    def attack(self):
        now_missin = self.unit.pop()
        now_missin.attack()

class StrikeMission(Mission):
    def attack(self):
        now_missin = self.unit.pop()
        now_missin.attack()

class RescueMission(Mission):
    def attack(self):
        now_missin = self.unit.pop()
        now_missin.attack()


