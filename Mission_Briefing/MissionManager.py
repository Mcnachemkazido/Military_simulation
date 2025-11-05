


class MissionManager:
    def __init__(self):
        self.missions = []

    def add_mission(self,mission:"Mission"):
        self.missions.append(mission)

    def sub_mission(self,mission_name):
        for mission in self.missions:
            if mission.mission_name == mission_name:
                self.missions.remove(mission)


