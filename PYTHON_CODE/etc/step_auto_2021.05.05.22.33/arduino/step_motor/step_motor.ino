#define motor_speed 90 // 90 => max_high_speed

#define step_motor1_pul_pin 2
#define step_motor2_pul_pin 3
#define step_motor1_dir_pin 5
#define step_motor2_dir_pin 6
#define step_eable_pin 8


#define header1 0
#define header2 1
#define data_kind 2
#define set_angle 3
#define set_parameta 4

double now_angle1=0;
double now_angle2=0;
double target_angle1=0;
double target_angle2=0;
double gear1=1;
double gear2=1;
int motor1_dir=1;
int motor2_dir=1;

int mode = header1;
int read_date_size=0;
uint8_t angle[4]={0,0,0,0};
uint8_t motor_setup[4]={1,1,1,1};

void setup() {
  Serial.begin(115200);
  Serial.println("start step_motor~");

  pinMode(step_eable_pin,OUTPUT);
  pinMode(step_motor1_dir_pin,OUTPUT);
  pinMode(step_motor2_dir_pin,OUTPUT);
  pinMode(step_motor1_pul_pin,OUTPUT);
  pinMode(step_motor2_pul_pin,OUTPUT);

  digitalWrite(step_eable_pin,HIGH);
  digitalWrite(step_motor1_dir_pin,LOW);
  digitalWrite(step_motor2_dir_pin,LOW);
  digitalWrite(step_motor1_pul_pin,LOW);
  digitalWrite(step_motor2_pul_pin,LOW);

}

void loop()
{
   move_motor1();
   move_motor2();
   cmd();
}

void move_motor1()
{
  digitalWrite(step_motor1_pul_pin,LOW);

  double co_angle_to_position1 = (gear1*3200)/360;
  double co_position_to_angle1 = 360/(gear1*3200);
  
    int32_t target_position1 = target_angle1*co_angle_to_position1;
    int32_t now_position1 = now_angle1*co_angle_to_position1;
    int32_t error1 = target_position1-now_position1;

    if(error1>0)
    {
      digitalWrite(step_eable_pin,LOW);
      if(motor1_dir)
        digitalWrite(step_motor1_dir_pin,LOW);
      else
        digitalWrite(step_motor1_dir_pin,HIGH);
      delayMicroseconds(10);
      digitalWrite(step_motor1_pul_pin,HIGH);
      delayMicroseconds(motor_speed);
      now_angle1 += co_position_to_angle1;
    }else if(error1<0)
    {
      digitalWrite(step_eable_pin,LOW);
      if(motor1_dir)
        digitalWrite(step_motor1_dir_pin,HIGH);
      else
        digitalWrite(step_motor1_dir_pin,LOW);
      delayMicroseconds(10);
      digitalWrite(step_motor1_pul_pin,HIGH);
      delayMicroseconds(motor_speed);
      now_angle1 -= co_position_to_angle1;
    }
}

void move_motor2()
{
  digitalWrite(step_motor2_pul_pin,LOW);

  double co_angle_to_position2 = (gear2*3200)/360;
  double co_position_to_angle2 = 360/(gear2*3200);
  
    int32_t target_position2 = target_angle2*co_angle_to_position2;
    int32_t now_position2 = now_angle2*co_angle_to_position2;
    int32_t error2 = target_position2-now_position2;

    if(error2>0)
    {
      digitalWrite(step_eable_pin,LOW);
      if(motor2_dir)
        digitalWrite(step_motor2_dir_pin,LOW);
      else
        digitalWrite(step_motor2_dir_pin,HIGH);
      delayMicroseconds(10);
      digitalWrite(step_motor2_pul_pin,HIGH);
      delayMicroseconds(motor_speed);
      now_angle2 += co_position_to_angle2;
    }else if(error2<0)
    {
      digitalWrite(step_eable_pin,LOW);
      if(motor2_dir)
        digitalWrite(step_motor2_dir_pin,HIGH);
      else
        digitalWrite(step_motor2_dir_pin,LOW);
      delayMicroseconds(10);
      digitalWrite(step_motor2_pul_pin,HIGH);
      delayMicroseconds(motor_speed);
      now_angle2 -= co_position_to_angle2;
    }
}

void cmd()
{
  if(Serial.available()>0)
    {
      unsigned char c = Serial.read();
      switch(mode)
      {
        case header1:
          read_date_size=0;
          if(c==0xAA)
            mode++;
          else
            mode=header1;
        break;
        case header2:
          if(c==0x55)
            mode++;
          else
            mode=header1;
        break;
        case data_kind:
          if(c==0x00)
          {
            mode=set_angle;
            read_date_size=4;
          }else if(c==0x01)
          {
            mode=set_parameta;
            read_date_size=4;
          }
        break;
        case set_angle:
        angle[4-read_date_size]=c;
        read_date_size--;
        if(read_date_size<=0)
        {
          target_angle1 = (double)((int32_t)angle[0]*256 + (int32_t)angle[1])/100;
          target_angle2 = (double)((int32_t)angle[2]*256 + (int32_t)angle[3])/100;
          Serial.print("angle1_set: ");
          Serial.print(target_angle1);
          Serial.print(", angle2_set: ");
          Serial.println(target_angle2);
          mode=header1;
        }
        break;
        case set_parameta:
        motor_setup[4-read_date_size]=c;
        read_date_size--;
        if(read_date_size<=0)
        {
          gear1 = motor_setup[0];
          gear2 = motor_setup[1];
          motor1_dir = motor_setup[2];
          motor2_dir = motor_setup[3];
          Serial.print("gear1: ");
          Serial.print(gear1);
          Serial.print(", gear2: ");
          Serial.print(gear2);
          Serial.print(", motor1_dir: ");
          Serial.print(motor1_dir);
          Serial.print(", motor2_dir: ");
          Serial.println(motor2_dir);

          mode=header1;
        }
        break;
        default:
          mode=header1;
      }
      
    }
  
}
