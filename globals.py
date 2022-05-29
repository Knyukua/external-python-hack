import pymem

from utility import prefix
from offsets import signatures

try:
    game = pymem.Pymem('csgo.exe')
except pymem.exception.ProcessNotFound as e:
    print(prefix() + 'CSGO is not launched. Launch it first.')
    exit(0)

client = pymem.process.module_from_name(
    game.process_handle, 'client.dll').lpBaseOfDll
engine = pymem.process.module_from_name(
    game.process_handle, 'engine.dll').lpBaseOfDll
client_state = game.read_uint(engine + signatures.dwClientState)
