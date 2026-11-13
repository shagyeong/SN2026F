import time
import RPi.GPIO as GPIO

SWI_RED= 2 # 개방 스위치
SWI_GRE= 3 # 폐쇄 스위치
LED_RED=13 # 적색 LED(경보)
LED_GRE=19 # 녹색 LED(알림)
LED_YEL=26 # 황색 LED(서보모터 대체)

# 초기화
def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # 스위치 출력 방향 지정(풀업 저항: 열림 0, 닫힘 1)
    GPIO.setup(SWI_RED,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 폐쇄 스위치
    GPIO.setup(SWI_GRE,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 개방 스위치

    # LED, 모터 출력 방향 지정
    GPIO.setup(LED_RED,GPIO.OUT) # 빨강 LED - 경보
    GPIO.setup(LED_GRE,GPIO.OUT) # 초록 LED - 알림
    GPIO.setup(LED_YEL,GPIO.OUT) # 모터 대체(켜짐: 개방, 꺼짐: 폐쇄)

    # LED 초기화: 켜짐 확인 후 끈 상태로 프로그램 진입
    led_on(LED_RED)
    led_on(LED_GRE)
    led_on(LED_YEL); time.sleep(1)
    led_off(LED_RED)
    led_off(LED_GRE)
    led_off(LED_YEL)

# led 조작
def led_on(pin):
    GPIO.output(pin,1)
def led_off(pin):
    GPIO.output(pin,0)

# 모터 조작(황색 LED 조작으로 대체)
def door_open(pin):
    print("green switch")
    led_on(LED_YEL)
def door_close(pin):
    print("red switch")
    led_off(LED_YEL)