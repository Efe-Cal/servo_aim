import RPi.GPIO as GPIO
import math
import numpy as np


servoPIN1= 17
servoPIN2=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
pwm1 = GPIO.PWM(servoPIN1, 50)
GPIO.setmode(GPIO.BCM)
pwm1.start(0)

GPIO.setup(servoPIN2, GPIO.OUT)
pwm2 = GPIO.PWM(servoPIN2, 50) 
pwm2.start(0)

class ServoControl:
    def __init__(self):
        self.current_angle=0
        self.aciAyarla(0)
    def aciAyarla(self,aci,no):
        x=(1/180)*aci + 1
        duty=x*5
        exec(f"pwm{no}.ChangeDutyCycle(duty)")
        self.current_angle+=duty

    
        
    def aim(self,distance,dist2cent_x,dist2cent_y):
        #horizental aim
        hipotenus=math.sqrt(dist2cent_x**2+distance**2)
        sineh=dist2cent_x//hipotenus
        degh=np.rad2deg(np.arcsin(sineh))
        self.aciAyarla(self.current_angle+degh,1)
        
        #vertical aim
        hipotenus=math.sqrt(dist2cent_y**2+distance**2)
        sinev=dist2cent_x//hipotenus
        degv=np.rad2deg(np.arcsin(sinev))
        self.aciAyarla(self.current_angle+degv,2)