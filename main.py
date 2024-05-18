from header import *
from poker import *
from I2C_reader import *


def set_up_debug():
    def toggle_fold(player):
        player.update_player_info(folded=not player.folded)
        print(f"{player.name} folded: {player.folded}")

    def open_debug_window():
        debug_window = Toplevel(players[0].root)
        debug_window.title("Debug Window")

        for player in players:
            btn = Button(
                debug_window,
                text=f"Toggle {player.name} Fold",
                command=lambda p=player: toggle_fold(p)
            )
            btn.pack(pady=5)

    debug_button = Button(players[0].root, text="Open Debug Window", command=open_debug_window)
    debug_button.pack(pady=20)


def update_win_chance():
    not_folded_players = []
    hands = []
    folded_hands = []
    for player in players:
        if player.hand[0] == 0 or player.hand[1] == 0:
            continue
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
    if last_win_chances == win_chances:
        return
    for i, player in enumerate(not_folded_players):
        player.update_player_info(winPerc=win_chances[i], tiePerc=tie_chances[i])


def simulate_players():
    for i in range(1, 10):
        player = Player(player_addresses[i], root, i + 1, cords[i][0], cords[i][1], cords[i][2], cords[i][3],
                        cords[i][4], cords[i][5], cords[i][6], cords[i][7], cords[i][8], cords[i][9], cords[i][10],
                        cords[i][11])
        player.update_player_info(hand=[i * 3, i * 3 + 1], folded= i % 2)
        player.place_widgets()
        players.append(player)


def initialize_players(devices):
    for i in devices:
        player = Player(player_addresses[i], root, i + 1, cords[i][0], cords[i][1], cords[i][2], cords[i][3],
                        cords[i][4], cords[i][5], cords[i][6], cords[i][7], cords[i][8], cords[i][9], cords[i][10],
                        cords[i][11])
        player.place_widgets()
        players.append(player)


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


def keep_game_state(players, community, bus):
    global all_folded
    folds = 0
    un_folds = 0
    if all_folded == 1:
        for player in players:
            if player.folded == 1:
                un_folds += 1
        if un_folds == len(players):
            all_folded = 0
            write_community(bus, community, DRAW)
    else:
        for player in players:
            if player.folded == 1:
                folds += 1
        print("folds:")
        print(folds)
        if folds == len(players):
            all_folded = 1
            write_community(bus, community, DELETE)


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
players = []
BBLevelValues = [1] * 10
anteLevelValues = [1] * 10
community = None
all_folded = 1
last_win_chances = []


def setup():
    global community
    read_config()
    create_gui()
    update_timer()
    devices = scan_i2c_devices(bus)
    community = Community(110, root, CMYC1_x, CMYC1_y, CMYC2_x, CMYC2_y, CMYC3_x, CMYC3_y, CMYC4_x, CMYC4_y, CMYC5_x,
                          CMYC5_y)
    if is_linux:
        initialize_players(devices)
    else:
        simulate_community(community)
    simulate_players()


def loop():
    if timer_running:
        read_i2c(bus, players)
        read_i2c_community(bus, community)
        keep_game_state(players, community, bus)
        update_win_chance()
        root.after(1000, loop)


setup()
set_up_debug()
loop()

# Start GUI main loop
root.mainloop()
