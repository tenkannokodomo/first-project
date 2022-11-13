import time 
if __name__ == '__main__':
	words = ['Hui', 'Zalupa', 'Blyat']
	tm = time.monotonic() + 60 * 30
	while time.monotonic() < tm:
		for i in range(len(words)):
			print(words[i])
			time.sleep(3)