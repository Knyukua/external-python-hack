import globals as g

from offsets import signatures, netvars


class Entity:
    def __init__(self, id: int):
        self._base = g.game.read_uint(
            g.client + signatures.dwEntityList + (0x10 * id))

    def exists(self) -> bool:
        return self._base != 0

    def hp(self) -> int:
        return g.game.read_int(self._base + netvars.m_iHealth)

    def is_dormant(self) -> bool:
        return g.game.read_bool(self._base + signatures.m_bDormant)

    def is_alive(self) -> bool:
        return self.hp() > 0

    def is_spotted(self) -> bool:
        return g.game.read_bool(self._base + netvars.m_bSpotted)

    def set_spotted(self, state: bool):
        g.game.write_bool(self._base + netvars.m_bSpotted, state)

    def team(self):
        return g.game.read_int(self._base + netvars.m_iTeamNum)

    def glow_id(self):
        return g.game.read_uint(self._base + netvars.m_iGlowIndex)
