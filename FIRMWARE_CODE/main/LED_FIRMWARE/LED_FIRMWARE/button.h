extern void UART_transmit(uint8_t data);

#define USER_BUTTON_PIN 2

void button_init()
{
  DDRD &=  ~(1<<USER_BUTTON_PIN); // PB2 GPIO WRITE MODE
}

int wait_time=0;
long reset_cnt=0;
uint8_t button=0;

char button_cnt=0;
void filtered_button()
{
  if((PIND & (1 << PIND2)) != (1 << PIND2))
    button_cnt++;
  if((PIND & (1 << PIND2)) == (1 << PIND2))
    button_cnt--;

  if(button_cnt>100)
  {
    button=1;
    button_cnt=100;
  }
  if(button_cnt<-100)
  {
    button=0;
    button_cnt=-100;
  }
}

uint8_t button_status=0;
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
			UART_transmit('R');
			UART_transmit('e');
			UART_transmit('s');
			UART_transmit('e');
			UART_transmit('t');
			UART_transmit('\r');
			UART_transmit('\n');
            reset_cnt=0;
        }   
    }else
    {
      if(button_status)
      {
        			UART_transmit('P');
        			UART_transmit('r');
        			UART_transmit('e');
        			UART_transmit('s');
        			UART_transmit('s');
        			UART_transmit('\r');
        			UART_transmit('\n');
        button_status=0;
      }
        reset_cnt=0;
    }
}
}
