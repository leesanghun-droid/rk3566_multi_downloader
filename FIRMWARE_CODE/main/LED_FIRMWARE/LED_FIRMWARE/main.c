/*
 * main.c
 *
 * Created: 11/21/2023 5:58:37 PM
 *  Author: ac837
 */ 

#define F_CPU 14745600UL
#include <xc.h>
#include "cmd.h"
#include "ex_power.h"
#include "board.h"
#include "button.h"
#include "led_bar.h"
#include "led_motion.h"
#include "process_bar.h"
//fuse bit HIGH : D1, LOW : EF
int main(void)
{
	  ex_power_init();
	  ex_power_down();
	  uart_init();
	  led_bar_init();
	  button_init();
	  
    while(1)
    {
       PROCESS_BAR_LED();
       BOOT_LED();
       LED_BAR_RUN();
       CMD();
       button_read();
    }
}