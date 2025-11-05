from Army_Inventory.Weapon import Weapon
from Army_Inventory.Unit import Infantry,Tanks,Sniper
from Army_Inventory.Soldier import Soldier
from Strike_Options.Tank import Tank
from Strike_Options.Drone import Drone
from Mission_Briefing.Mission import ReconMission,StrikeMission,RescueMission
from Mission_Briefing.Agent import Agent
from Mission_Briefing.MissionManager import MissionManager
from Battle_Simulation.Army import Army

if __name__ == "__main__":
    weapon_1 = Weapon("rove",1)
    weapon_2 = Weapon("akdn", 2)
    weapon_3 = Weapon("rimon",5)
    soldier1 = Soldier("menachem","M",weapon_1)
    soldier2 = Soldier("dni","T",weapon_2)
    soldier3 = Soldier("moshe","T",weapon_3)
    soldier4 = Soldier("dna","M",weapon_1)
    soldier5 = Soldier("yosi","T",weapon_2)
    soldier6 = Soldier("rouvn","T",weapon_3)
    t = Tank("mrcava",100)
    d = Drone("silon",100)
    unit_infantry = Infantry("1919",soldier1,[soldier2,soldier3],[t,d])
    unit_tanks = Tanks("8160", soldier3, [soldier5, soldier6], [t, d])
    unit_shiper = Sniper("1021", soldier6, [soldier4, soldier5], [t, d])

    unit_infantry.briefing()
    for s in unit_infantry.soldier:
        print(s.name)
    unit_shiper.briefing()
    for s in unit_shiper.soldier:
        print(s.name)
    unit_tanks.briefing()
    for s in  unit_tanks.soldier:
        print(s.name)

    a1 = Agent("1234", 10)
    a2 = Agent("11111",5)
    a3 = Agent("888",3)
    m1 = ReconMission("blagn", "sorva", a1, [unit_infantry])
    m1.briefing()
    m2 = StrikeMission("tror","new_eork",a2,[unit_shiper])
    m3 = RescueMission("hill avir","afula",a3,[unit_tanks])

    army = Army([unit_infantry, unit_tanks, unit_shiper])
    army.attack_all()
    print(army.total_attacks)

    mission_manager = MissionManager()
    mission_manager.add_mission(m1)
    mission_manager.add_mission(m2)
    mission_manager.add_mission(m3)
    for mission in mission_manager.missions:
        mission.briefing()










