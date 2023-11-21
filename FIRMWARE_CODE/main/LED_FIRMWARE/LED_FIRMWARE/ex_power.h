#define EX_POWER_UP		PORTC |=  (1<<PORTC4)
#define EX_POWER_DOWN	PORTC &= ~(1<<PORTC4)


void ex_power_init()
{
	DDRC |=  (1<<DDC4); // PC4 GPIO OUTPUT MODE
}

void ex_power_up()
{
	EX_POWER_UP;
}

void ex_power_down()
{
	EX_POWER_DOWN;
}
