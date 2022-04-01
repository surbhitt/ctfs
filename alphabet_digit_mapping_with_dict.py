''' program for one to one mapping of the alphabets with the digits


    other ways to create dictionary are
		/////
    d = {} #empty dictionary
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
    d[alpha[i]] = i
		//////
    d = {enumerate(alpha)}
'''



from string import ascii_lowercase


f = open("message.txt", "rb")
l = [int(x) for x in (f.read().strip()).split()]

print("the text from the data file", l)

thedic = {k:v for k, v in enumerate(ascii_lowercase)}

print("the dic ", thedic) 
nn = 0
for j in range(26, 36):
	thedic[j] = "{here}".format(here = nn)
	nn+=1
thedic[36] = "_" 

print("THe complete dic ", thedic)

flag = ""

for x in l:
	flag += thedic[x%37]


print("\n")
print(flag)
