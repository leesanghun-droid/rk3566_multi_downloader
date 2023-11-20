#define data_pin 0
#define enable_pin 1
#define latch_pin 2
#define clk_pin 3

#define ABCD_pin 0
#define EFGH_pin 1
#define IJKL_pin 2

#define ABCD_OFF	PORTB &= ~(1<<ABCD_pin)
#define ABCD_ON   PORTB |=  (1<<ABCD_pin)

#define EFGH_OFF	PORTB &= ~(1<<EFGH_pin)
#define EFGH_ON   PORTB |=  (1<<EFGH_pin)

#define IJKL_OFF	PORTB &= ~(1<<IJKL_pin)
#define IJKL_ON   PORTB |=  (1<<IJKL_pin)


#define ENABLE	PORTC &= ~(1<<enable_pin)
#define DISABLE PORTC |=  (1<<enable_pin)

#define DATA_HIGH PORTC |=  (1<<data_pin)
#define DATA_LOW  PORTC &= ~(1<<data_pin)

#define LATCH_HIGH PORTC |=  (1<<latch_pin)
#define LATCH_LOW  PORTC &= ~(1<<latch_pin)

#define CLK_HIGH PORTC |=  (1<<clk_pin)
#define CLK_LOW  PORTC &= ~(1<<clk_pin)
