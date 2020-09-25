import requests
from bs4 import BeautifulSoup
import re
import io
from PIL import Image

def RaidFormer():
	with requests.Session() as s:
		p = s.post('https://sigil.outwar.com/world.php?rg_sess_id=rnsh121yywsxffbvc13772sv9w5b171k&suid=122176&serverid=1')
		captcha = s.get('https://sigil.outwar.com/phpcatcha/phpcatcha_show.php')
		image_bytes = io.BytesIO(captcha.content)
		img = Image.open(image_bytes)
		img.show()
RaidFormer()
