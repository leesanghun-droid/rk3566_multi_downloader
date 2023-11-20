#define USER_BUTTON_PIN 2

void button_init()
{
  DDRD &=  ~(1<<USER_BUTTON_PIN); // PB2 GPIO WRITE MODE
}

int wait_time=0;
long reset_cnt=0;

void button_read()
{

wait_time--;
if(wait_time<0)
wait_time=0;

if(wait_time==0)
{
    if ((PIND & (1 << PIND2)) != (1 << PIND2) ) 
    {
        Serial.println("Press");
        wait_time=30000;
        reset_cnt++;
        if(reset_cnt>10)
        {
            Serial.println("Reset");
            reset_cnt=0;
        }   
    }else
    {
        reset_cnt=0;
    }
}

}