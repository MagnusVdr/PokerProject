from tkinter import *
from PIL import ImageTk, Image

pokerCards = [
      "CardBorder",
      "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd",
      "Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc",
      "As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks",
      "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh"
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
P1W_y = P1C1_y
P1T_x = P1C1_x + 160
P1T_y = P1C1_y + 72

P2C1_x = 200
P2C1_y = 780
P2C2_x = P2C1_x + 80
P2C2_y = P2C1_y
P2N_x = P2C1_x
P2N_y = 725
P2P_x = P2C1_x
P2P_y = P2C1_y + 112
P2W_x = P2C1_x + 160
P2W_y = P2C1_y
P2T_x = P2C1_x + 160
P2T_y = P2C1_y + 72

P3C1_x = 95
P3C1_y = 485
P3C2_x = P3C1_x + 80
P3C2_y = P3C1_y
P3N_x = P3C1_x
P3N_y = 440
P3P_x = P3C1_x
P3P_y = P3C1_y + 112
P3W_x = P3C1_x + 160
P3W_y = P3C1_y
P3T_x = P3C1_x + 160
P3T_y = P3C1_y + 72

P4C1_x = 240
P4C1_y = 152
P4C2_x = P4C1_x + 80
P4C2_y = P4C1_y
P4N_x = P4C1_x
P4N_y = 110
P4P_x = P4C1_x
P4P_y = P4C1_y + 112
P4W_x = P4C1_x + 160
P4W_y = P4C1_y
P4T_x = P4C1_x + 160
P4T_y = P4C1_y + 72

P5C1_x = 655
P5C1_y = 38
P5C2_x = P5C1_x + 80
P5C2_y = P5C1_y
P5N_x = P5C1_x
P5N_y = 0
P5P_x = P5C1_x
P5P_y = P5C1_y + 112
P5W_x = P5C1_x + 160
P5W_y = P5C1_y
P5T_x = P5C1_x + 160
P5T_y = P5C1_y + 72

P6C1_x = 1920 - P5C1_x - 160
P6C1_y = P5C1_y
P6C2_x = P6C1_x + 80
P6C2_y = P6C1_y
P6N_x = P6C1_x
P6N_y = P5N_y
P6P_x = P6C1_x
P6P_y = P5P_y
P6W_x = P6C1_x + 160
P6W_y = P6C1_y
P6T_x = P6C1_x + 160
P6T_y = P6C1_y + 72

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
P7T_x = P7C1_x + 160
P7T_y = P7C1_y + 72

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
P8T_x = P8C1_x + 160
P8T_y = P8C1_y + 72

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
P9T_x = P9C1_x + 160
P9T_y = P9C1_y + 72

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
P10T_x = P10C1_x + 160
P10T_y = P10C1_y + 72

CMYC3_x = 920
CMYC3_y = 485
CMYC1_x = CMYC3_x - 186
CMYC1_y = CMYC3_y
CMYC2_x = CMYC3_x - 93
CMYC2_y = CMYC3_y
CMYC4_x = CMYC3_x + 93
CMYC4_y = CMYC3_y
CMYC5_x = CMYC3_x + 186
CMYC5_y = CMYC3_y

cords = [
    [P1N_x, P1N_y, P1P_x, P1P_y, P1C1_x, P1C1_y, P1C2_x, P1C2_y, P1W_x, P1W_y, P1T_x, P1T_y],
    [P2N_x, P2N_y, P2P_x, P2P_y, P2C1_x, P2C1_y, P2C2_x, P2C2_y, P2W_x, P2W_y, P2T_x, P2T_y],
    [P3N_x, P3N_y, P3P_x, P3P_y, P3C1_x, P3C1_y, P3C2_x, P3C2_y, P3W_x, P3W_y, P3T_x, P3T_y],
    [P4N_x, P4N_y, P4P_x, P4P_y, P4C1_x, P4C1_y, P4C2_x, P4C2_y, P4W_x, P4W_y, P4T_x, P4T_y],
    [P5N_x, P5N_y, P5P_x, P5P_y, P5C1_x, P5C1_y, P5C2_x, P5C2_y, P5W_x, P5W_y, P5T_x, P5T_y],
    [P6N_x, P6N_y, P6P_x, P6P_y, P6C1_x, P6C1_y, P6C2_x, P6C2_y, P6W_x, P6W_y, P6T_x, P6T_y],
    [P7N_x, P7N_y, P7P_x, P7P_y, P7C1_x, P7C1_y, P7C2_x, P7C2_y, P7W_x, P7W_y, P7T_x, P7T_y],
    [P8N_x, P8N_y, P8P_x, P8P_y, P8C1_x, P8C1_y, P8C2_x, P8C2_y, P8W_x, P8W_y, P8T_x, P8T_y],
    [P9N_x, P9N_y, P9P_x, P9P_y, P9C1_x, P9C1_y, P9C2_x, P9C2_y, P9W_x, P9W_y, P9T_x, P9T_y],
    [P10N_x, P10N_y, P10P_x, P10P_y, P10C1_x, P10C1_y, P10C2_x, P10C2_y, P10W_x, P10W_y, P10T_x, P10T_y]
    ]


player_addresses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


class Player:
    def __init__(self, ID, root, playerNumber, name_x, name_y, stack_x, stack_y, card1_x, card1_y, card2_x, card2_y, win_x, win_y, tie_x, tie_y):
        self.address = ID
        self.root = root
        self.playerNumber = playerNumber
        self.name = f"Player {playerNumber}"
        self.nameLabel = Label(root, text=self.name, font=("Arial", 24), fg="black", bd=0)
        self.hand = [0, 0]
        self.card1Image = Image.open("Images/" + pokerCards[self.hand[0]] + ".png")
        self.card1ImageGui = ImageTk.PhotoImage(self.card1Image)
        self.card1Label = Label(root, image=self.card1ImageGui)
        self.card2Image = Image.open("Images/" + pokerCards[self.hand[1]] + ".png")
        self.card2ImageGui = ImageTk.PhotoImage(self.card2Image)
        self.card2Label = Label(root, image=self.card2ImageGui)
        self.folded = 0
        self.stack = 5000
        self.stackLabel = Label(root, text="stack:" + str(self.stack), font=("Arial", 20), fg="black", bd=0)
        self.winPerc = 0
        self.winPercLabel = Label(root, text="W:" + str(self.winPerc) + "%", font=("Arial", 20), fg="black", bd=0)
        self.tiePerc = 0
        self.tiePercLabel = Label(root, text="T:" + str(self.winPerc) + "%", font=("Arial", 20), fg="black", bd=0)
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
        self.tie_x = tie_x
        self.tie_y = tie_y

    def place_widgets(self):
        self.nameLabel.place(x=self.name_x, y=self.name_y)
        self.stackLabel.place(x=self.stack_x, y=self.stack_y)
        self.winPercLabel.place(x=self.win_x, y=self.win_y)
        self.tiePercLabel.place(x=self.tie_x, y=self.tie_y)
        self.card1Label.place(x=self.card1_x, y=self.card1_y)
        self.card2Label.place(x=self.card2_x, y=self.card2_y)

    def fold_cards(self):
        alpha = 80
        # Create a new image with white background and desired alpha value
        grayed_card1 = Image.new("RGBA", self.card1Image.size, (255, 255, 255, alpha))
        grayed_card2 = Image.new("RGBA", self.card2Image.size, (255, 255, 255, alpha))

        # Composite the original card image onto the new image, preserving transparency
        grayed_card1.paste(self.card1Image, (0, 0), self.card1Image)
        grayed_card2.paste(self.card2Image, (0, 0), self.card2Image)

        # Convert the composite images to grayscale
        grayed_card1_gray = grayed_card1.convert('L')
        grayed_card2_gray = grayed_card2.convert('L')

        # Convert grayscale images back to RGBA, applying the desired alpha value
        grayed_card1_final = grayed_card1_gray.convert('RGBA')
        grayed_card2_final = grayed_card2_gray.convert('RGBA')
        grayed_card1_final.putalpha(alpha)
        grayed_card2_final.putalpha(alpha)

        # Convert images to PhotoImage for display
        self.card1ImageGui = ImageTk.PhotoImage(grayed_card1_final)
        self.card1Label.config(image=self.card1ImageGui)
        self.card2ImageGui = ImageTk.PhotoImage(grayed_card2_final)
        self.card2Label.config(image=self.card2ImageGui)

    def update_player_info(self, name=None, hand=None, stack=None, winPerc=None, tiePerc=None, folded=None):
        if name is not None:
            self.name = name
            self.nameLabel.config(text=self.name)

        if hand is not None:
            self.hand = hand
            if self.folded == 1:
                self.fold_cards()
            else:
                self.card1Image = Image.open("Images/" + pokerCards[self.hand[0]] + ".png")
                self.card1ImageGui = ImageTk.PhotoImage(self.card1Image)
                self.card1Label.config(image=self.card1ImageGui)
                self.card2Image = Image.open("Images/" + pokerCards[self.hand[1]] + ".png")
                self.card2ImageGui = ImageTk.PhotoImage(self.card2Image)
                self.card2Label.config(image=self.card2ImageGui)

        if stack is not None:
            self.stack = stack
            self.stackLabel.config(text="stack:" + str(self.stack))

        if winPerc is not None:
            self.winPerc = winPerc
            self.winPercLabel.config(text="W:" + str(self.winPerc) + "%")

        if tiePerc is not None:
            self.tiePerc = tiePerc
            self.tiePercLabel.config(text="T:" + str(self.tiePerc) + "%")

        if folded is not None:
            if self.folded != folded:
                if folded == 1:
                    self.fold_cards()
                    self.folded = 1
                    self.winPerc = 0
                    self.tiePerc = 0
                else:
                    self.card1Image = Image.open("Images/" + pokerCards[self.hand[0]] + ".png").convert("RGBA")
                    self.card1ImageGui = ImageTk.PhotoImage(self.card1Image)
                    self.card1Label.config(image=self.card1ImageGui)
                    self.card2Image = Image.open("Images/" + pokerCards[self.hand[1]] + ".png").convert("RGBA")
                    self.card2ImageGui = ImageTk.PhotoImage(self.card2Image)
                    self.card2Label.config(image=self.card2ImageGui)
                    self.folded = 0


class Community:
    def __init__(self, ID, root, card1_x, card1_y, card2_x, card2_y, card3_x, card3_y, card4_x, card4_y, card5_x, card5_y):
        self.address = ID
        self.root = root
        self.cards = [0, 0, 0, 0, 0]
        self.card1Image = Image.open("Images/" + pokerCards[self.cards[0]] + ".png")
        self.card1ImageGui = ImageTk.PhotoImage(self.card1Image)
        self.card1Label = Label(root, image=self.card1ImageGui, bd=0)
        self.card2Image = Image.open("Images/" + pokerCards[self.cards[1]] + ".png")
        self.card2ImageGui = ImageTk.PhotoImage(self.card2Image)
        self.card2Label = Label(root, image=self.card2ImageGui, bd=0)
        self.card3Image = Image.open("Images/" + pokerCards[self.cards[2]] + ".png")
        self.card3ImageGui = ImageTk.PhotoImage(self.card3Image)
        self.card3Label = Label(root, image=self.card3ImageGui, bd=0)
        self.card4Image = Image.open("Images/" + pokerCards[self.cards[3]] + ".png")
        self.card4ImageGui = ImageTk.PhotoImage(self.card4Image)
        self.card4Label = Label(root, image=self.card4ImageGui, bd=0)
        self.card5Image = Image.open("Images/" + pokerCards[self.cards[4]] + ".png")
        self.card5ImageGui = ImageTk.PhotoImage(self.card5Image)
        self.card5Label = Label(root, image=self.card5ImageGui, bd=0)
        self.card1_x = card1_x
        self.card1_y = card1_y
        self.card2_x = card2_x
        self.card2_y = card2_y
        self.card3_x = card3_x
        self.card3_y = card3_y
        self.card4_x = card4_x
        self.card4_y = card4_y
        self.card5_x = card5_x
        self.card5_y = card5_y

    def place_widgets(self):
        self.card1Label.place(x=self.card1_x, y=self.card1_y)
        self.card2Label.place(x=self.card2_x, y=self.card2_y)
        self.card3Label.place(x=self.card3_x, y=self.card3_y)
        self.card4Label.place(x=self.card4_x, y=self.card4_y)
        self.card5Label.place(x=self.card5_x, y=self.card5_y)

    def update(self, cards):
        self.cards = cards
        self.card1Image = Image.open("Images/" + pokerCards[self.cards[0]] + ".png")
        self.card1ImageGui = ImageTk.PhotoImage(self.card1Image)
        self.card1Label.config(image=self.card1ImageGui)
        self.card2Image = Image.open("Images/" + pokerCards[self.cards[1]] + ".png")
        self.card2ImageGui = ImageTk.PhotoImage(self.card2Image)
        self.card2Label.config(image=self.card2ImageGui)
        self.card3Image = Image.open("Images/" + pokerCards[self.cards[2]] + ".png")
        self.card3ImageGui = ImageTk.PhotoImage(self.card3Image)
        self.card3Label.config(image=self.card3ImageGui)
        self.card4Image = Image.open("Images/" + pokerCards[self.cards[3]] + ".png")
        self.card4ImageGui = ImageTk.PhotoImage(self.card4Image)
        self.card4Label.config(image=self.card4ImageGui)
        self.card5Image = Image.open("Images/" + pokerCards[self.cards[4]] + ".png")
        self.card5ImageGui = ImageTk.PhotoImage(self.card5Image)
        self.card5Label.config(image=self.card5ImageGui)

