extern bool BOOT_DONE;
extern int BOOT_LED_COLOR;

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
          }
          mode=header1;
        break;
        default:
          mode=header1;
      }
      
    }
  
}