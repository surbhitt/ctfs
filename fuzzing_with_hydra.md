
# FUZZING USING HYDRA

(ref_article)[https://infinitelogins.com/2020/02/22/how-to-brute-force-websites-using-hydra/] <br>
(ref_vid)[https://www.youtube.com/watch?v=YrMNih3Z-4Y] 

> INTRO

- it is brute force online password cracking program
- used on SSH, Web Application Form, FTP or SNMP
- it can brute force Asterisk, AFP, Cisco AAA, Cisco auth, Cisco enable, CVS, Firebird, FTP,  HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET, HTTP-HEAD, HTTP-POST, HTTP-PROXY, HTTPS-FORM-GET, HTTPS-FORM-POST, HTTPS-GET, HTTPS-HEAD, HTTPS-POST, HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MS-SQL, MYSQL, NCP, NNTP, Oracle Listener, Oracle SID, Oracle, PC-Anywhere, PCNFS, POP3, POSTGRES, RDP, Rexec, Rlogin, Rsh, RTSP, SAP/R3, SIP, SMB, SMTP, SMTP Enum, SNMP v1+v2+v3, SOCKS5, SSH (v1 and v2), SSHKEY, Subversion, Teamspeak (TS2), Telnet, VMware-Auth, VNC and XMPP.
- (ref)[https://en.kali.tools/?p=220] to kali tool page for hydra
- (git repo)[https://github.com/vanhauser-thc/thc-hydra]

>command

### fuzzing a web form login

`sudo hydra -l cool.hacker.8 -P /folder/utils/rockyou.txt 142.93.209.130 http-post-form "/forums-login:username=cool.hacker.8&password=^PASS^&csrfmiddlewaretoken=qcMXh1SE1z6lfLtTLt3SZ9UfpzVgcevyjXH4JyJEqCKuZrzCJAV5FS4rLPzFo18r:Access to 142.93.209.130 was denied"`

- sudo hydra *identifier* $USERNAMElist *identifier* $PASSWORDlist ip type "/location of the form:username=^USER^&password=^PASS^:failure identifier"

<br> // <br>

`hydra -l <username> -P <wordlist> 10.10.115.211 http-form-post "/:username=^USER^&password=^PASS^:F=incorrect" -V`

- the -V is for the verbrose 

### bruteforcing ssh

`hydra -l <username> -P <full path to pass> 10.10.115.211 -t 4 ssh`

- `-t` identifies the number of threads and the 4 is the number identifier 


> description 

- the username identifier can be `-l` to give single username or `-L` to provide a wordlist for usernames
- the ip is the ip we are connecting (without the port)
- type is the post or get method used `http-post-form` here
- the location of the form is the directory its is located in (found in the dns)
- after the first : is the request being send (can be found in the network tab of the inspect element, in mozilla edit and resend scroll to bottom)
- the lst : is for faiure detection 
