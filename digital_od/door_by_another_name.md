
>*writeup*: [writeup](https://atomicnicos.me/postx/2021/2021_10_11%2Bdigital-overdose-official-writeup-2-a-lying-cake)

***
> context: something to do with the game halo

>
 *"Zero-width space" characters*: which can be found in unicode U+200B, U+200C, U+2060 and U+FEFF.
 [zws](https://stackoverflow.com/questions/11392312/zero-width-non-breaking-space)
 prohibited use in domain names as it can lead to a homograph attack.

***

> the above is a text with zero width spacing. when opened in sublime text there are <0x200b> unicode character, counting the number of these characters and converting them to ascii charaacter the flag is reveled.

>*python code*:
	'
	text = "T​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​h​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​e​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​c​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​a​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​k​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​e​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​i​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​s​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​a​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​l​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​i​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​	e"
	result = []
	alphabet = list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1)) + [ord(" ")]
	
	# ord: Return the integer that represents the character

	for i in range(len(text)):
	    if ord(text[i]) in alphabet and i < len(text):
	        result += [0]
	    else:
		result[-1] += 1

	print("".join([chr(a) for a in result]))
	'

> flag: DO{1$_1NV1$1BL3}

 