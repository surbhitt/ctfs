
---
# Metactf

> VMDK file format 

To identify any file there are some bytes in the starting of the file signature, called ==magic bytes==.

> Ransomware

The attacks have a technique ID ==T/XXX==.

> CVSSv3

The vulnerabilities have a code ==CVE-YYYY-XXXX==.

> Substitution cipher

The key is the reverse order of alphabets.

> How to ssh

`ssh ctf-1@host.cg21.metaproblems.com -p 7000`
ssh host@url {option} {port number if opt =-p}
when encountered with SSH host key err
`ssh -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" ctf-1@host.cg21.metaproblems.com -p 7000`

> debugging of code 

GDB (gnu debugger) used,
some options
- gdb `info functions`: returns the list of functions
- gdb `info registers`: returns the list of registers in use
- gdb `b *mem address`: used to set a break point at the mem address

> intercepting the traffic



### cryptography

> one time pad encryption / vernam cipher

The encryption is similar to vigener cipher with the key size => the length of message and one time use the key is randomly chosen. The key can not be reused. The key and plain text calculated as modulo 10/26/2. There are two keys one with sender and reciever.
XOR operator is an addtition operator with mod 2.

code to use cipher1 to find key to enc cipher2.

`
import re
c1 = "4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291"
c2 = "41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b"
p1 = "hey let's rob the bank at midnight tonight!"
c1 = [int("0x" + d, base=16) for d in re.split("(..)", c1)[1::2]]
c2 = [int("0x" + d, base=16) for d in re.split("(..)", c2)[1::2]]
p1 = [ord(c) for c in list(p1)]
key = [c ^ p for (c, p) in zip(c1, p1)]
p2 = [chr(c ^ k) for (c, k) in zip(c2, key)]
flag = ''.join(p2)
print(flag)
`
>RSA with ciphertxt e and n

