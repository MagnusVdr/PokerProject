from tkinter import *
from PIL import ImageTk, Image
import platform

from header import *
#from smbus2 import SMBus


def add_players():
    for i in range(1, 10):
        player = Player(player_addresses[i], root, i + 1, cords[i][0], cords[i][1], cords[i][2], cords[i][3],
                        cords[i][4], cords[i][5], cords[i][6], cords[i][7], cords[i][8], cords[i][9])
        player.place_widgets()


def scan_i2c_devices():
    for i in range(10):
        try:
            bus.read_byte(player_addresses[i])
            devices.append(i)
            print("device" + str(i) + "found")
        except IOError:
            pass


def initialize_players():
    for i in devices:
        player = Player(player_addresses[i], root, i + 1, cords[i][0], cords[i][1], cords[i][2], cords[i][3], cords[i][4],
                                                cords[i][5], cords[i][6], cords[i][7], cords[i][8], cords[i][9])
        player.place_widgets()
        players.append(player)


def read_i2c():
    for player in players:
        data_received = []
        data_received = bus.read_i2c_block_data(player.address, 6, 6)
        print(data_received)
        player.update_player_info(hand=[data_received[1], data_received[2]],
                                  stack=(data_received[3] << 8) | data_received[4])


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
    global minutes, seconds, BB, ante, timer_running
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


def pause_timer():
    global timer_running
    timer_running = False


def create_gui():
    global screen_width, screen_height
    root.geometry(f"{screen_width}x{screen_height}")
    root.state('zoomed')

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
                             font=("Arial", 14), bg="white", fg="black")
    poker_info_label.place(relx=0.95, rely=0.05, anchor="ne")

    # Buttons for start and pause
    start_button = Button(root, text="Start", command=start_timer, width=10, height=2)
    start_button.place(x=1600, y=900)

    pause_button = Button(root, text="Pause", command=pause_timer, width=10, height=2)
    pause_button.place(x=1600, y=940)

    close_button = Button(root, text="Close Application", command=root.quit)
    close_button.place(x=1600, y=980)


def open_config_window():

    BBEntries = []
    anteEntries = []

    config_window = Toplevel(root)
    config_window.title("Poker Level Configuration")
    config_window.wm_attributes("-topmost", 1)

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
    global minutes, BB, ante
    minutes = int(time_entry.get())
    BB = int(bb_entries[0].get())
    ante = int(ante_entries[0].get())
    for i in range(10):
        BBLevelValues[i] = int(bb_entries[i].get())
        anteLevelValues[i] = int(ante_entries[i].get())

    with open('config.txt', 'w') as file:
        file.write(f"Level time in minutes: {minutes}\n")
        for i in range(10):
            file.write(f"Level {i + 1} BB: {BBLevelValues[i]}\n")
            file.write(f"Level {i + 1} ante: {anteLevelValues[i]}\n")


def read_config():
    global minutes, BB, ante, BBLevelValues, anteLevelValues
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


try:
    pass
    #bus = SMBus(1)
except FileNotFoundError:
    print("I2C bus not found.")
# Initialize timer variables
minutes = 0  # Set the initial minutes here
seconds = 0
timer_running = False
level = 0
devices = []
players = []

BBLevelValues = [1] * 10
anteLevelValues = [1] * 10
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def setup():
    read_config()
    create_gui()
    update_timer()
    #scan_i2c_devices()
    initialize_players()
    add_players()


def loop():
    #read_i2c()
    update_info()
    root.after(100, loop)


setup()
loop()

# Start GUI main loop
root.mainloop()
