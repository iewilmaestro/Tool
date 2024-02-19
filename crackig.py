import os,sys

#modul
try:
    import iewil
except ImportError:
    print("---[+] installing modul iewil")
    os.system("pip install iewil")
from importlib.metadata import version
if not version('iewil') >= "0.0.4":
    print("---[^] upgrade modul iewil")
    os.system("pip install iewil --upgrade")
try:
    import requests
except ImportError:
    print("---[+] installing modul requests")
    os.system("pip install requests")

import requests
from iewil import *

ses = requests.Session()

def Menu(no, msg):
    print(b+"---["+p+str(no)+b+"] "+p+msg)
def loading (des):
    sym = ['.... ─ ', '...  / ', '..   │ ', '.    \ ']
    a = 0
    while True:
        a += 1
        if a > 100:
            break
        print(des + sym[a % 4] + str(a) + str(' %') , end="\r")
        time.sleep(0.1)
def UaIg():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent
    
def LoginCookie():
    cok = input(h+"---["+p+"+"+h+"]"+p+"Input Cookie: ")
    use = input(h+"---["+p+"+"+h+"]"+p+"Input Username: ")
    
    kuki=open('data/.cookie','w').write(cok)
    user=open('data/.username','w').write(us)
    
def LoginUser():
    use = input(h+"---["+p+"+"+h+"]"+p+"Input Username: ")
    pas = input(h+"---["+p+"+"+h+"]"+p+"Input Password: ")
    
    r = ses.get("https://www.instagram.com/",headers={"user-agent":UaIg()}).text
    
def SesionCheck():
    try:
        kuki=open('data/.cookie','r').read()
    except FileNotFoundError:
        Menu(1,"Login Cookie")
        Menu(2,"Login User & Pas")
        Metode = input(k+"---["+p+"?"+k+"] "+p+"pilih nomor: ")
        Line()
        if Metode == 1:LoginCookie()
        elif Metode == 2:LoginUser()
        else Metode =='':exit(m+"---["+p+"!"+m+"] "+p+"Tolol")
try:os.mkdir('data')
except:pass
Banner("tool","1.0")

SesionCheck()
