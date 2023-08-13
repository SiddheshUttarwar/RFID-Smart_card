#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN    9
#define SS_PIN     10

MFRC522 mfrc522(SS_PIN, RST_PIN);

MFRC522::MIFARE_Key Key;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
while(!Serial);
SPI.begin();
mfrc522.PCD_Init();
for(byte i = 0; i < 6; i++)
 Key.keyByte[i] = 0xFF;
Serial.print('>');

}

void loop() {
  // put your main code here, to run repeatedly:
   if ( ! mfrc522.PICC_IsNewCardPresent())
        return;
    if ( ! mfrc522.PICC_ReadCardSerial())
        return;
    send_tag_val(mfrc522.uid.uidByte, mfrc522.uid.size);
    delay(1000);

}

void send_tag_val(byte *buffer, byte bufferSize)

{

    Serial.print("ID:");
    for (byte i = 0; i < bufferSize; i++)
    {
        Serial.print(buffer[i], DEC);
        Serial.print(" ");
    }
    Serial.println(0, DEC);
    Serial.print('>');
}
