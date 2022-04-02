''' a program to find pattern string in a file '''

import re
f = open("0.xml", "rb")
stuff = re.findall(r'(>)([\w+\s\w+{*\w}*]+)(<)',f.read())
l =""
for x in stuff:
 	l += x[1].strip()

print(l.replace(" ", ""))
