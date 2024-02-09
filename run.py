#!/usr/bin/python
# Creator iewil
# Date 09-02-2024, 13:20 WIB
# Support youtube.com/@iewil
# Follow my github https://github.com/iewilmaestro

#warna
b = "\033[1;34m"
c = "\033[1;36m"
d = "\033[0m"
h = "\033[1;32m"
k = "\033[1;33m"
m = "\033[1;31m"
p = "\033[1;37m"
u = "\033[1;35m"
mm = "\033[101m\033[1;31m"
mp = "\033[101m\033[1;37m"
hp = "\033[1;7m"
n = "\n"


#modul
try:
    import iewil
except ImportError:
    print("--[+] installing modul iewil")
    os.system("pip install iewil")
from importlib.metadata import version
if not version('iewil') >= "0.0.4":
    print("--[^] upgrade modul iewil")
    os.system("pip install iewil --upgrade")
    
try:
    import requests
except ImportError:
    print("--[+] installing modul requests")
    os.system("pip install requests")
try:
    import bs4
except ImportError:
    print("--[+] installing modul bs4")
    os.system("pip install bs4")

import re,requests
from iewil import *
from bs4 import BeautifulSoup
ses = requests.Session()

def login_cookie(cookie):
    try:
        url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
        if "Apa yang Anda pikirkan sekarang" in url:
            pass
        else:
            print(Echo("paket data",1))
            #gunakan data
    except:
        exit(echo_eror("Cookie expired",1))
def ubah_bahasa(cookie):
    url = ses.get("https://mbasic.facebook.com/language/",cookies={"cookie": cookie})
    bs4 = BeautifulSoup(url.text,"html.parser")
    for x in bs4.find_all("form",{"method":"post"}):
        if "Bahasa Indonesia" in str(x):
            data = {
                "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
                "jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
                "submit"  : "Bahasa Indonesia"
            }
            post = ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})

cookie = "xxx"
r=login_cookie(cookie)
print(r)
