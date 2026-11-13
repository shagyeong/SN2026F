import time
import RPI.GPIO as GPIO

def led_on(pin):
    GPIO.output(pin,1)
def led_off(pin):
    GPIO.output(pin,0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 풀업 저항: 열림 0, 닫힘 1
SWI_RED= 2; GPIO.setup(SWI_RED,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 폐쇄 스위치
SWI_GRE= 3; GPIO.setup(SWI_GRE,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 개방 스위치
LED_RED= 5; GPIO.setup(LED_RED,GPIO.OUT) # 빨강 LED - 경보
LED_GRE= 6; GPIO.setup(LED_GRE,GPIO.OUT) # 초록 LED - 알림
LED_YEL=13; GPIO.setup(LED_YEL,GPIO.OUT) # 모터 대체(켜짐: 개방, 꺼짐: 폐쇄)

led_on(LED_RED); time.sleep(1); led_off(LED_RED)
led_on(LED_GRE); time.sleep(1); led_off(LED_GRE)
led_on(LED_YEL); time.sleep(1); led_off(LED_YEL)

GPIO.cleanup()