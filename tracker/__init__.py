from character import Character, PlayerCharacter, NPCCharacter
from typing import List
import os

class Tracker:
    queue: List[Character]
    turn: int = 0
    def __init__(self, char_names, npc_names):
        self.queue = []
        for name, level in char_names:
            self.queue.append(PlayerCharacter(name, level))
        for name, alignment in npc_names:
            self.queue.append(NPCCharacter(name, alignment))

    def list_characters(self):
        for i, ch in enumerate(self.queue):
            print(f"<{i}> {ch}")
 
    def sort(self):
        self.queue = sorted(self.queue, key=lambda x: x.init)

    def help(self):
        print("[i {idx} {value}] - set init") 
        print("[h {idx} {value}] - set HP") 
        print("[d {idx}] - delete") 
        print("[s] - sort") 
        input(" go back to tracker →")

    def run(self):
    
        while True:
            os.system("clear")

            print(f"# Round {self.turn // len(self.queue)} #")
            self.list_characters()
            print("\n[?] - help")
            inp = input(" -> ")
            
            match inp.split():
                case ["x"]:
                    return
                case ["s"]:
                    self.sort()
                case ["?"]:
                    self.help()
                case ["b"]:
                    self.back()
                case ["h", *args]:
                    if not (len(args) == 2 and args[0].isdigit() and args[1].isdigit()):
                        input("Invalid command!")
                        continue

                    self.queue[int(inp.split()[1])].hp = int(inp.split()[2])
                case ["i", *args]:
                    if not ( len(args) == 2 and args[0].isdigit() and args[1].isdigit()):
                        input("Invalid command!")
                        continue

                    self.queue[int(inp.split()[1])].init = int(inp.split()[2])
                    continue
                
                case ["d", *args]:
                    if not ( len(args) == 1 and args[1].isdigit()):
                        input("Invalid command!")
                        continue

                    self.queue.pop(int(inp.split()[1]))
                
                case other:
                    self.next()

    def next(self):
        self.turn += 1
        buf = self.queue[0]
        self.queue = self.queue[1:]
        self.queue += [buf]

    def back(self):
        self.turn -= 1
        buf = self.queue[-1]
        self.queue = self.queue[:-1]
        self.queue = [buf] + self.queue


