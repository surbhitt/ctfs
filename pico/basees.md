
> base 64 decoding using command line
	
	echo -n 'bDNhcm5fdGgzX3IwcDM1' | base64 --decode

> base 64 decod using python

	import base64

	e='bDNhcm5fdGgzX3IwcDM1'
	d=base64.b64decode(e)
	print(e)