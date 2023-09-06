import pyautogui  # used for simulating mouse and keyboard interactions and controlling chrome and copying urls
from time import sleep	# pause between each action
from tkinter import Tk	# Tk is used to access system clipboard to get the copied url

links = []
SLEEP_TIME = 0.5
filename = 'chrome_tabs.txt'
MAX_DUPLICATE_COUNT = 5

def read_urls():	# simulates mouse click on address bar, copy the url to the clipboard and retrieve it using Tk().clipboard_get()
	pyautogui.hotkey('ctrl', '1')	# go to first tab
	sleep(SLEEP_TIME)
	duplicate_count = 0
	while duplicate_count < MAX_DUPLICATE_COUNT:
		pyautogui.click(x=1000, y=70, button='left')	# typical left mouse click to select the url in the address bar of current open browser
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'a')
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'c')
		sleep(SLEEP_TIME)
		link = Tk().clipboard_get()	# access system clipboard, get the saved url and assign it to a variable
		if len(links) > 0 and link in links:	# checks if the links list is not empty and copied link is already in links
			duplicate_count += 1	# if link is a duplicate, duplicate_count is incremented and printed in the console
			print(f'Duplicate {str(duplicate_count)} found: {link}')
		else:
			links.append(link)
		print(link)
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'tab')	# go to next tab
		sleep(SLEEP_TIME)

def save_to_file():
	file = open(filename, 'w') # open file in write mode and create variable to write content inside it
	file.write('\n'.join(links))	# joins the urls into a single string, separating each url by '\n'

if __name__ == '__main__':
	read_urls()
	save_to_file()
	pyautogui.hotkey('ctrl', 'd')
