import uart
import time


num=0
while True:
    num=num+1
    result=uart.read_serial()
    print(str(num)+" : "+result)

