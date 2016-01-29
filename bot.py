import sys
import time
import pprint
import telepot
import random

def guessnum(text, chat_id, msg_id): 
	num = random.randint(1,10)
	for s in text.split():
        	if s.isdigit():
                	int(s)

	if num == int(s):
		bot.sendMessage(chat_id, "Well Done. You guessed right.\nThe numeber is: "+str(num),None,None,msg_id)	
	else:
		if (int(s)>10) | (int(s)<1):	
			bot.sendMessage(chat_id, "You must enter a number between 1 to 10, Try Again",None,None,msg_id)
		else:
			bot.sendMessage(chat_id, "You lose, \n The number is: "+str(num),None,None,msg_id)

def handle(msg):
	pprint.pprint(msg)
	chat_id = msg['chat']['id']
	if 'username' in msg['from']:
		user = '@'+msg['from']['username']
	else:
		if 'last_name' in msg['from']:
			 user = msg['from']['first_name']+' '+msg['from']['last_name']
		else:
			user = msg['from']['first_name']
	text = msg['text']
	msg_id = msg['message_id']

	if "/whoami" in text:
		bot.sendMessage(chat_id, user)
	elif "/time" in text:
		bot.sendMessage(chat_id, time.asctime(time.localtime(time.time())),None,None,msg_id)
	elif "/dice" in text:
		bot.sendMessage(chat_id, random.randint(1,6),None,None,msg_id)
	elif "/info" in text:
		bot.sendMessage(chat_id, "This is a test bot written in python by @tasosgrv",None,None,msg_id)
	elif "/hello" in text:
		bot.sendMessage(chat_id, "Hello, "+user+" and welcome to chat!",None,None,msg_id)
	elif "/help" in text:
		bot.sendMessage(chat_id, "======COMMANDS======\n /whoami - Returns your name\n /hello - The bot says hello\n /time - Shows the current time\n /dice - Roll the dice\n /guessnum [number] - Guess a number between 1 to 10\n /info -  Informations aboot the bot\n /help - shows is message")
	elif "/guessnum" in text:	
		if text == "/guessnum":
			bot.sendMessage(chat_id, "You must type a number after the command\ne.g. /guessnum 6",None,None,msg_id)
		else:
			guessnum(text, chat_id, msg_id)
		
# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
# Keep the program running.
while 1:
    time.sleep(10)