import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 풀업 저항: 열림 0, 닫힘 1
SWI_RED= 2; GPIO.setup(SWI_RED,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 폐쇄 스위치
SWI_GRE= 3; GPIO.setup(SWI_GRE,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 개방 스위치
LED_RED=13; GPIO.setup(LED_RED,GPIO.OUT) # 빨강 LED - 경보
LED_GRE=19; GPIO.setup(LED_GRE,GPIO.OUT) # 초록 LED - 알림
LED_YEL=26; GPIO.setup(LED_YEL,GPIO.OUT) # 모터 대체(켜짐: 개방, 꺼짐: 폐쇄)

# led 조작
def led_on(pin):
    GPIO.output(pin,1)
def led_off(pin):
    GPIO.output(pin,0)

# 모터 조작(led로 대체)
def door_open(pin):
    print("green switch")
    led_on(LED_YEL)
def door_close(pin):
    print("red switch")
    led_off(LED_YEL)

# LED 테스트
led_off(LED_RED)
led_off(LED_GRE)
led_off(LED_YEL)

led_on(LED_RED)
led_on(LED_GRE)
led_on(LED_YEL)

time.sleep(1)

led_off(LED_RED)
led_off(LED_GRE)
led_off(LED_YEL)

# 2. 인터럽트 이벤트 등록 (풀업이므로 1->0으로 떨어지는 FALLING 감지)
GPIO.add_event_detect(SWI_GRE, GPIO.FALLING, callback=door_open, bouncetime=300)
GPIO.add_event_detect(SWI_RED, GPIO.FALLING, callback=door_close, bouncetime=300)

# 3. 메인 루프 (인터럽트 대기)
try:
    print("Press Switch")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Keyboard Interrupt")

finally:
    led_on(LED_RED)
    led_on(LED_GRE)
    led_on(LED_YEL)

    time.sleep(1)   

    led_off(LED_RED)
    led_off(LED_GRE)
    led_off(LED_YEL)
    GPIO.cleanup()