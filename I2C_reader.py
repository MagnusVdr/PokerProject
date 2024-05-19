import platform

player_addresses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


class DummySMBus:
    def read_byte(self, addr):
        return 0

    def read_i2c_block_data(self, addr, cmd, length):
        return [0] * length

    def write_i2c_block_data(self, addr, cmd, data):
        pass


is_linux = platform.system() == "Linux"
if is_linux:
    from smbus2 import SMBus
else:
    SMBus = DummySMBus

"""Timer Macros"""
START = 1
PAUSE = 2
SET_NEW_TIME = 3
""""""""""""""""""""""""
"""Node Macros"""
DRAW = 1
DELE = 2
""""""""""""""""""""""""


def update_player_node_timers(bus, players, cmd, new_time=None):
    if cmd == START:
        data_to_send = [START, 0]
    elif cmd == PAUSE:
        data_to_send = [PAUSE, 0]
    elif cmd == SET_NEW_TIME:
        data_to_send = [SET_NEW_TIME, new_time]
    else:
        print("Unknown command")
        return
    for player in players:
        bus.write_i2c_block_data(player.address, 0x00, data_to_send)


def simulate_community(community):
    community.update(cards=[49, 1, 35, 46, 0])
    community.place_widgets()


def read_i2c_community(bus, community):
    if not is_linux:
        simulate_community(community)
        return
    try:
        data_received = bus.read_i2c_block_data(community.address, 6, 6)
        print(data_received)
        for i in range(1, 6):
            if community.cards[i - 1] != data_received[i]:
                community.update(cards=[data_received[1], data_received[2],
                                        data_received[3], data_received[4], data_received[5]])
        community.place_widgets()

    except OSError as e:
        print(f"Error reading from I2C device at address {community.address}: {e}")


def scan_i2c_devices(bus):
    connected_devices = []
    if not is_linux:
        return
    for i in range(10):
        try:
            bus.read_byte(player_addresses[i])
            connected_devices.append(i)
        except IOError:
            pass
    return connected_devices


def read_i2c(bus, players):
    if not is_linux:
        return
    for player in players:
        try:
            data_received = bus.read_i2c_block_data(player.address, 6, 6)
            print(data_received)
            player.update_player_info(hand=[data_received[1], data_received[2]], folded=data_received[3],
                                      stack=(data_received[4] << 8) | data_received[5])
        except OSError as e:
            pass
            #print(f"Error reading from I2C device at address {player.address}: {e}")


def write_community(bus, community, cmd):
    if cmd == DELE:
        bus.write_i2c_block_data(community.address, 0x00, [cmd, 2, 0, 0, 0, 0])
    if cmd == DRAW:
        bus.write_i2c_block_data(community.address, 0x00, [cmd, 1, 0, 0, 0, 0])
    else:
        print("Unknown command")
