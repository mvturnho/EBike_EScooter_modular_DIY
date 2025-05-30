import espnow as ESPNow

# firmware_common/boards_ids.py should be placed on the root path
from firmware_common.boards_ids import BoardsIds

class RearLights(object):

    def __init__(self, _espnow, mac_address, system_data):
        self._espnow = _espnow
        self._peer = ESPNow.Peer(mac=bytes(mac_address), channel=1)
        self._espnow.peers.append(self._peer)
        self._system_data = system_data
        
    def send_data(self):
        if self._espnow is not None:
            try:
                self._espnow.send(
                    f"{int(BoardsIds.REAR_LIGHTS)} \
                    {int(self._system_data.rear_lights_board_pins_state)}",
                    self._peer)

            except Exception as e:
                print(f"RearLights tx error: {e}")
