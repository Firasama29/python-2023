import pyautogui
from tkinter import Tk
from time import sleep

SLEEP_TIME = 0.5
MAX_DUPLICATE_COUNT = 5
links = []
filename = 'chrome_tabs.txt'

def read_urls():
	pyautogui.hotkey('ctrl', '1') #first tab
	duplicate_count = 0
	while duplicate_count < MAX_DUPLICATE_COUNT:
		pyautogui.click(x=1000, y=70, button='left')
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'a')
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'c')
		sleep(SLEEP_TIME)
		link = Tk().clipboard_get()
		if len(links) > 0 and link in links:
			duplicate_count += 1
		else:
			links.append(link)
		print(link)
		sleep(SLEEP_TIME)
		pyautogui.hotkey('ctrl', 'tab')
		sleep(SLEEP_TIME)

def save_to_file():
	file = open(filename, 'w')
	file.write('\n'.join(links))
	file.close()

if __name__ == '__main__':
	read_urls()
	save_to_file()
	pyautogui.hotkey('win', 'd')
