#include "SparkFun_UHF_RFID_Reader.h" //Library for controlling the M6E Nano module
#include <Wire.h>

#include "communityr_reader.h"

volatile uint16_t stack = 0;
volatile uint16_t savedStack = 0;
volatile uint16_t lastStack = 0;

RFID nano;
volatile uint16_t rfidEPC = 0;
volatile uint16_t lastRfidEPC = 0;

volatile uint8_t readCards[5] = {0, 0, 0, 0, 0};
volatile uint8_t savedCards[5] = {0, 0, 0, 0, 0};
volatile uint8_t noCards = 0;

volatile uint8_t scan = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(500000);
  Wire.begin(85); // Initialize I2C communication with the specified address
  Wire.onReceive(receiveEvent); // Set up event handler for receiving data
  Wire.onRequest(requestEvent);
  if(setupNano(115200) == false){
    Serial.println("Nano Error");
    while(1);
  }
  nano.startReading();
}

void loop() {
  RFID_loop();
  //debug();
}

void receiveEvent(byte numBytes){
  int i = 0;
  byte  received_data[numBytes];
  while (Wire.available() > 0 && i < numBytes) {
    // Read the received byte and store it in the array
    received_data[i] = Wire.read();
    i++;
  }
  //*
  Serial.println(numBytes);
  Serial.println("data");
  for(uint8_t j = 0; j < numBytes; j++){
    Serial.print(received_data[j]);
    Serial.print("|");
  }//*/
  Serial.println(" ");
  if(numBytes > 1){
    //2 is everyone folded, new game
    if(received_data[1] == 2)
    {
      Serial.println("Folded");
      for(uint8_t i = 0; i < 5; i++){
        readCards[i] = 0;
      }
      scan = 0;
    }//1 is everyone has their cards, can start scanning for community cards
    else if(received_data[1] == 1)
    {
      Serial.println("Draw");
      scan = 1;
    }
  }
}

void requestEvent(){
  byte data_array[6] = {1, readCards[0], readCards[1], readCards[2], readCards[3], readCards[4]};
  Serial.println("request");
  for(uint8_t i = 0; i < 6; i++){
    Wire.write(data_array[i]);
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

      if(rfidEPC < 53)
      {
        for(uint8_t i = 0; i < 5; i++)
        {
          //Serial.println("rfidEPC:");
          //Serial.println(rfidEPC);
          if(readCards[i] == rfidEPC){

            break;
          }
          else if(readCards[i] == 0)
          {
            readCards[i] = rfidEPC;
            break;
          }
        }
      }
    }
    else if (responseType == ERROR_CORRUPT_RESPONSE)
    {

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

void debug(){
  Serial.println("ReadCard:");
  Serial.print(pokerCards[readCards[0]]);
  Serial.print("|");
  Serial.print(pokerCards[readCards[1]]);
  Serial.print("|");
  Serial.print(pokerCards[readCards[2]]);
  Serial.print("|");
  Serial.print(pokerCards[readCards[3]]);
  Serial.print("|");
  Serial.println(pokerCards[readCards[4]]);
}