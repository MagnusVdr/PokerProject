pokerCards = [
      "CardBorder",
      "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
      "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
      "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
      "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"
    ]
P1N_x = 550
P1N_y = 890
P1P_x = 535
P1P_y = 1035
P1C1_x = 545
P1C1_y = 928
P1C2_x = P1C1_x + 80
P1C2_y = P1C1_y + 110

P2N_x = 235
P2N_y = 725
P2P_x = 220
P2P_y = 870
P2C1_x = 230
P2C1_y = 763
P2C2_x = P1C1_x + 80
P2C2_y = P1C1_y + 110

P3N_x = 160
P3N_y = 440
P3P_x = 145
P3P_y = 590
P3C1_x = 155
P3C1_y = 485
P3C2_x = P1C1_x + 80
P3C2_y = P1C1_y + 110

P4N_x = 250
P4N_y = 110
P4P_x = 235
P4P_y = 260
P4C1_x = 240
P4C1_y = 152
P4C2_x = P1C1_x + 80
P4C2_y = P1C1_y + 110

P5N_x = 660
P5N_y = 0
P5P_x = 645
P5P_y = 145
P5C1_x = 655
P5C1_y = 38
P5C2_x = P1C1_x + 80
P5C2_y = P1C1_y + 110

P6N_x = 1920 - P5N_x - 160
P6N_y = P5N_y
P6P_x = 1920 - P5P_x - 180
P6P_y = P5P_y
P6C1_x = 1920 - P5C1_x - 160
P6C1_y = P5C1_y
P6C2_x = P1C1_x + 80
P6C2_y = P1C1_y + 110

P7N_x = 1920 - P4N_x - 160
P7N_y = P4N_y
P7P_x =  1920 - P4P_x - 180
P7P_y = P4P_y
P7C1_x = 1920 - P4C1_x - 160
P7C1_y = P4C1_y
P7C2_x = P1C1_x + 80
P7C2_y = P1C1_y + 110

P8N_x = 1920 - P3N_x - 160
P8N_y = P3N_y
P8P_x = 1920 - P3P_x - 180
P8P_y = P3P_y
P8C1_x = 1920 - P3C1_x - 160
P8C1_y = P3C1_y
P8C2_x = P1C1_x + 80
P8C2_y = P1C1_y + 110

P9N_x = 1920 - P2N_x - 160
P9N_y = P2N_y
P9P_x = 1920 - P2P_x - 180
P9P_y = P2P_y
P9C1_x = 1920 - P2C1_x - 160
P9C1_y = P2C1_y
P9C2_x = P1C1_x + 80
P9C2_y = P1C1_y + 110

P10N_x = 1920 - P1N_x - 160
P10N_y = P1N_y
P10P_x = 1920 - P1P_x - 180
P10P_y = P1P_y
P10C1_x = 1920 - P1C1_x - 160
P10C1_y = P1C1_y
P10C2_x = P1C1_x + 80
P10C2_y = P1C1_y + 110

players_coordinates = [
    [P1N_x, P1N_y, P1P_x, P1P_y, P1C1_x, P1C1_y, P1C2_x, P1C2_y],
    [P2N_x, P2N_y, P2P_x, P2P_y, P2C1_x, P2C1_y, P2C2_x, P2C2_y],
    [P3N_x, P3N_y, P3P_x, P3P_y, P3C1_x, P3C1_y, P3C2_x, P3C2_y],
    [P4N_x, P4N_y, P4P_x, P4P_y, P4C1_x, P4C1_y, P4C2_x, P4C2_y],
    [P5N_x, P5N_y, P5P_x, P5P_y, P5C1_x, P5C1_y, P5C2_x, P5C2_y],
    [P6N_x, P6N_y, P6P_x, P6P_y, P6C1_x, P6C1_y, P6C2_x, P6C2_y],
    [P7N_x, P7N_y, P7P_x, P7P_y, P7C1_x, P7C1_y, P7C2_x, P7C2_y],
    [P8N_x, P8N_y, P8P_x, P8P_y, P8C1_x, P8C1_y, P8C2_x, P8C2_y],
    [P9N_x, P9N_y, P9P_x, P9P_y, P9C1_x, P9C1_y, P9C2_x, P9C2_y],
    [P10N_x, P10N_y, P10P_x, P10P_y, P10C1_x, P10C1_y, P10C2_x, P10C2_y]
]


players_ID = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


class Player:
    def __init__(self, ID, playerNumber, name_x, name_y, pot_x, pot_y, card1_x, card1_y, card2_x, card2_y):
        self.ID = ID
        self.name = f"Player {playerNumber}"
        self.hand = [0, 0]
        self.pot = 0
        self.name_x = name_x
        self.name_y = name_y
        self.pot_x = pot_x
        self.pot_y = pot_y
        self.card1_x = card1_x
        self.card1_y = card1_y
        self.card2_x = card2_x
        self.card2_y = card2_y


