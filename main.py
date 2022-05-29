import time
import keyboard as kb

import features
import globals as g
from offsets import signatures
from utility import prefix

def main():
    print(prefix() + 'Everything is alright I guess. Gotta do stuff now...')

    while True:
        is_connected = g.game.read_int(g.client_state + signatures.dwClientState_State) == 6
        if not is_connected:
            time.sleep(0.05)
            continue

        features.glow_esp.run()
        features.no_flash.run()
        features.radar.run()

        if kb.is_pressed('end'):
            break


if __name__ == '__main__':
    main()