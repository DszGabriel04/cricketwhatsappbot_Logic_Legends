import config
import json
import requests
import pywhatkit


phone_num = "+919527867744"
msg = "Test Message 2"


#pywhatkit.sendwhatmsg(phone_num, msg, 14, 50, wait_time=8)
#pywhatkit.sendwhatmsg(phone_num, msg)
pywhatkit.sendwhatmsg_instantly(phone_num, msg, 10, True, 5)
#pywhatkit.sendwhats_image(phone_num, img, msg, 15, True, 3)
