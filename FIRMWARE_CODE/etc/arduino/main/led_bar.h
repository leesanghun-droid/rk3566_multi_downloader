#define ABCD 0
#define EFGH 1
#define IJKL 2

#define RED 0
#define GREEN 1
int cycle_wait=0;
int position_select=ABCD; // 0=ABCD, 1=EFGH, 2=IJKL
bool LED_CHANGE=false;

uint8_t LED_BAR_ARRAY[12][2]={
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0},
  {0,0}};


void HC595_send_byte(uint8_t data)
{
	uint8_t temp1	=	0;
	uint8_t i		=	0;
	
	for(i=0;i<8;i++)
	{
		CLK_LOW;
		temp1=data & 0b00000001;
		if(temp1)
		DATA_HIGH;
		else
		DATA_LOW;
		CLK_HIGH;
		data= data >> 1;
	}
	CLK_LOW;
	_delay_loop_1(1);
}

void HC595_init()
{
		DDRC  = 0b00000010;  //  only Enable pin write mode
		PORTC = 0b00000010; //  disable device
		DDRC  = 0b00001111;  //  data,enable,latch,clk pin write mode
		PORTC = 0b00000010; //  initial state
		
		int init_cnt=0;
		for(init_cnt=0;init_cnt<3;init_cnt++)
		{
				HC595_send_byte(0);
		}
		LATCH_HIGH;
		_delay_loop_1(5);
		LATCH_LOW;
		_delay_ms(1);
		ENABLE;
		DATA_LOW;
		LATCH_LOW;
		CLK_LOW;
		_delay_ms(1);
}

void HC595_latch()
{
  LATCH_HIGH;
	_delay_loop_1(5);
	LATCH_LOW;
}

void LED_SHOW()
{
  HC595_latch();
}
void LED_SETTING(uint8_t data)
{
  HC595_send_byte(data);
}

void LED_BAR_SETUP(uint8_t red, uint8_t green)
{
  for(int i=0;i<12;i++)
  {
      LED_BAR_ARRAY[i][0]=(i<red);
      LED_BAR_ARRAY[i][1]=(i<green);
  }
}


void led_bar_init()
{
  DDRB |=  (1<<ABCD_pin); // PB0 GPIO WRITE MODE
  DDRB |=  (1<<EFGH_pin); // PB1 GPIO WRITE MODE
  DDRB |=  (1<<IJKL_pin); // PB2 GPIO WRITE MODE
  HC595_init();
  LED_BAR_SETUP(0,0);
}

void LED_SELECT(uint8_t SEL_NUM)
{
  if(SEL_NUM==0)
  {
    ABCD_ON;
    EFGH_OFF;
    IJKL_OFF;
  }
  if(SEL_NUM==1)
  {
    ABCD_OFF;
    EFGH_ON;
    IJKL_OFF;
  }
  if(SEL_NUM==2)
  {
    ABCD_OFF;
    EFGH_OFF;
    IJKL_ON;
  }
}

void LED_BAR_RUN()
{
  cycle_wait++;
  if(cycle_wait>300)
  {
    cycle_wait=0;
    LED_CHANGE=true;
  }

  if(LED_CHANGE)
  { 
    
    position_select++;
    if(position_select>2)
    position_select=0;

    LED_CHANGE=false;
    uint8_t LED_DATA=0;
     for(int i=0;i<4;i++)
     {
      LED_DATA=LED_DATA<<1;
      LED_DATA+=LED_BAR_ARRAY[position_select*4+i][RED];
      LED_DATA+=LED_BAR_ARRAY[position_select*4+i][GREEN]*16;
     }

    LED_SETTING(LED_DATA);
    LED_SELECT(position_select);
    LED_SHOW();

  }
}