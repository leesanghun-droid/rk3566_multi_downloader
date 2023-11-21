#define BUTTON_LED_ON		PORTD |=  (1<<PORTD5)
#define BUTTON_LED_OFF		PORTD &= ~(1<<PORTD5)

extern void UART_transmit(uint8_t data);

void button_init()
{
  DDRD &=  ~(1<<DDD2);	// PD2 GPIO INPUT MODE
  DDRD |=  (1<<DDD5);	// PD5 GPIO OUTPUT MODE
  button_led_off();
}

void button_led_on()
{
	BUTTON_LED_ON;
}

void button_led_off()
{
	BUTTON_LED_OFF;
}

int wait_time=0;
long reset_cnt=0;
uint8_t button=0;

uint8_t button_cnt=128;
void filtered_button()
{
  if((PIND & (1 << PIND2)) != (1 << PIND2))
  {
    button_cnt++;
  }
  if((PIND & (1 << PIND2)) == (1 << PIND2))
  {
    button_cnt--;
  }

  if(button_cnt>228)
  {
    button=1;
    button_cnt=228;
  }
  if(button_cnt<28)
  {
    button=0;
    button_cnt=28;
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
