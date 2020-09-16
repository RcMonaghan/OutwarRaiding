import requests
from bs4 import BeautifulSoup
import re
from discord import Webhook, RequestsWebhookAdapter

from datetime import datetime


webhook = Webhook.from_url("https://discordapp.com/api/webhooks/730453800527069246/Q31aGhUfXY2R8xuWXcNhX9iiNUI0s6ybeFq6DseYlntIYv_bm_5jKMAQukkjN-SqI27d", adapter=RequestsWebhookAdapter())

# Fill in your details here to be posted to the login form.
payload = {
    'login_username': 'TardBot',••••••••
    'login_password': ''
}
def GodWatch():
	Gods = []
	CurrentSpawn = []
	with requests.Session() as s:
		webhook.send("Starting a new session")
		p = s.post('https://sigil.outwar.com/login', data=payload)
		while True:
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print(current_time)
			
			me = s.get('https://sigil.outwar.com/world?suid=1034264&serverid=1')
			vault = s.get('https://sigil.outwar.com/raidtools')
			soup = BeautifulSoup(vault.content, 'html.parser')
			for a in soup.find_all("a", text=re.compile('Teleport to ')):
				God = a.text.replace("Teleport to ", "")
				CurrentSpawn.append(God)
				if (God in Gods):
					pass
				else:
					print(God+" HAS SPAWNED")
					webhook.send(God+" HAS SPAWNED at "+ current_time)
					Gods.append(God)
			for GodCheck in Gods:
				if (GodCheck in CurrentSpawn):
					pass
				else:
					webhook.send(GodCheck+" Has died "+ current_time)
					Gods.remove(GodCheck)
					GodsKilled = s.get('https://sigil.outwar.com/godstatus')
					soup = BeautifulSoup(GodsKilled.content, 'html.parser')
					for a in soup.find_all("a", text=re.compile(GodCheck)):
						KillLogLink = a.get('href')
						KillLog =  s.get('https://sigil.outwar.com/'+KillLogLink)
						KillLogContents = BeautifulSoup(KillLog.content, 'html.parser')
						for tag in KillLogContents.findAll("a", text=re.compile('items')):
							DropsDirty = tag['onmouseover']
							DropsClean = DropsDirty.replace("popup(event,'<b>", " ")
							DropsClean = DropsClean.replace("<br><br>", " ")
							DropsClean = DropsClean.replace(" </b>')", " ")
							webhook.send("Items Dropped from "+GodCheck+" "+DropsClean)
			CurrentSpawn = []
			
GodWatch()
