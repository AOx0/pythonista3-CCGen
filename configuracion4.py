
from __future__ import print_function
import datetime
import ui
import console,notification
from random import choice
import sys
from scene import *
import Tools
from Tools import *
from Tools import configuracion3 as configuracion3
import console
from time import sleep
import clipboard

# The Caesar Cipher Algorithm
t = 3

    
def main(passe):
	global t
	message = passe
	key     = 10
	mode    = 'c'

	if mode.lower().startswith('c'):
		mode = "cifrar"
	elif mode.lower().startswith('d'):
		mode = "descifrar"

	message = encdec(message, key, mode)
	message = encdec2(message, key, mode)
	message = encdec3(message, key, mode)
	message = encdec4(message, key, mode)
	message = encdec5(message, key, mode)
	translated = encdec6(message, key, mode)
	
	if t !=0:
		for i in range(101):
			sleep(0.01)
		t = t - 1
		   
	passe = translated
	return passe
        
def encdec(message, key, mode):
    message    = message
    translated = ""
    LETTERS    = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890()!?,.@"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    
    message = translated        
    return message
    
def encdec2(message, key, mode):
    message    = message
    translated = ""
    LETTERS    = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890()!?,.@"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    
    message = translated        
    return message
    
def encdec3(message, key, mode):
    message    = message
    translated = ""
    LETTERS    = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890()!?,.@"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    
    message = translated        
    return message
    
def encdec4(message, key, mode):
    message    = message
    translated = ""
    LETTERS    = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890()!?,.@"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    
    message = translated        
    return message
    
def encdec5(message, key, mode):
    message    = message
    translated = ""
    LETTERS    = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890()!?,.@"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    
    message = translated        
    return message
    
def encdec6(message, key, mode):
    message    = message
    translated = ""
    LETTERS    = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890()!?,.@"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated

    

#s = run(MyScene())
        
passe=''
account1=''
account=''
save = ''
        

    

#s = run(MyScene())
def gen_pass():
	global passe,account1,account, save       
	account = console.input_alert('Tipo de Cuenta','Inserta el tipo de Cuenta')
	account1 = console.input_alert('Usuario','Inserta el correo,usuario,etc.')
	mode = console.alert('Caracteres Especiales','Selecciona Si/No','Si','No',hide_cancel_button=True)
	save = console.alert('Guardar en .txt?','Selecciona Si/No\nAl guardar se E: 10','Guardar','No Guardar',hide_cancel_button=True)
	n1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	n2 = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
	n3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	n4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	n5 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	n6 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	n7 = ['1','2','3','4','5','6','7','8','9','0']
	n8 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	n9 = ['1','2','3','4','5','6','7','8','9','0']
	n10 = ['1','2','3','4','5','6','7','8','9','0']
	n11 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	n12 = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
	n_e1 =['=','#']


	n1=choice(n1)
	n2=choice(n2)
	n3=choice(n3)
	n4=choice(n4)
	n5=choice(n5)
	n6=choice(n6)
	n7=choice(n7)
	n8=choice(n8)
	n9=choice(n9)
	n10=choice(n10)
	n11=choice(n11)

	caracters = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11]
	n1=choice(caracters)
	n2=choice(caracters)
	n3=choice(caracters)
	n4=choice(caracters)
	n5=choice(caracters)
	n6=choice(caracters)
	n7=choice(caracters)
	n8=choice(caracters)
	n9=choice(caracters)
	n10=choice(caracters)
	
	if mode == 1:
		passe = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11
	else:
		pass

		passe = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10

	if save == 1:
		lake(account,account1,passe)
	else:
		passs = [account,account1,passe]
		passs = str(passs)
		clipboard.set(passs)
		console.hud_alert('Copiado')
	
		

def lake(account,account1,passe):
	passe = main(passe)
	account = main(account)
	account1= main(account1)
	
	now = datetime.datetime.now()
	file_name='file_'+account+str(now.day) + str(now.hour) + str(now.minute) + str(now.second)+'.text'
	f =open(file_name,'w')
	f.write(account + '\n')
	f.write(account1+ '\n')
	f.write(str(passe))
	console.hud_alert('Listo')

def run_c():
	gen_pass()
