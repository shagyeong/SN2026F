# 라이브러리
import time
import cv2
from picamera2 import Picamera2
import RPi.GPIO as GPIO

# 사용자 모듈
from init_camera import init_camera # 카메라 초기화
from gpio import init_gpio,led_on,led_off,door_open,door_close # GPIO 조작
from gpio import SWI_RED,SWI_GRE,LED_RED,LED_GRE,LED_YEL # GPIO 상수

def main():
    camera=init_camera()
    init_gpio()

    # 2. 인터럽트 이벤트 등록 (풀업이므로 1->0으로 떨어지는 FALLING 감지)
    GPIO.add_event_detect(SWI_GRE, GPIO.FALLING, callback=door_open, bouncetime=300)
    GPIO.add_event_detect(SWI_RED, GPIO.FALLING, callback=door_close, bouncetime=300)

    try:
        while True:
            frame=camera.capture_array()
            cv2.imshow("Camera",frame)
            cv2.waitKey(1)

    except KeyboardInterrupt:
        print("Keyboard Interrupt")

    finally:
        camera.stop()
        cv2.destroyAllWindows()
        GPIO.cleanup()

if __name__ == "__main__":
    main()