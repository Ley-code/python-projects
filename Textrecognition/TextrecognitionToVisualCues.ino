

#include "SevSeg.h"
SevSeg sevseg; 

void setup(){
    Serial.begin(9600);
    byte numDigits = 1;
    byte digitPins[] = {};
    byte segmentPins[] = {6, 5, 2, 3, 4, 7, 8, 9};
    bool resistorsOnSegments = true;

    byte hardwareConfig = COMMON_CATHODE; 
    sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments);
    sevseg.setBrightness(90);
}

void loop(){
  String msg = Serial.readString();
  if (msg == "one"){
    sevseg.setNumber(1);
    sevseg.refreshDisplay();
  }    
  else if (msg == "two"){
    sevseg.setNumber(2);
    sevseg.refreshDisplay();
  }    
  else if (msg == "two"){
    sevseg.setNumber(2);
    sevseg.refreshDisplay();
  }    
  else if (msg == "three"){
    sevseg.setNumber(3);
    sevseg.refreshDisplay();
  }    
  else if (msg == "four"){
    sevseg.setNumber(4);
    sevseg.refreshDisplay();
  }    
  else if (msg == "five"){
    sevseg.setNumber(5);
    sevseg.refreshDisplay();
  }    
  else if (msg == "six"){
    sevseg.setNumber(6);
    sevseg.refreshDisplay();
  }    
  else if (msg == "seven"){
    sevseg.setNumber(7);
    sevseg.refreshDisplay();
  }    
  else if (msg == "eight"){
    sevseg.setNumber(8);
    sevseg.refreshDisplay();
  }    
  else if (msg == "nine"){
    sevseg.setNumber(9);
    sevseg.refreshDisplay();
  }
   

  
  
                
}