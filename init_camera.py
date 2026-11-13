import time
from picamera2 import Picamera2

def init_camera(width=640,height=480):
    camera=Picamera2()
    config=camera.create_preview_configuration(main={"format":"RGB888","size":(width,height)})
    camera.configure(config)
    camera.start()
    time.sleep(1.0)
    return camera