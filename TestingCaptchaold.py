import requests
from bs4 import BeautifulSoup
import re
import io
from PIL import Image, ImageTk
import time
import tkinter as tk

Group1 = [
"https://sigil.outwar.com/world?suid=121995&serverid=1",
"https://sigil.outwar.com/world?suid=149484&serverid=1"
]

def Refresh():
	s.post("https://sigil.outwar.com/world?suid=121995&serverid=1")
	captcha = s.get('https://sigil.outwar.com/phpcatcha/phpcatcha_show.php')
	image_bytes = io.BytesIO(captcha.content)
	global img
	img = Image.open(image_bytes)
	global tkimage
	tkimage = ImageTk.PhotoImage(img)
	#CaptchaShow = tk.Label(root, image=tkimage)
	CaptchaShow.configure(image=tkimage)
	
	
def GetAccount():
	global s
	with requests.Session() as s:
		p = s.post('https://sigil.outwar.com/world.php?rg_sess_id=rnsh121yywsxffbvc13772sv9w5b171k&suid=122176&serverid=1')
		s.post("https://sigil.outwar.com/world?suid=121995&serverid=1")
		captcha = s.get('https://sigil.outwar.com/phpcatcha/phpcatcha_show.php')
		image_bytes = io.BytesIO(captcha.content)
		global img
		img = Image.open(image_bytes)
		GUI()
def GUI():
	global root
	root = tk.Tk()
	#global tkimage
	#tkimage = ImageTk.PhotoImage(img)
	#global CapthcaShow
	#CapthcaShow = tk.Label(root, image=tkimage).pack(side="top")
	global tkimage
	tkimage = ImageTk.PhotoImage(img)
	global CaptchaShow
	CaptchaShow = tk.Label(root, image=tkimage)
	CaptchaShow.pack(side="top")
	global CaptchaEntry
	CaptchaEntry = tk.Text(root, width=20, height=1).pack(side="bottom")
	w = tk.Button(root, text="Get Captcha", command = Refresh).pack(side="bottom")
	CaptchaEntryContents = CaptchaEntry
	#if CaptchaEntry = > 6 pass else submit
	root.mainloop()
			
GetAccount()


