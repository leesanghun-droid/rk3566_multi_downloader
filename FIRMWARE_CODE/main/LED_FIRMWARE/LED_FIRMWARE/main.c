/*
 * main.c
 *
 * Created: 11/21/2023 5:58:37 PM
 *  Author: ac837
 */ 

#define F_CPU 14745600UL
#include <xc.h>
#include "cmd.h"
#include "board.h"
#include "button.h"
#include "led_bar.h"
#include "led_motion.h"
#include "process_bar.h"

int main(void)
{
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