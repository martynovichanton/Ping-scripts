import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


def ping_ip(ip, active_ips):
    try:
        print(f"[*] pinging IP: {ip}")
        response = os.popen(f"ping -n 1 {ip}").read()
        if "Reply from" in response and "bytes=" in response:
            active_ips.append(ip) 
    except Exception as e:
        print(f"EXCEPTION: {e}")
    return response	
	
def ping_subnet(subnet):
    active_ips = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_list = []
        for i in range(1,250):
            time.sleep(0.1)
            ip = f"{subnet}.{i}"
            future = executor.submit(ping_ip, ip, active_ips)
            future_list.append(future)

        # for f in as_completed(future_list):
        #     print(f.result())        
            

        

    print(f"[*] Active IPs:")
    print(active_ips)

    print(f"[*] Active IPs count: {len(active_ips)}")


ping_subnet("192.168.0")
