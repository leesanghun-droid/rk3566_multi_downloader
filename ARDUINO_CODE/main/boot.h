extern void LED_BAR_SETUP(uint8_t red, uint8_t green);

int boot_cycle_wait=0;
int boot_logic_cnt=0;
bool BOOT_DONE=false;
void BOOT_LED_LOGIC()
{
  if(BOOT_DONE==false)
  {
    boot_logic_cnt++;
    if(boot_logic_cnt>=13)
    {
      boot_logic_cnt=0;
      BOOT_DONE=true;
    }

    uint8_t led_level = boot_logic_cnt;
    LED_BAR_SETUP(0,led_level);
  }
}
void BOOT_LED()
{
  boot_cycle_wait++;
  if(boot_cycle_wait>30000)
  {
    boot_cycle_wait=0;
    BOOT_LED_LOGIC();
  }
}