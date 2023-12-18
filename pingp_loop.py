from subprocess import Popen
import time

for i in range(10):
	Popen(["python", "pingp.py"])
	time.sleep(0.2)
