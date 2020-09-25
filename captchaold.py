import requests
from bs4 import BeautifulSoup
import re
import io
from PIL import Image

def RaidFormer():
	with requests.Session() as s:
		p = s.post('https://sigil.outwar.com/world.php?rg_sess_id=rnsh121yywsxffbvc13772sv9w5b171k&suid=122176&serverid=1')
		me = s.get('http://sigil.outwar.com/myaccount')
		soup = BeautifulSoup(me.content, 'html.parser')
		for Accounts in soup.findAll('a', attrs={'href': re.compile("^http://")}):
			Account = Accounts.get('href')
			AccountName = Accounts.get('target')
			pattern = 'PLAY!'
			result = re.match(pattern, AccountName)
			if Accounts.text != "PLAY!":
				Member = s.get(Account)
				print(Member)
				captcha = s.get('https://sigil.outwar.com/phpcatcha/phpcatcha_show.php')
				image_bytes = io.BytesIO(captcha.content)
				img = Image.open(image_bytes)
				img.show()
RaidFormer()
