//#define F_CPU 16000000UL
//#include <stdio.h>
//#include <util/delay.h>
//#include <avr/io.h>
//ubuntu_tip : sudo chmod a+rw /dev/ttyACM0

#include "board.h"
#include "led_bar.h"
#include "boot.h"

void setup() {
  Serial.begin(9600);
  led_bar_init();
}

void loop()
{
    BOOT_LED();
    LED_BAR_RUN();
}