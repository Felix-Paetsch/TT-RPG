from rpg.utils import create_get_set

class Player:
    def __init__(self, name, sex = None, descr = None):
        self.name = name
        self.sex  = sex
        self.descr = descr


create_get_set(Player, "name")
create_get_set(Player, "sex")
create_get_set(Player, "descr")