#define DATA_SIZE 6

#define TFT_DC 46
#define TFT_CS 53
#define TFT_MOSI 51
#define TFT_CLK 52
#define TFT_RST 49
#define TFT_MISO 50
#define TFT_T_CS 48

#define LCD_END_X 320
#define LCD_END_Y 240
#define LCD_ZERO_X 0
#define LCD_ZERO_Y 0

#define SCREEN_REFRESH 1000

#define READ_POWER 1000 //10.00 dBm.

#define TEXT_SIZE_2_HEIGHT 16
#define TEXT_SIZE_2_WIDTH 12

char pokerCards[53][4] = 
{
  "---",
  "A D", "2 D", "3 D", "4 D", "5 D", "6 D", "7 D", "8 D", "9 D", "T D", "J D", "Q D", "K D",
  "A C", "2 C", "3 C", "4 C", "5 C", "6 C", "7 C", "8 C", "9 C", "T C", "J C", "Q C", "K C", 
  "A S", "2 S", "3 S", "4 S", "5 S", "6 S", "7 S", "8 S", "9 S", "T S", "J S", "Q S", "K S",
  "A H", "2 H", "3 H", "4 H", "5 H", "6 H", "7 H", "8 H", "9 H", "T H", "J H", "Q H", "K H"  
};

char playerPositions[3][3] =
{
  "--", "SB", "BB"
};

template<typename T>
struct is_integer {
    static const bool value = false;
};

template<>
struct is_integer<int> {
    static const bool value = true;
};

template<>
struct is_integer<unsigned int> {
    static const bool value = true;
};

template<>
struct is_integer<long> {
    static const bool value = true;
};