import time
from bs4 import BeautifulSoup
import requests

REFRESH_INTERVAL = 10

class SiriusXMListener(object):
	def __init__(self, channel_number):
		self.channel = channel_number
	
	def listen(self, callback):
		self.callback = callback
		self.listenForever()
		
	def listenForever(self):
		while True:
			self.extract_now_playing()
			time.sleep(5)

	def extract_now_playing(self):
		r = requests.get('http://www.dogstarradio.com/now_playing.php')
		soup = BeautifulSoup(r.text, 'html5lib')
		div_id_name = 'channel%s' % self.channel
		query = soup.find('div', id=div_id_name).get_text()
		self.callback(query)