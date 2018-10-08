/*
 * LiquidCrystal Library
 * 
 * This code is meant to integrate with the raspberry pi over a serial connection.
 * 
 * It first prints a welcome message before listening in on the serial connection.
 */

// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Welcome Messages
String line1 = "Welcome! :)";
String line2 = "Proj BandWith";

// put your setup code here, to run once:
void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialise the serial port and its baud rate.
  Serial.begin(9600);

  // print welcome message
  lcd.print(line1);
  lcd.setCursor(0, 1); // set cursor to col 0, row 1.
  lcd.print(line2);  
}

// put your main code here, to run repeatedly:
void loop() {
  // if there are input available in the arduino serial port
  if(Serial.available()) {

    // clear the LCD Screen and position cursor in top left
    lcd.clear();
    line1 = line2; // shuffle up
    line2 = Serial.readString(); // read string from serial to line2
    lcd.print(line1);
    lcd.setCursor(0, 1);
    lcd.print(line2); 
    
  }

}
