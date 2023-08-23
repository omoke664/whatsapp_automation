import pywhatkit
import datetime


phone_number= input("Enter the receiver's phone number:")    #Receivers phone number with country code
message=input("Enter the message you wish to send:")
hours = 14
minutes = 35



now = datetime.datetime.now()
scheduled_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
pywhatkit.sendwhatmsg(phone_number, message, scheduled_time.hour, scheduled_time.minute)
