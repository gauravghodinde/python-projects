from ntpath import join
import pywhatkit
from datetime import datetime
import time

PHONE_no = '+917769932661'

obj_now = datetime.now()
T = obj_now.hour
X = obj_now.minute + 2

#Message_times = int(input("How many times Message should be sent : "))



for i in range(0,10 ):
    pywhatkit.sendwhatmsg(PHONE_no,"Message_edited", T ,X)
    time.sleep(20)
    X += 1

  