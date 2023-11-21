extern bool PROCESS_DONE;
extern int BAR_LED_COLOR;
extern int PROCESS_TIME;

extern bool BOOT_DONE;
extern int BOOT_LED_COLOR;
extern void LED_BAR_SETUP(uint8_t red, uint8_t green);

#define header1 0
#define header2 1
#define cmd 2
#define GREEN 0
#define RED 1
#define YELLOW 2

int mode    =   header1;

void CMD()
{
  if(Serial.available()>0)
    {
      unsigned char c = Serial.read();
      switch(mode)
      {
        case header1:
          if(c==0xAA)
          {
            mode++;
          }
          else
            mode=header1;
        break;
        case header2:
          if(c==0x55)
            mode++;
          else
            mode=header1;
        break;
        case cmd:
          if(c==0x00)
          {
            BOOT_DONE=false;
            BOOT_LED_COLOR=GREEN;
          }else if(c==0x01)
          {
            BOOT_DONE=false;
            BOOT_LED_COLOR=RED;
          }else if(c==0x02){
            BOOT_DONE=false;
            BOOT_LED_COLOR=YELLOW;
          }else if(c==0x10){
            LED_BAR_SETUP(0,0);
          }else if(c==0x11){
            LED_BAR_SETUP(0,1);
          }else if(c==0x12){
            LED_BAR_SETUP(0,2);
          }else if(c==0x13){
            LED_BAR_SETUP(0,3);
          }else if(c==0x14){
            LED_BAR_SETUP(0,4);
          }else if(c==0x15){
            LED_BAR_SETUP(0,5);
          }else if(c==0x16){
            LED_BAR_SETUP(0,6);
          }else if(c==0x17){
            LED_BAR_SETUP(0,7);
          }else if(c==0x18){
            LED_BAR_SETUP(0,8);
          }else if(c==0x19){
            LED_BAR_SETUP(0,9);
          }else if(c==0x1A){
            LED_BAR_SETUP(0,10);
          }else if(c==0x1B){
            LED_BAR_SETUP(0,11);
          }else if(c==0x1C){
            LED_BAR_SETUP(0,12);
          }else if(c>=0x20 && c<=0x70){
            // FLASH PROCESS LED BAR
            PROCESS_DONE=false;
            //BAR_LED_COLOR=GREEN;
            PROCESS_TIME=(c-0x20)*10;
          }else if(c==0x71){
            BAR_LED_COLOR=GREEN;
          }else if(c==0x72){
            BAR_LED_COLOR=RED;
          }else if(c==0x73){
            BAR_LED_COLOR=YELLOW;
          }
          mode=header1;
        break;
        default:
          mode=header1;
      }
      
    }
  
}