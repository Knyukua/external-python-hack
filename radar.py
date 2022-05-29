from offsets import signatures, netvars
import globals as g
from entity import Entity

def run():
    local_player = Entity(0)
    for i in range(1, 33):
        ent = Entity(i)
        if not ent.exists(): continue
        if ent.is_dormant() and not ent.is_alive(): continue
        if ent.team() == local_player.team(): continue

        ent.set_spotted(True)