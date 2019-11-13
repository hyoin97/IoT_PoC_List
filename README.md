# IoT_PoC_List

IoT 기기들의 취약점 여부 판별 코드

* CVE-2018-9032  
  인증 우회 취약점으로 /category_view.php, /folder_view.php 와 같은 인증된 페이지에 직접 액세스가 가능함  
  
* Netgear JNR1010 - Authentication Bypass  
  인증 우회 취약점으로 fake Session ID를 생성 후 로그인, 로그아웃 과정에서 세션 ID의 변화가 없음  

* Netgear JNR1010 - Path Traversal  
  Path Traversal 취약점으로 로그인 없이 계정 관련 파일이 노출됨  

* CVE-2018-15840
  'nmap -f'를 이용한 DoS공격으로 기기를 
