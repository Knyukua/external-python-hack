from offsets import signatures, netvars
import globals as g
from entity import Entity

def run():
    local_player = Entity(0)
    if not local_player.exists(): return
    g.game.write_float(local_player._base + netvars.m_flFlashDuration, float(0))