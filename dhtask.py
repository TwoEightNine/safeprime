import os
import time

DELAY = 60 * 60 * 24 # 1 day

while True:
	os.system("python dhprime.py")
	time.sleep(DELAY)
