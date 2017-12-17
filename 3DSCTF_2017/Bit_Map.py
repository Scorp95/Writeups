import re	
import binascii
import requests
r=requests.get("http://bitmap01.3dsctf.org:8010/")
allcolors = re.search(r'<tr>(.*)</tr>',r.text)
allcolors=allcolors.group(1)
list=re.findall('"\#([^"]*)"', r.text)
with open('flag', 'wb') as program:
	for l in list:
		program.write(binascii.unhexlify(l))
program.close()

#root@Scorp:~# python Bit_Map.py
#root@Scorp:~# chmod +x flag && ./flag
#3DS{H1dd3n_1n_7ru3_C0l0r5}

