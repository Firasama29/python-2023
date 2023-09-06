import pyautogui
from time import sleep
from tkinter import Tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

links = []
filename = 'tabs.pdf'
MAX_DUPLICATE_COUNT = 5
sleep_time = 0.5


def read_urls():
	pyautogui.hotkey('ctrl', '1')
	sleep(sleep_time)
	duplicate_count = 0
	while duplicate_count < MAX_DUPLICATE_COUNT:
		pyautogui.click(x=1000, y=70, button='left')
		pyautogui.hotkey('ctrl', 'a')
		sleep(sleep_time)
		pyautogui.hotkey('ctrl', 'c')
		sleep(sleep_time)
		link = Tk().clipboard_get()
		if len(links) and link in links:
			duplicate_count += 1
		else:
			links.append(link)

		print(link)
		sleep(sleep_time)
		pyautogui.hotkey('ctrl', 'tab')
		sleep(sleep_time)
		

def save_to_pdf():
	c = canvas.Canvas(filename, pagesize=letter)
	c.setFont('Helvetica', 12)
	
	# set the initial y coordinate
	c.drawString(100, 700, 'CHROME TABS')

	# add headline in the pdf
	y = 650
	for link in links:
		c.drawString(100, y, link)
		
		# move to the next line (decrease y coordinate)
		y -= 12
	c.save()

if __name__ == '__main__':
	read_urls()
	save_to_pdf()
	#pyautogui.hotkey('ctrl', 'd')
	

