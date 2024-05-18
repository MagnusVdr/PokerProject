from tkinter import *
from PIL import ImageTk, Image
import platform

from header import *
from poker import *


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


def update_win_chance():
    not_folded_players = []
    hands = []
    folded_hands = []
    for player in players:
        if player.folded == 1:
            folded_hands.append([pokerCards[player.hand[0]], pokerCards[player.hand[1]]])
        else:
            hands.append([pokerCards[player.hand[0]], pokerCards[player.hand[1]]])
            not_folded_players.append(player)
    for player in fake_players:
        if player.folded == 1:
            folded_hands.append([pokerCards[player.hand[0]], pokerCards[player.hand[1]]])
        else:
            hands.append([pokerCards[player.hand[0]], pokerCards[player.hand[1]]])
            not_folded_players.append(player)

    community_cards = []
    for card in community.cards:
        if card != 0:
            community_cards.append(pokerCards[card])
        else:
            break

    if (len(community_cards) < 3) or (len(hands) < 2):
        return

    win_chances, tie_chances, _ = calculate_win_percentages(hands, community_cards, folded_hands)

    for i, player in enumerate(not_folded_players):
        player.update_player_info(winPerc=win_chances[i], tiePerc=tie_chances[i])


def simulate_players():
    for i in range(1, 10):
        player = Player(player_addresses[i], root, i + 1, cords[i][0], cords[i][1], cords[i][2], cords[i][3],
                        cords[i][4], cords[i][5], cords[i][6], cords[i][7], cords[i][8], cords[i][9], cords[i][10],
                        cords[i][11])
        player.update_player_info(hand=[i * 3, i * 3 + 1], folded= i % 2)
        player.place_widgets()
        fake_players.append(player)


def scan_i2c_devices():
    if not is_linux:
        return
    for i in range(10):
        try:
            bus.read_byte(player_addresses[i])
            devices.append(i)
        except IOError:
            pass


def initialize_players():
    for i in devices:
        player = Player(player_addresses[i], root, i + 1, cords[i][0], cords[i][1], cords[i][2], cords[i][3],
                        cords[i][4], cords[i][5], cords[i][6], cords[i][7], cords[i][8], cords[i][9], cords[i][10],
                        cords[i][11])
        player.place_widgets()
        players.append(player)


def read_i2c():
    if not is_linux:
        return
    for player in players:
        try:
            data_received = bus.read_i2c_block_data(player.address, 6, 6)
            print(data_received)
            player.update_player_info(hand=[data_received[1], data_received[2]], folded=data_received[3],
                                      stack=(data_received[4] << 8) | data_received[5])
        except OSError as e:
            print(f"Error reading from I2C device at address {player.address}: {e}")


def read_i2c_community():
    if not is_linux:
        return
    try:
        data_received = bus.read_i2c_block_data(community.address, 6, 6)
        community.update(cards=[data_received[1], data_received[2], data_received[3], data_received[4], data_received[5]])
    except OSError as e:
        print(f"Error reading from I2C device at address {community.address}: {e}")


def simulate_community():
    global community
    community = Community(110, root, CMYC1_x, CMYC1_y, CMYC2_x, CMYC2_y, CMYC3_x, CMYC3_y, CMYC4_x, CMYC4_y, CMYC5_x,
                          CMYC5_y)
    community.update(cards=[49, 27, 35, 46, 48])
    community.place_widgets()


def write_i2c():
    for player in players:
        data_to_send = []
        bus.write_i2c_block_data(player.address, 0x00, data_to_send)


def update_info():
    for player in players:
        player.place_widgets()


def update_gui():
    pass


def update_poker_info(time):
    global poker_info_label
    poker_info_label.config(
        text=f"Level: {level} | BB: {BBLevelValues[level]} | Ante: {anteLevelValues[level]} | Time: {time}")


def update_timer():
    global minutes, seconds, timer_running
    if timer_running:
        if seconds > 0:
            seconds -= 1
        elif minutes > 0:
            minutes -= 1
            seconds = 59
        # Format the time string
        time_str = f"{minutes:02d}:{seconds:02d}"
        update_poker_info(time_str)
        # If timer is not zero, continue updating
        if minutes > 0 or seconds > 0:
            root.after(1000, update_timer)
        else:
            timer_running = False


def start_timer():
    global timer_running
    timer_running = True
    update_timer()
    start_button.config(state=DISABLED)  # Disable the start button
    loop()


def pause_timer():
    global timer_running

    if timer_running:
        print("got here")
        timer_running = False
        pause_button.config(text="Continue")
    else:
        timer_running = True
        pause_button.config(text="Pause")
        update_timer()


def create_gui():
    global screen_width, screen_height, start_button, pause_button
    root.geometry(f"{screen_width}x{screen_height}")
    root.after(2000, lambda: root.attributes('-fullscreen', 1))

    pokerTableImage = Image.open("Images/PokerTable.png")
    global pokerTableGUI
    pokerTableGUI = ImageTk.PhotoImage(pokerTableImage)
    labelImage = Label(root, image=pokerTableGUI)
    labelImage.place(x=0, y=0)

    config_button = Button(root, text="Open Config Window", command=open_config_window, width=20, height=3)
    config_button.place(x=0, y=0)

    # Label for BB, ante, timer
    global poker_info_label
    poker_info_label = Label(root,
                             text=f"Level: {level} | BB: {BBLevelValues[level]} | Ante: {anteLevelValues[level]} | Time: 00:00",
                             font=("Arial", 20), fg="black")
    poker_info_label.place(relx=1, rely=0, anchor="ne")

    # Buttons for start and pause
    start_button = Button(root, text="Start", command=start_timer, width=10, height=2)
    start_button.place(x=0, y=60)

    pause_button = Button(root, text="Pause", command=pause_timer, width=10, height=2)
    pause_button.place(x=0, y=100)

    close_button = Button(root, text="Close Application", command=root.quit)
    close_button.place(x=0, y=140)


def open_config_window():

    BBEntries = []
    anteEntries = []

    config_window = Toplevel(root)
    config_window.title("Poker Level Configuration")

    Label(config_window, text="Time between levels (minutes):").grid(row=0, column=0)
    time_entry = Entry(config_window)
    time_entry.grid(row=0, column=1)
    time_entry.insert(0, str(minutes))

    for i in range(10):
        Label(config_window, text=f"Lev {i + 1} BB:").grid(row=i * 2 + 1, column=0)
        entry = Entry(config_window)
        entry.grid(row=i * 2 + 1, column=1)
        entry.insert(0, str(BBLevelValues[i]))
        BBEntries.append(entry)

        Label(config_window, text=f"Lev {i + 1} Ante:").grid(row=i * 2 + 2, column=0)
        entry = Entry(config_window)
        entry.grid(row=i * 2 + 2, column=1)
        entry.insert(0, str(anteLevelValues[i]))
        anteEntries.append(entry)

    Button(config_window, text="Save", command=lambda: save_config(time_entry, BBEntries, anteEntries)).grid(row=21,
                                                                                                             columnspan=2)


def save_config(time_entry, bb_entries, ante_entries):
    global minutes
    minutes = int(time_entry.get())
    for i in range(10):
        BBLevelValues[i] = int(bb_entries[i].get())
        anteLevelValues[i] = int(ante_entries[i].get())

    with open('config.txt', 'w') as file:
        file.write(f"Level time in minutes: {minutes}\n")
        for i in range(10):
            file.write(f"Level {i + 1} BB: {BBLevelValues[i]}\n")
            file.write(f"Level {i + 1} ante: {anteLevelValues[i]}\n")


def read_config():
    global minutes, BBLevelValues, anteLevelValues
    try:
        with open('config.txt', 'r') as file:
            lines = file.readlines()
            # Extracting minutes from the first line
            minutes = int(lines[0].split(': ')[1])
            for i in range(10):
                # Extracting BB and ante values from subsequent lines
                BBLevelValues[i] = int(lines[2*i + 1].split(': ')[1])
                anteLevelValues[i] = int(lines[2*i + 2].split(': ')[1])
    except FileNotFoundError:
        # Default values if config file is not found
        minutes = 10
        BBLevelValues = [1] * 10
        anteLevelValues = [1] * 10


if is_linux:
    try:
        bus = SMBus(1)
    except FileNotFoundError:
        print("I2C bus not found.")
else:
    bus = None
# Initialize timer variables

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

minutes = 0  # Set the initial minutes here
seconds = 0
timer_running = False
level = 0
devices = []
players = []
fake_players = []
global community
BBLevelValues = [1] * 10
anteLevelValues = [1] * 10


def setup():
    read_config()
    create_gui()
    update_timer()
    scan_i2c_devices()
    initialize_players()
    simulate_players()
    simulate_community()


def loop():
    if timer_running:
        read_i2c()
        update_info()
        update_win_chance()
        root.after(1000, loop)


setup()
loop()

# Start GUI main loop
root.mainloop()
