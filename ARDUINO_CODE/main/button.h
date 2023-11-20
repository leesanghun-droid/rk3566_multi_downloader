#define USER_BUTTON_PIN 2

void button_init()
{
  DDRD &=  ~(1<<USER_BUTTON_PIN); // PB2 GPIO WRITE MODE
}

int wait_time=0;
long reset_cnt=0;
bool button=false;

char button_cnt=0;
bool filtered_button()
{
  if((PIND & (1 << PIND2)) != (1 << PIND2))
    button_cnt++;
  if((PIND & (1 << PIND2)) == (1 << PIND2))
    button_cnt--;

  if(button_cnt>100)
  {
    button=true;
    button_cnt=100;
  }
  if(button_cnt<-100)
  {
    button=false;
    button_cnt=-100;
  }
}

bool button_status=false;
void button_read()
{
filtered_button();

wait_time--;
if(wait_time<0)
wait_time=0;

if(wait_time==0)
{
    if (button) 
    {
        button_status=button;
        wait_time=30000;
        reset_cnt++;
        if(reset_cnt>30)
        {
            Serial.println("Reset");
            reset_cnt=0;
        }   
    }else
    {
      if(button_status)
      {
        Serial.println("Press");
        button_status=false;
      }
        reset_cnt=0;
    }
}
}
