*Automated WhatsApp Message Sender*
This Python script utilizes the pywhatkit library to send scheduled WhatsApp messages automatically. Users can input the recipient's phone number, the desired message, and the scheduled time for sending the message.

Prerequisites
Python 3.x
pywhatkit library (install using pip install pywhatkit)
How to Use
Install the required library if you haven't already:

bash
Copy code
pip install pywhatkit
Run the script using a Python interpreter:

bash
Copy code
python automated_whatsapp_sender.py
Follow the prompts in the console:

Enter the recipient's phone number (including the country code).
Enter the message you want to send.
Specify the hours and minutes when you want to send the message.
The script will then use the pywhatkit.sendwhatmsg() function to schedule and send the specified message to the provided phone number at the specified time.

Input Explanation
phone_number: Enter the recipient's phone number in international format (including the country code). For example: "+1234567890".
message: Input the text message you want to send.
hours and minutes: Set the scheduled time for sending the message in 24-hour format. For instance, if you set hours = 14 and minutes = 35, the message will be sent at 2:35 PM.
Note
Make sure your computer has an active internet connection and WhatsApp Web is logged in on the browser you intend to use.
Disclaimer
This script interacts with WhatsApp Web using the pywhatkit library. While it's intended for legitimate and personal use, automated messaging might violate WhatsApp's terms of service or be considered spam if misused. Use this script responsibly and in accordance with WhatsApp's policies.

Author
Wesley Omoke

License
This project is licensed under the MIT License.
