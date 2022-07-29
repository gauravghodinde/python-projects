from ntpath import join
import pywhatkit
from datetime import datetime
import time

PHONE_no = '+91' +input("enter the phone no")
print(PHONE_no)
obj_now = datetime.now()
T = obj_now.hour
X = obj_now.minute + 2
print(f'enter message before its over min {X} ')
Message_times = int(input("How many times Message should be sent : "))

Message = input("enter the message :  ")
Y = int(input("to be repeated : "))
Message_edited = " ".join((Message) * Y)
print(f' your message {Message_edited}')
for i in range(0,Message_times ):
    pywhatkit.sendwhatmsg(PHONE_no,Message_edited, T ,X)
    time.sleep(20)
    X += 1

  