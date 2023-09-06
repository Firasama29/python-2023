import pyautogui	# for simulating mouse and keyboard interactions
from tkinter import Tk	# to get copied content from clipboard
from time import sleep	# to pause between each action

import pyshorteners	# to shorten the urls

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


links = []
SLEEP_TIME = 0.5
MAX_DUPLICATE_COUNT = 5
pdf_file = 'tabs.pdf'

def read_urls():
	pyautogui.hotkey('ctrl', '1')	# go to first tab in the browser
	sleep(SLEEP_TIME)
	duplicate_count = 0
	shortener= pyshorteners.Shortener()	# get the class from pyshorteners library and assign it to a variable
	while duplicate_count < MAX_DUPLICATE_COUNT:
		pyautogui.click(x=100, y=70, button='left')	# typical left mouse click coordinates to select address bar in the browser
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'a')
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'c')
		sleep(SLEEP_TIME)
		link = Tk().clipboard_get()	# retrieve the copied url from clipboard

		# shorten url
		shortened_url = shortener.tinyurl.short(link)

		if len(links) and shortened_url in links:
			duplicate_count += 1
		else:
			links.append(shortened_url)
		print(f'original url: {link}')
		print(f'shortened url: {shortened_url}')
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'tab')
		sleep(SLEEP_TIME)

def save_to_pdf():
	c = canvas.Canvas(pdf_file, pagesize=letter)	# initialize Canvas object
	c.setFont('Helvetica', 12)

	# write the headline
	c.drawString(100, 700, 'CHROME TABS') # y=700
	y = 670	# initial y coordinate for the links
	# write the links 
	for link in links:
		c.drawString(100, y, link)
		y -= 12	# decrease y coordinate to move each link to the next line
	c.save()


if __name__ == '__main__':
	read_urls()
	save_to_pdf()
	
