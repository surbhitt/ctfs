
>[writeup](https://picoctf2021.haydenhousen.com/reverse-engineering/transformation)

>file named *enc*
>content: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽
>UTF-8
<--ascii conversion: ioT{6bt_nt4_f8e0b8}>
<--one more conversion to decimal or something>
	
>reverse the given py code 
>''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
>this shifts every alternate character by 8 bits to the left

>code 
	
'	
encoded_flag ='灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽'
flag = ""
for i in range(0, len(encoded_flag)):
    character1 = chr((ord(encoded_flag[i]) >> 8))
    character2 = chr(encoded_flag[i].encode('utf-16be')[-1])
    flag += character1
    flag += character2

print("Flag: " + flag)
'
