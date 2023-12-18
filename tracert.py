import os
import subprocess
import time
from datetime import datetime

    
for i in range(1,9999999):
    logFile = open(f"tracert.txt", "a+")
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    logFile.write(f"{now}" + " ")
    hostname = "x.x.x.x"
    #response = os.system("tracert -d -h 1 " + hostname)
    response = subprocess.check_output("tracert -d -h 15 " + hostname).decode("utf-8").replace('\r\n',' ').replace('\r',' ').replace('\n',' ')
    logFile.write(f"{response}" + "\n")
    logFile.close()
    time.sleep(1)
    
