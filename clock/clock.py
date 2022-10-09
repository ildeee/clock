import time
from clock_funcs import *
     

rad=100

tur.ht()
tur.tracer(0)


clock(rad,(0,0))

while True:
    tym=time.localtime()
    tymexpand=(tym.tm_hour,tym.tm_min,tym.tm_sec)
    angles=time_angle(tymexpand)
    scene(angles,rad)
    tur.update()
    time.sleep(1)
    clearscene(angles,rad)
    tur.update()
