import random
import string
import pycurl 
from io import BytesIO 
	
def notrussion(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())
	
def send_register(userName, userPassword, lenkey):
	if not notrussion(userName) and not notrussion(userPassword) and lenkey > 0 and lenkey < 65:
		letters = string.ascii_uppercase
		KeyJoin = ''.join(random.choice(letters) for i in range(lenkey))
		value = BytesIO() 
		crl = pycurl.Curl() 
		crl.setopt(crl.URL, 'http://testm.myjino.ru/index.php?nameUser=' + userName + '&passwordUser=' + userPassword + '&keyJoin=' + KeyJoin)
		crl.setopt(crl.WRITEDATA, value)
		crl.perform() 
		crl.close() 
		return value.getvalue().decode('utf8')
	else:
		return 'RegisterError'
	
def send_login(userName, userPassword):
	if not notrussion(userName) and not notrussion(userPassword):
		value = BytesIO() 
		crl = pycurl.Curl() 
		crl.setopt(crl.URL, 'http://testm.myjino.ru/index.php?nameUser=' + userName + '&passwordUser=' + userPassword)
		crl.setopt(crl.WRITEDATA, value)
		crl.perform() 
		crl.close() 
		return value.getvalue().decode('utf8')
	else:
		return 'AutorizationError'