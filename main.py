import tkinter as tk
import threading
import time

i = 0


def update_gui():
    # Update GUI elements here based on your data
    # For example:
    global i
    label.config(text="Updated: " + str(i))
    # Repeat this for all elements you want to update


def loop():
    while True:
        # Your main loop logic goes here
        # For example, updating data or reading sensors
        # For demonstration, sleep for a second
        time.sleep(1)
        global i
        i += 1
        # Call the function to update the GUI
        update_gui()


# Create GUI
root = tk.Tk()
label = tk.Label(root, text="Initial Value")
label.pack()

# Start loop in a separate thread
thread = threading.Thread(target=loop)
thread.daemon = True  # Daemonize thread so it dies when main program exits
thread.start()

# Start GUI main loop
root.mainloop()
