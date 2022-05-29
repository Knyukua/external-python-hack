from offsets import signatures, netvars
import globals as g
from entity import Entity

def run():
    glow_object_manager = g.game.read_uint(g.client + signatures.dwGlowObjectManager)

    local_player = Entity(0)
    for i in range(1, 33):
        ent = Entity(i)
        if not ent.exists(): continue
        if ent.is_dormant() and not ent.is_alive(): continue
        if ent.team() == local_player.team(): continue

        entity_glow_id = ent.glow_id()

        g.game.write_float(glow_object_manager + entity_glow_id * 0x38 + 0x8, float(0))   # R
        g.game.write_float(glow_object_manager + entity_glow_id * 0x38 + 0xC, float(1))   # G
        g.game.write_float(glow_object_manager + entity_glow_id * 0x38 + 0x10, float(1))  # B
        g.game.write_float(glow_object_manager + entity_glow_id * 0x38 + 0x14, float(1))  # Alpha
        g.game.write_bool(glow_object_manager + entity_glow_id * 0x38 + 0x28, True)