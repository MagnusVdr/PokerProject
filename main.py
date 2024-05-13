from tkinter import *
from PIL import ImageTk, Image
from header import *


def update_poker_info(level, bb, ante, time):
    poker_info_label.config(text=f"Level: {level} | BB: {bb} | Ante: {ante} | Time: {time}")


def update_timer():
    global minutes, seconds, BB, ante, timer_running
    if timer_running:
        # Decrement the timer
        if seconds > 0:
            seconds -= 1
        elif minutes > 0:
            minutes -= 1
            seconds = 59
        # Format the time string
        time_str = f"{minutes:02d}:{seconds:02d}"
        update_poker_info(level, BB, ante, time_str)
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


def create_gui(root, screen_width, screen_height):
    root.overrideredirect(True)
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    #root.wm_attributes("-topmost", 1)
    pokerTableImage = Image.open("Images/PokerTable.png")
    global pokerTableGUI
    pokerTableGUI = ImageTk.PhotoImage(pokerTableImage)
    labelImage = Label(root, image=pokerTableGUI)
    labelImage.place(x=0, y=0)




def open_config_window():

    BBEntries = []
    anteEntries = []

    config_window = Toplevel(root)
    config_window.title("Poker Level Configuration")

    # Create entry fields for configuration
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

    Button(config_window, text="Save", command=lambda: save_config(time_entry, BBEntries, anteEntries)).grid(row=21, columnspan=2)


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


# Initialize timer variables
minutes = 10  # Set the initial minutes here
seconds = 0

level = 1
timer_running = False
BBLevelValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
anteLevelValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

read_config()
BB = BBLevelValues[0]
ante = anteLevelValues[0]

# Create GUI
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

create_gui(root, screen_width, screen_height)

# Button for the config window
config_button = Button(root, text="Open Config Window", command=open_config_window, width=20, height=3)
config_button.place(x=0, y=0)

# Label for BB, ante, timer
poker_info_label = Label(root, text=f"Level: {level} | BB: {BB} | Ante: {ante} | Time: 00:00", font=("Arial", 14), bg="white", fg="black")
poker_info_label.place(relx=0.95, rely=0.05, anchor="ne")

# Buttons for start and pause
start_button = Button(root, text="Start", command=start_timer, width=10, height=2)
start_button.place(x=1600, y=900)

pause_button = Button(root, text="Pause", command=pause_timer, width=10, height=2)
pause_button.place(x=1600, y=940)

update_timer()

# Start GUI main loop
root.mainloop()
