#!/usr/bin/python3

import os

#from tracker import game_tracker
from tracker import Tracker

def get_characters():
    with open("characters.txt", "r") as file:
        return [l.rstrip().split(",") for l in file.readlines()]

def list_characters(chars, indexs):
    for i, ch in enumerate(chars):
        print(f"  {i}. [*] {ch}" if i in indexs else f"  {i}. [ ] {ch}")
    
def pick_characters(chars):
    os.system("clear")

    indexs = []
    while True:
        print("INITIATIVE TRACKER")
        print("# Pick Characters #")

        list_characters(chars, indexs)
        inp = input(" -> ")
        
        if inp in ["x", "n"]:
            break 

        if inp == "*":
            indexs = list(range(0, 100))

        try:
            indexs += [int(i) for i in inp.split()] 
        except ValueError:
            pass
        
        os.system("clear")
        
    return indexs

chars = get_characters()
idx = pick_characters([ch[0] for ch in chars])

chars = [ch for i, ch in enumerate(chars) if i in idx]

print(chars)

tracker = Tracker(
        [ch for ch in chars if ch[1].isdigit()], 
        [ch for ch in chars if not ch[1].isdigit()]
)

tracker.sort()
tracker.run()

#while action != 'exit':
#  print(f"\nCurrent: {game_tracker.get_current()}")
#
#  action = input("Command: ")
#  game_tracker.handle_actions(action)

