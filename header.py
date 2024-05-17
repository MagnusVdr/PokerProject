from tkinter import *
from PIL import ImageTk, Image

pokerCards = [
      "CardBorder",
      "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
      "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
      "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
      "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"
    ]


P1C1_x = 545
P1C1_y = 928
P1C2_x = P1C1_x + 80
P1C2_y = P1C1_y
P1N_x = P1C1_x
P1N_y = P1C1_y - 39
P1P_x = P1C1_x
P1P_y = P1C1_y + 112
P1W_x = P1C1_x + 160
P1W_y = 1000

P2C1_x = 230
P2C1_y = 763
P2C2_x = P2C1_x + 80
P2C2_y = P2C1_y
P2N_x = P2C1_x
P2N_y = 725
P2P_x = P2C1_x
P2P_y = P2C1_y + 112
P2W_x = P2C1_x + 160
P2W_y = 835

P3C1_x = 95
P3C1_y = 485
P3C2_x = P3C1_x + 80
P3C2_y = P3C1_y
P3N_x = P3C1_x
P3N_y = 440
P3P_x = P3C1_x
P3P_y = P3C1_y + 112
P3W_x = P3C1_x + 160
P3W_y = 555

P4C1_x = 240
P4C1_y = 152
P4C2_x = P4C1_x + 80
P4C2_y = P4C1_y
P4N_x = P4C1_x
P4N_y = 110
P4P_x = P4C1_x
P4P_y = P4C1_y + 112
P4W_x = P4C1_x + 160
P4W_y = 225

P5C1_x = 655
P5C1_y = 38
P5C2_x = P5C1_x + 80
P5C2_y = P5C1_y
P5N_x = P5C1_x
P5N_y = 0
P5P_x = P5C1_x
P5P_y = P5C1_y + 112
P5W_x = P5C1_x + 160
P5W_y = 110

P6C1_x = 1920 - P5C1_x - 160
P6C1_y = P5C1_y
P6C2_x = P6C1_x + 80
P6C2_y = P6C1_y
P6N_x = P6C1_x
P6N_y = P5N_y
P6P_x = P6C1_x
P6P_y = P5P_y
P6W_x = P6C1_x + 160
P6W_y = P5W_y

P7C1_x = 1920 - P4C1_x - 160
P7C1_y = P4C1_y
P7C2_x = P7C1_x + 80
P7C2_y = P7C1_y
P7N_x = P7C1_x
P7N_y = P4N_y
P7P_x = P7C1_x
P7P_y = P4P_y
P7W_x = P7C1_x + 160
P7W_y = P4W_y

P8C1_x = 1920 - P3C1_x - 160
P8C1_y = P3C1_y
P8C2_x = P8C1_x + 80
P8C2_y = P8C1_y
P8N_x = P8C1_x
P8N_y = P3N_y
P8P_x = P8C1_x
P8P_y = P3P_y
P8W_x = P8C1_x + 160
P8W_y = P3W_y

P9C1_x = 1920 - P2C1_x - 160
P9C1_y = P2C1_y
P9C2_x = P9C1_x + 80
P9C2_y = P9C1_y
P9N_x = P9C1_x
P9N_y = P2N_y
P9P_x = P9C1_x
P9P_y = P2P_y
P9W_x = P9C1_x + 160
P9W_y = P2W_y

P10C1_x = 1920 - P1C1_x - 160
P10C1_y = P1C1_y
P10C2_x = P10C1_x + 80
P10C2_y = P10C1_y
P10N_x = P10C1_x
P10N_y = P1N_y
P10P_x = P10C1_x
P10P_y = P1P_y
P10W_x = P10C1_x + 160
P10W_y = P1W_y

cords = [
    [P1N_x, P1N_y, P1P_x, P1P_y, P1C1_x, P1C1_y, P1C2_x, P1C2_y, P1W_x, P1W_y],
    [P2N_x, P2N_y, P2P_x, P2P_y, P2C1_x, P2C1_y, P2C2_x, P2C2_y, P2W_x, P2W_y],
    [P3N_x, P3N_y, P3P_x, P3P_y, P3C1_x, P3C1_y, P3C2_x, P3C2_y, P3W_x, P3W_y],
    [P4N_x, P4N_y, P4P_x, P4P_y, P4C1_x, P4C1_y, P4C2_x, P4C2_y, P4W_x, P4W_y],
    [P5N_x, P5N_y, P5P_x, P5P_y, P5C1_x, P5C1_y, P5C2_x, P5C2_y, P5W_x, P5W_y],
    [P6N_x, P6N_y, P6P_x, P6P_y, P6C1_x, P6C1_y, P6C2_x, P6C2_y, P6W_x, P6W_y],
    [P7N_x, P7N_y, P7P_x, P7P_y, P7C1_x, P7C1_y, P7C2_x, P7C2_y, P7W_x, P7W_y],
    [P8N_x, P8N_y, P8P_x, P8P_y, P8C1_x, P8C1_y, P8C2_x, P8C2_y, P8W_x, P8W_y],
    [P9N_x, P9N_y, P9P_x, P9P_y, P9C1_x, P9C1_y, P9C2_x, P9C2_y, P9W_x, P9W_y],
    [P10N_x, P10N_y, P10P_x, P10P_y, P10C1_x, P10C1_y, P10C2_x, P10C2_y, P10W_x, P10W_y]
]


player_addresses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


class Player:
    def __init__(self, ID, root, playerNumber, name_x, name_y, stack_x, stack_y, card1_x, card1_y, card2_x, card2_y, win_x, win_y):
        self.address = ID
        self.root = root
        self.name = f"Player {playerNumber}"
        self.nameLabel = Label(root, text=self.name, font=("Arial", 24), bg="white", fg="black", bd=0)
        self.hand = [0, 0]
        self.card1Image = Image.open("Images/" + pokerCards[self.hand[0]] + ".png")
        self.card1ImageGui = ImageTk.PhotoImage(self.card1Image)
        self.card1Label = Label(root, image=self.card1ImageGui)
        self.card2Image = Image.open("Images/" + pokerCards[self.hand[1]] + ".png")
        self.card2ImageGui = ImageTk.PhotoImage(self.card2Image)
        self.card2Label = Label(root, image=self.card2ImageGui)
        self.folded = 0
        self.stack = 5000
        self.stackLabel = Label(root, text="stack:" + str(self.stack), font=("Arial", 24), bg="white", fg="black", bd=0)
        self.winPerc = 0
        self.winPercLabel = Label(root, text=str(self.winPerc) + "%", font=("Arial", 24), bg="white", fg="black", bd=0)
        self.name_x = name_x
        self.name_y = name_y
        self.stack_x = stack_x
        self.stack_y = stack_y
        self.card1_x = card1_x
        self.card1_y = card1_y
        self.card2_x = card2_x
        self.card2_y = card2_y
        self.win_x = win_x
        self.win_y = win_y

    def place_widgets(self):
        self.nameLabel.place(x=self.name_x, y=self.name_y)
        self.stackLabel.place(x=self.stack_x, y=self.stack_y)
        self.winPercLabel.place(x=self.win_x, y=self.win_y)
        self.card1Label.place(x=self.card1_x, y=self.card1_y)
        self.card2Label.place(x=self.card2_x, y=self.card2_y)

    def update_player_info(self, name=None, hand=None, stack=None, winPerc=None):
        if name is not None:
            self.name = name
            self.nameLabel.config(text=self.name)

        if hand is not None:
            self.hand = hand
            self.card1Image = Image.open("Images/" + pokerCards[self.hand[0]] + ".png")
            self.card1ImageGui = ImageTk.PhotoImage(self.card1Image)
            self.card1Label.config(image=self.card1ImageGui)
            self.card2Image = Image.open("Images/" + pokerCards[self.hand[1]] + ".png")
            self.card2ImageGui = ImageTk.PhotoImage(self.card2Image)
            self.card2Label.config(image=self.card2ImageGui)

        if stack is not None:
            self.stack = stack
            print(f"Stack in player: {stack}");
            self.stackLabel.config(text="stack:" + str(self.stack))

        if winPerc is not None:
            self.winPerc = winPerc
            self.winPercLabel.config(text=str(self.winPerc))
