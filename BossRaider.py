import requests
from bs4 import BeautifulSoup
import re
import time


payload = {
	'submit': 'Join This Raid!',
	'submit': 'Join This Raid!',
	'join': '1'
}
JoinPayload = {
	'formtime': '1',
	'submit': 'Join This Raid!',
	'submit': 'Join This Raid!'}

def RaidFormer():
	with requests.Session() as s:
		p = s.post('https://sigil.outwar.com/world.php?rg_sess_id=****************&suid=******&serverid=1')
		me = s.get('https://sigil.outwar.com/world?suid=147052&serverid=1')
		s.post('https://sigil.outwar.com/formraid.php?target=127', data=JoinPayload)
		

def BossRaider():
	with requests.Session() as s:
		p = s.post('https://sigil.outwar.com/world.php?rg_sess_id=******************&suid=******&serverid=1')
		soup = BeautifulSoup(p.content, 'html.parser')
		me = s.get('http://sigil.outwar.com/myaccount')
		soup = BeautifulSoup(me.content, 'html.parser')
		for Accounts in soup.findAll('a', attrs={'href': re.compile("^http://")}):
			Account = Accounts.get('href')
			AccountName = Accounts.get('target')
			pattern = 'PLAY!'
			result = re.match(pattern, AccountName)
			if Accounts.text != "PLAY!":
				me = s.get(Account)
				Raid = s.get('https://sigil.outwar.com/crew_raidsforming.php')
				soup = BeautifulSoup(Raid.content, 'html.parser')
				for a in soup.find_all("a", attrs={'href': re.compile('/joinraid.php')}):
					RaidLink= a.get('href')
					global RaidJoin
					RaidJoin = ('https://sigil.outwar.com'+RaidLink)
					print(RaidJoin)
					start = 'https://sigil.outwar.com//joinraid.php?raidid='
					end = '&'
					global RaidID
					RaidID = RaidJoin[RaidJoin.find(start)+len(start):RaidJoin.rfind(end)]
					print(RaidID)
					s.post(RaidJoin, data=payload)



def RaidLaunch():
	with requests.Session() as s:
		p = s.post('https://sigil.outwar.com/world.php?rg_sess_id=*******************&suid=******&serverid=1')
		me = s.get('https://sigil.outwar.com/world?suid=******&serverid=1')
		print(RaidJoin)
		JoinLink = ('https://sigil.outwar.com/joinraid.php?raidid='+RaidID)
		print(JoinLink)
		print(JoinLink+"&launchraid=yes&raidid="+RaidID)
		s.get(JoinLink+"&launchraid=yes&raidid="+RaidID)
RaidFormer()
# Wait for 5 seconds
time.sleep(10)
BossRaider()
time.sleep(10)
RaidLaunch()
