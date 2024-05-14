#include "SPI.h"
#include "Adafruit_GFX.h"
#include "Adafruit_ILI9341.h"
#include <string.h>
#include "SparkFun_UHF_RFID_Reader.h" //Library for controlling the M6E Nano module
#include <Wire.h>

#include "player_node.h"

uint16_t currentTextColor = ILI9341_WHITE;
uint16_t currentBackroundColor = ILI9341_BLACK;
uint8_t currentTextSize = 1;

uint16_t BB = 0;
uint16_t lastBB = 0;
uint16_t ante = 0;
uint16_t lastAnte = 0;

/*
uint8_t position = 0;
uint8_t lastPosition = 0;
//*/

uint8_t newLevMin = 10;
uint8_t lastNewLevMin = 0;
uint8_t newLevSec = 0;

uint16_t stack = 0;
uint16_t lastStack = 0;
uint8_t winPerc = 0;
uint8_t lastWinPerc = 0;

Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_MOSI, TFT_CLK, TFT_RST, TFT_MISO);
RFID nano; //Create instance

uint16_t rfidEPC = 0;
uint16_t lastRfidEPC = 0;
uint8_t readCards[2] = {0, 0};
uint8_t savedCards[2] = {0, 0};
uint8_t lastCards[2] = {0, 0};

uint8_t noCards = 0;
uint8_t folded = 0;

uint32_t prevMillis1 = 0;
uint32_t prevMillis2 = 0;
uint32_t prevMillis3 = 0;


void setup() 
{
  Serial.begin(500000);
  Wire.begin(10); // Initialize I2C communication with the specified address
  Wire.onReceive(receiveEvent); // Set up event handler for receiving data
  Wire.onRequest(requestEvent);
  
  set_up_LCD();

  //*
  if (setupNano(115200) == false) //Configure nano to run at 115200bps
  {
    tft.setTextColor(ILI9341_RED);
    tft.setCursor(LCD_ZERO_X + 100, LCD_ZERO_Y + 120);
    tft.print("Nano ERROR");
    while (1); //Freeze!
  }
  nano.startReading();//*/
}

void loop() 
{
  uint32_t currentMillis = millis();
  if(currentMillis - prevMillis1 >= SCREEN_REFRESH)
  {
    update_main_screen();
    prevMillis1 = currentMillis;
  }
  if(currentMillis - prevMillis2 >= SCREEN_REFRESH)
  {
    if(readCards[0] != 0){
      savedCards[0] = readCards[0];
    }
    if(readCards[1] != 0)
    {
      savedCards[1] = readCards[1];
    }
    readCards[0] = 0;
    readCards[1] = 0;
    prevMillis2 = currentMillis;
  }
  if(readCards[0] != 0 || readCards[1] != 0){
    prevMillis3 = currentMillis;
    folded = 0;
  }
  else if((currentMillis - prevMillis3 >= 5000)){
    folded = 1;
  }
  //if(readCards[])
  RFID_loop();
  // put your main code here, to run repeatedly:
}

void receiveEvent(int numBytes) {
  int i = 0;
  byte  received_data[DATA_SIZE];
  while (Wire.available() > 0 && i < DATA_SIZE) {
    // Read the received byte and store it in the array
    received_data[i] = Wire.read();
    i++;
  }
  //1 is update to timer, BB and ante
  if(received_data[0] == 1)
  {
    if(received_data[1] != 255){
      newLevMin = received_data[1];
    }
    BB = (received_data[2] << 8) | received_data[3];
    ante = (received_data[4] << 8) | received_data[5];
  }//2 is update chip sizes
  else if(received_data[0] == 2)
  {

  }//3 is update win%
  else if(received_data[0] == 3){
    winPerc = received_data[1];
  }
}

void requestEvent() {
    byte data_array[6] = {1, savedCards[0], savedCards[1], folded, highByte(stack), lowByte(stack)};
    for (int i = 0; i < 6; i++) 
      Wire.write(data_array[i]);
}


void set_up_LCD()
{
  pinMode(TFT_CS, OUTPUT);//
  pinMode(TFT_T_CS, OUTPUT);//
  digitalWrite(TFT_CS, HIGH);//
  digitalWrite(TFT_T_CS, HIGH);//

  tft.begin();

  tft.setRotation(3);
  set_up_main_screen();
}

void tft_set_text_color_and_track(uint16_t color){
  currentTextColor = color;
  tft.setTextColor(color);
}

void tft_set_backround_color_and_track(uint16_t color){
  currentBackroundColor = color;
  tft.fillScreen(color);
}

void tft_set_text_size_and_track(uint8_t size){
  currentTextSize = size;
  tft.setTextSize(size);
}

template <typename T>
void tft_print(int16_t x, int16_t y, T message)
{
  tft.setCursor(x, y);
  if (is_integer<T>::value) 
  {
    // If message is an integer, convert it to a string using itoa
    char buffer[10];
    itoa(message, buffer, 10); // Convert integer to string
    tft.print(buffer); // Print the string on the TFT screen
  }
  else 
  {
    tft.print(message); // Print the message on the TFT screen
  }
  
}

void set_up_main_screen()
{
  tft_set_backround_color_and_track(ILI9341_BLACK);
  tft_set_text_color_and_track(ILI9341_WHITE);
  tft_set_text_size_and_track(2); //12x16 size
  //Level counter
  ///////////////////////
  tft_print(LCD_ZERO_X, LCD_ZERO_Y, "L:");
  
  tft_print(LCD_ZERO_X + 24, LCD_ZERO_Y, newLevMin);

  tft_print(LCD_ZERO_X + 48, LCD_ZERO_Y, ":");

  tft_print(LCD_ZERO_X + 60, LCD_ZERO_Y, newLevSec);
  //////////////////////
  //BB and ante
  //////////////////////
  tft_print(LCD_END_X - 48, LCD_ZERO_Y, ante);

  tft_print(LCD_END_X - 72, LCD_ZERO_Y, "A:");
  
  tft_print(LCD_END_X - 132, LCD_ZERO_Y, BB);
  
  tft_print(LCD_END_X - 168, LCD_ZERO_Y, "BB:");
  //////////////////////
  //Player position
  //////////////////////
  /*
  tft_print(LCD_ZERO_X, LCD_ZERO_Y + 40, "Position:");

  tft_print(LCD_ZERO_X + 108, LCD_ZERO_Y + 40, playerPositions[position]);//*/
  //////////////////////
  //Player cards
  //////////////////////
  tft_print(LCD_ZERO_X, LCD_ZERO_Y + 80, "Your Cards:");

  tft_print(LCD_ZERO_X + 132, LCD_ZERO_Y + 80, pokerCards[lastCards[0]]);

  tft_print(LCD_ZERO_X + 180, LCD_ZERO_Y + 80, pokerCards[lastCards[1]]);
  //////////////////////
  //Player stack
  //////////////////////
  tft_print(LCD_ZERO_X, LCD_ZERO_Y + 120, "Stack:");

  tft_print(LCD_ZERO_X + 72, LCD_ZERO_Y + 120, stack);
  //////////////////////
  //win % incase of all in
  //////////////////////
  tft_print(LCD_ZERO_X, LCD_ZERO_Y + 160, "win%:");

  tft_print(LCD_ZERO_X + 60, LCD_ZERO_Y + 160, winPerc);
}

void update_main_screen()
{
  if(newLevSec > 0)
  {
    newLevSec--;
    tft.fillRect(LCD_ZERO_X + 60, LCD_ZERO_Y, TEXT_SIZE_2_WIDTH * 2, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_ZERO_X + 60, LCD_ZERO_Y, newLevSec);
  }
  else if(newLevSec == 0 && newLevMin > 0)
  {
    newLevMin--;
    newLevSec = 59;
    tft.fillRect(LCD_ZERO_X + 60, LCD_ZERO_Y, TEXT_SIZE_2_WIDTH * 2, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_ZERO_X + 60, LCD_ZERO_Y, newLevSec);
    tft.fillRect(LCD_ZERO_X + 24, LCD_ZERO_Y, 24, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_ZERO_X + 24, LCD_ZERO_Y, newLevMin);
  }
  
  if(lastNewLevMin != newLevMin){
    
    lastNewLevMin = newLevMin;
  }
  if(lastAnte != ante){
    tft.fillRect(LCD_END_X - 48, LCD_ZERO_Y, TEXT_SIZE_2_WIDTH * 4 ,TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_END_X - 48, LCD_ZERO_Y, ante);
    lastAnte = ante;
  }
  if(lastBB != BB){
    tft.fillRect(LCD_END_X - 132, LCD_ZERO_Y, TEXT_SIZE_2_WIDTH * 2, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_END_X - 132, LCD_ZERO_Y, BB);
    lastBB = BB;
  }
  /*
  if(lastPosition != position){
    tft.fillRect(LCD_ZERO_X + 108, LCD_ZERO_Y + 40, TEXT_SIZE_2_WIDTH * 2, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_ZERO_X + 108, LCD_ZERO_Y + 40, playerPositions[position]);
    lastPosition = position;
  }//*/

  if((savedCards[0] != lastCards[0] && savedCards[0] != lastCards[1]) || (savedCards[1] != lastCards[0] && savedCards[1] != lastCards[1]))
  {
    Serial.print(savedCards[0]);Serial.print("|");Serial.println(savedCards[1]);
    Serial.print(lastCards[0]);Serial.print("|");Serial.println(lastCards[1]);
    tft.fillRect(LCD_ZERO_X + 132, LCD_ZERO_Y + 80, TEXT_SIZE_2_WIDTH * 7, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_ZERO_X + 132, LCD_ZERO_Y + 80, pokerCards[savedCards[0]]);
    tft_print(LCD_ZERO_X + 180, LCD_ZERO_Y + 80, pokerCards[savedCards[1]]);
    lastCards[0] = savedCards[0];
    lastCards[1] = savedCards[1];
  }

  if(lastStack != stack){
    tft.fillRect(LCD_ZERO_X + 72, LCD_ZERO_Y + 120, TEXT_SIZE_2_WIDTH * 5, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_ZERO_X + 72, LCD_ZERO_Y + 120, stack);
    lastStack = stack;
  }
  if(lastWinPerc != winPerc){
    tft.fillRect(LCD_ZERO_X + 60, LCD_ZERO_Y + 160, TEXT_SIZE_2_WIDTH * 3, TEXT_SIZE_2_HEIGHT, currentBackroundColor);
    tft_print(LCD_ZERO_X + 60, LCD_ZERO_Y + 160, winPerc);
    lastWinPerc = winPerc;
  }
}

void RFID_loop()
{
  if (nano.check() == true) //Check to see if any new data has come in from module
  {
    byte responseType = nano.parseResponse(); //Break response into tag ID, RSSI, frequency, and timestamp

    if (responseType == RESPONSE_IS_KEEPALIVE)
    {

    }
    else if (responseType == RESPONSE_IS_TAGFOUND)
    {
      byte tagEPCBytes = nano.getTagEPCBytes(); //Get the number of bytes of EPC from response

      //Print EPC bytes, this is a subsection of bytes from the response/msg array
      
      rfidEPC = 0;
      rfidEPC = nano.msg[31] << 8;
      rfidEPC |= nano.msg[32];
      if(rfidEPC < 53){
        for(int i = 0; i < 2; i++){
          if(readCards[i] == rfidEPC){
            break;
          }else if(readCards[i] == 0){
            readCards[i] = rfidEPC;
            break;
          }else if(i == 1){
            Serial.println("Read third card!");
          }
        }
      }     
    }
    else if (responseType == ERROR_CORRUPT_RESPONSE)
    {
      Serial.println("Bad CRC");
    }
    else
    {
      //Unknown response
      Serial.print("Unknown error");
    }
  }
}

boolean setupNano(long baudRate)
{
  nano.begin(Serial1);
  //Hardware serial
  Serial1.begin(baudRate); //For this test, assume module is already at our desired baud rate
  while(!Serial1);
  nano.setBaud(115200);

  //About 200ms from power on the module will send its firmware version at 115200. We need to ignore this.
  while (Serial1.available()) Serial1.read();

  nano.getVersion();

  if (nano.msg[0] == ERROR_WRONG_OPCODE_RESPONSE)
  {
    //This happens if the baud rate is correct but the module is doing a ccontinuous read
    nano.stopReading();

    Serial.println(F("Module continuously reading. Asking it to stop..."));

    delay(1500);
  }
  else
  {
    //The module did not respond so assume it's just been powered on and communicating at 115200bps
    Serial1.begin(115200); //Start serial at 115200

    nano.setBaud(baudRate); //Tell the module to go to the chosen baud rate. Ignore the response msg

    //softSerial.begin(baudRate); //Start the software serial port, this time at user's chosen baud rate
    Serial1.begin(baudRate); //Start the serial port, this time at user's chosen baud rate

    delay(250);
  }

  //Test the connection
  nano.getVersion();

  if (nano.msg[0] != ALL_GOOD) return (false); //Something is not right

  //The M6E has these settings no matter what
  nano.setTagProtocol(); //Set protocol to GEN2

  nano.setAntennaPort(); //Set TX/RX antenna ports to 1

  nano.setRegion(REGION_EUROPE); //Set to Europe

  nano.setReadPower(READ_POWER); 
  delay(10);

  return (true); //We are ready to rock
}
