extern void LED_BAR_SETUP(uint8_t red, uint8_t green);

#define GREEN 0
#define RED 1
#define YELLOW 2
#define one_second_cnt 7500


int PROCESS_TIME=10;

int BAR_LED_COLOR=GREEN;
int process_bar_cycle_wait=0;
int process_bar_tims_second=0;
uint8_t Process_level=0;
bool PROCESS_DONE=true;
void PROCESS_LED_LOGIC()
{
  if(PROCESS_DONE==false)
  {
    Process_level++;

    uint8_t led_level = Process_level;
    if(BAR_LED_COLOR==GREEN)
      LED_BAR_SETUP(0,led_level);
    if(BAR_LED_COLOR==RED)
      LED_BAR_SETUP(led_level,0);
    if(BAR_LED_COLOR==YELLOW)
      LED_BAR_SETUP(led_level,led_level);

    if(Process_level>=12)
    {
      Process_level=0;
      PROCESS_DONE=true;
    }

  }
}

void PROCESS_BAR_LED()
{
  process_bar_cycle_wait++;
  if(process_bar_cycle_wait>one_second_cnt)
  {
    process_bar_cycle_wait=0;
    process_bar_tims_second++;
  }
  if(PROCESS_TIME<=10)
    PROCESS_TIME=10;
  if(process_bar_tims_second>PROCESS_TIME)
  {
    process_bar_tims_second=0;
    PROCESS_LED_LOGIC();
  }
}