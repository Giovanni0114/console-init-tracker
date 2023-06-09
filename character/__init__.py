class Character:
    init: int = 0
    name: str = ""
    hp: int = 0

    def __init__(self, name):
        self.name = name
    
    def set_init(self, init):
        self.init = init

    def set_hp(self, hp):
        self.hp = hp

    def modify_hp(self, value):
        self.hp += value
 

class PlayerCharacter(Character):
    level: int = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f" {self.init}. [{self.hp}] {self.name} lvl.{self.level} " 

class NPCCharacter(Character):
    level: int = 0
    alignment: str = ""

    def __init__(self, name, align):
        self.name = name
        self.alignment = align

    def __repr__(self):
        align = f' <= {self.alignment}' if self.alignment != '' else ''
        return f" {self.init}. [{self.hp}] {self.name} {align}" 


