import platform


class DummySMBus:
    def read_byte(self, addr):
        return 0

    def read_i2c_block_data(self, addr, cmd, length):
        return [0] * length

    def write_i2c_block_data(self, addr, cmd):
        return


is_linux = platform.system() == "Linux"
if is_linux:
    from smbus2 import SMBus
else:
    SMBus = DummySMBus

player_addresses = [18, 20, 30, 40, 50, 60, 70, 80, 90, 100]

"""I2C commands"""
START_TIME = 1
PAUSE_TIME = 2
SET_NEW_TIMER_TIME = 3
""""""""""""""""""""""""


def update_player_node_win_chance(bus, player, win_chance):
    data_to_send = [5, win_chance, win_chance]
    try:
        bus.write_i2c_block_data(player.address, 0x00, data_to_send)
    except OSError:
        pass


def update_player_node_timers(bus, players, cmd, new_time=None):
    if cmd == START_TIME:
        data_to_send = [START_TIME, 0]
    elif cmd == PAUSE_TIME:
        data_to_send = [PAUSE_TIME, 0]
    elif cmd == SET_NEW_TIMER_TIME:
        data_to_send = [SET_NEW_TIMER_TIME, new_time]
    else:
        print("Unknown command")
        return
    for player in players:
        try:
            bus.write_i2c_block_data(player.address, 0x00, data_to_send)
        except OSError:
            pass


def update_player_bb_ante(bus, players, BB, ante):
    data_to_send = [4, (BB >> 8) & 255, BB & 255, (ante >> 8) & 255, ante & 255]
    for player in players:
        try:
            bus.write_i2c_block_data(player.address, 0x00, data_to_send)
        except OSError:
            pass


def simulate_community(community):
    community.update(cards=[49, 1, 35, 0, 0])


def read_i2c_community(bus, community):
    if not is_linux:
        simulate_community(community)
        return
    try:
        data_received = bus.read_i2c_block_data(community.address, 0, 6)
        if any(num > 52 for num in data_received):
            return
        community.update(cards=[data_received[1], data_received[2],
                                data_received[3], data_received[4], data_received[5]])

    except OSError as e:
        simulate_community(community)
        pass
        # print(f"Error reading from I2C device at address {community.address}: {e}")


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

    try:
        pass
    except IOError:
        pass
    return connected_devices


def read_i2c(bus, players):
    if not is_linux:
        return
    for player in players:
        try:
            data_received = bus.read_i2c_block_data(player.address, 6, 6)
            #print(f"read players data:\n{data_received}")
            player.update_player_info(hand=[data_received[1], data_received[2]], folded=data_received[3],
                                      stack=(data_received[4] << 8) | data_received[5])
        except OSError as e:
            pass
            #print(f"Error reading from I2C device at address {player.address}: {e}")


def write_community(bus, community, cmd):
    data_send = []
    if cmd == 2:
        data_send = [cmd, 2]
    elif cmd == 1:
        data_send = [cmd, 1]
    else:
        print("Unknown command")
    try:
        bus.write_i2c_block_data(community.address, 0x00, data_send)
    except OSError as e:
        pass
