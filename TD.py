# -*- coding: utf-8 -*-
###############################################################################
# Esta es una aplicacion que extrae Tools y los almacena en tu carpeta de Python para su uso.
# Corre este script una vez para extraer el programa
# Es OBLIGATORIO tener Pythonista3, por OMZ Software.
# Se extraerán 5 archivos con terminacion .py y 5 archivos con terminación .pyui
# Asegúrate que los nombres de los archivos no existen en tus carpetas.
# Para actualizar el programa borra primero los archivos viejos
# Este script puede ser borrado despues de la extraccion
###############################################################################
# Empaquetado usando PackUI. By dgelessus
# Empaquetado & Creado por @Alecz
###############################################################################
#Novedades
#1.0 : Main Programme
#1.1 : Empaquetado con PackUI para su distribucion. Correcion de Errores
#1.2 : Correcion de Errores y del Programa en gral. para mejorar la compatibilidad. (Se solucionara)
#1.3 : Correcion de Errores. Mejorada un poco la interfaz
#1.4 : Mejora de aspecto.
#1.5 : Mejoras y cambios pequeños.
#1.6 : Mejoras y cambios pequeños.
#2.0 : Nueva interfaz. Aun es txt
#2.1 : Mejoras pequeñas
#2.2 : Mejoras pequeñas
#3.0 : Nueva interfaz: Ahora todo es gráfico
#3.1 : Mejoras y cambios pequeños
#3.2 : Mejoras y cambios pequeños
#3.3 : Empaquetado con PackUI para su distribución. 
#3.4 : Mejora de compatibilidad
#3.5 : Mejora de compatibilidad de texto.
###############################################################################
#Manual:


import console, os.path
import shutil
INIT		 = "__init__"
NAME     = "Launch_Tools"
NAME2		 = "configuracion1"
NAME3		 = "configuracion2"
NAME4	 	 = "configuracion3"
NAME5		 = "configuracion4"
NAME6    = "Launch_Tools"
NAME7		 = "configuracion1"
NAME8		 = "configuracion2"
NAME9	 	 = "configuracion3"
NAME10	 = "configuracion4"
NAME11	 = "Manual"
PYFILE   = """
import Tools
from Tools import *
from Tools import configuracion1 as configuracion1
from Tools import configuracion2 as configuracion2
from Tools import configuracion3 as configuracion3
from Tools import configuracion4 as configuracion4
import ui
import console
import sys


def start(sender):
	D = console.alert('Que quieres hacer?', 'Elige la opcion que desees', 'CCGen Tools', 'Encode Tools')
	
	if D == 1:
		ccgen_tools()
	elif D == 2:
		encode_tools()

def info_b(sender):
	console.alert('Informacion','Version 3.8\\nBy Alecz\\nPython 3.6.1\\nPythonista 3\\n(c)Alecz2018')
			
def encode_tools():
	F = console.alert('Que quieres hacer?','Elige la opcion que desees','Encriptar','PassGen')
	
	if F == 1:
		configuracion3.run_b()
	elif F == 2:
		configuracion4.run_c()
	else:
		sys.exit()
		
def ccgen_tools():
	E = console.alert('Que quieres hacer?', 'Elige la opcion que desees', 'Extrapolador', 'CCGen')
	
	if E == 2:
		configuracion1.run_a()
	elif E == 1:
		configuracion2.run_extra_a()
	else:
		sys.exit()
		
def run_alll():
	if __name__ == '__main__':
		v = ui.load_view()
		v.present('sheet', hide_title_bar=True)
run_alll()
"""

PYFILE2 = """
import ui
import getopt
import sys
import datetime
from random import randint
import clipboard
from time import sleep
import console

ccv = ''
date = ''


def cardLuhnChecksumIsValid(card_number):
	sum = 0
	num_digits = len(card_number)
	oddeven = num_digits & 1
	
	for count in range(0, num_digits):
		digit = int(card_number[count])
		
		if not (( count & 1 ) ^ oddeven ):
			digit = digit * 2
		if digit > 9:
			digit = digit - 9
			
		sum = sum + digit
		
	return ( (sum % 10) == 0 )

#Random ccv gen
def ccvgen():
	global ccv
	num = randint(10,999)
	
	if num < 100:
		ccv = "0" + str(num)
	else:
		ccv = str(num)
		
	return(ccv)

#Random exp date
def dategen():
	global date
	now = datetime.datetime.now()
	month = str(randint(1, 12))
	current_year = str(now.year)
	year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
	date = month + "|" + year
	
	return(date)

def addbutton_tapped(sender):
	global ca,cb
	input = sender.superview['textview1'].text
	bin_format = input
	out_cc=''
	if len(bin_format) == 16:
		#Iteration over the bin
		for i in range(15):
			if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
				out_cc = out_cc + bin_format[i]
				continue
			elif bin_format[i] in ("x"):
				out_cc = out_cc + str(randint(0,9))			
				
		for i in range(10):
			checksum_check = out_cc
			checksum_check = checksum_check + str(i)
			
			if cardLuhnChecksumIsValid(checksum_check):
				out_cc = checksum_check
				break
			else:
				checksum_check = out_cc
    
	if cb == 1:
		ccvgen()
		
	if ca == 1:
		dategen()
	
	out_cc = out_cc+'|'+ccv+'|'+date
	
	table = sender.superview['table'].data_source.items
	table.append(out_cc)

def copy_ccs(sender):
	table = sender.superview['table'].data_source.items
	clipboard.set(str(table))

def run_a():
	global ca,cb
	ca = console.alert('Quieres Generar FV?','','Si','No',hide_cancel_button=True)

	cb = console.alert('Quieres Generar CVV?','','Si','No',hide_cancel_button=True)
	
	
	
	v = ui.load_view()
	v.background_color = 'white'
	v.present('sheet',hide_title_bar=True)
	
	return ca,cb
	"""
		
PYFILE3 = """
import ui
import clipboard
import console

def extra_a(sender):
	cc1 = sender.superview['textview1'].text
	Grupo1 = cc1[0:8]
	Grupo2= cc1[8:16]
	CC1= cc1[:]
	
	cc2 = sender.superview['textview2'].text
	Grupo3= cc2[0:8]
	Grupo4= cc2[8:16]
	CC2= cc2[:]
	
	try:
		m1= int(Grupo1[0])*int(Grupo4[0])
		m2= int(Grupo1[1])*int(Grupo4[1])
		m3= int(Grupo1[2])*int(Grupo4[2])
		m4= int(Grupo1[3])*int(Grupo4[3])
		m5= int(Grupo1[4])*int(Grupo4[4])
		m6= int(Grupo1[5])*int(Grupo4[5])
		m7= int(Grupo1[6])*int(Grupo4[6])
		m8= int(Grupo1[7])*int(Grupo4[7])
	except IndexError:
		console.alert('Error','Introduce un Bin valido')
	except ValueError:
		console.alert('Error','Introduce un Bin valido')
	Dil=str(m1)+str(m2)+str(m3)+str(m4)+str(m5)+str(m6)+str(m7)+str(m8)
	
	for i1 in [Dil]:
		Ex1= i1[0:8]
		
	CCR=str(Grupo1)+str(Ex1)
	Ex2= ('x')
	
	try:
		a1=CCR[0];	 b1=CC1[0]
		a2=CCR[1];	 b2=CC1[1]
		a3=CCR[2];	 b3=CC1[2]
		a4=CCR[3];	 b4=CC1[3]
		a5=CCR[4];	 b5=CC1[4]
		a6=CCR[5];	 b6=CC1[5]
		a7=CCR[6];	 b7=CC1[6]
		a8=CCR[7];	 b8=CC1[7]
		a9=CCR[8];		b9=CC1[8]
		a10=CCR[9];		b10=CC1[9]
		a11=CCR[10];	b11=CC1[10]
		a12=CCR[11];	b12=CC1[11]
		a13=CCR[12];	b13=CC1[12]
		a14=CCR[13];	b14=CC1[13]
		a15=CCR[14];	b15=CC1[14]
		a16=CCR[15];	b16=CC1[15]
	except IndexError:
		console.alert('Error','Introduce un Bin valido')
	if a1 != b1:
		a1=str(Ex2)
	
	if a2 != b2:
		a2=str(Ex2)
	
	if a3 != b3:
		a3=str(Ex1)
	
	if a4 != b4:
		a4=str(Ex2)
	
	if a5 != b5:
		a5=str(Ex2)
	
	if a6 != b6:
		a6=str(Ex2)
	
	if a7 != b7:
		a7=str(Ex2)
	
	if a8 != b8:
		a8=str(Ex2)
	
	if a9 != b9:
		a9=str(Ex2)
	
	if a10 != b10:
		a10=str(Ex2)
	
	if a11 != b11:
		a11=str(Ex2)
	
	if a12 != b12:
		a12=str(Ex2)
	
	if a13 != b13:
		a13=str(Ex2)
	
	if a14 != b14:
		a14=str(Ex2)
	
	if a15 != b15:
		a15=str(Ex2)
	
	if a16 != b16:
		a16=str(Ex2)
	
	if a16==Ex2:
		Ex3=('1')
		a16=str(Ex3)
	CCFG=str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+str(a8)+str(a9)+str(a10)+str(a11)+str(a12)+str(a13)+str(a14)+str(a15)+str(a16)
	
	table = sender.superview['tableview1'].data_source.items
	table.append(CCFG)
	
def extra_b(sender):
	cc1 = sender.superview['textview1'].text
	try:
		Save1= cc1[9]
		Save2= cc1[10]
		Save4= cc1[0:8]
		CC111 = cc1[:]
	except IndexError:
		console.alert('Error','Introduce un Bin valido')
	
	cc2 = sender.superview['textview2'].text
	Save1_2= cc2[9]
	Save2_2= cc2[10]
	CC222 = cc2[:]
	
	CCF1=(((int(Save1)+int(Save1_2))/2)*5)
	CCF2=(((int(Save2)+int(Save2_2))/2)*5)

	
	CCF= int(CCF1)+int(CCF2)
	X1= 'xxxxxx'
	CCFG = str(Save4)+str(CCF)+str(X1)
	
	table = sender.superview['tableview1'].data_source.items
	table.append(CCFG)
	
def extra_c(sender):
	cc1 = sender.superview['textview1'].text
	Grupo1 = cc1[0:8]
	Grupo2= cc1[8:16]
	CC1= cc1[:]
	
	cc2 = sender.superview['textview2'].text
	Grupo3= cc2[0:8]
	Grupo4= cc2[8:16]
	CCR= cc2[:]
	
	try:
		a1=CCR[0];	 b1=CC1[0]
		a2=CCR[1];	 b2=CC1[1]
		a3=CCR[2];	 b3=CC1[2]
		a4=CCR[3];	 b4=CC1[3]
		a5=CCR[4];	 b5=CC1[4]
		a6=CCR[5];	 b6=CC1[5]
		a7=CCR[6];	 b7=CC1[6]
		a8=CCR[7];	 b8=CC1[7]
		a9=CCR[8];		b9=CC1[8]
		a10=CCR[9];		b10=CC1[9]
		a11=CCR[10];	b11=CC1[10]
		a12=CCR[11];	b12=CC1[11]
		a13=CCR[12];	b13=CC1[12]
		a14=CCR[13];	b14=CC1[13]
		a15=CCR[14];	b15=CC1[14]
		a16=CCR[15];	b16=CC1[15]
	except IndexError:
		console.alert('Error','Introduce un Bin valido')
	Ex2='x'
	
	if a1 != b1:
		a1=str(Ex2)
	
	if a2 != b2:
		a2=str(Ex2)
	
	if a3 != b3:
		a3=str(Ex1)
	
	if a4 != b4:
		a4=str(Ex2)
	
	if a5 != b5:
		a5=str(Ex2)
	
	if a6 != b6:
		a6=str(Ex2)
	
	if a7 != b7:
		a7=str(Ex2)
	
	if a8 != b8:
		a8=str(Ex2)
	
	if a9 != b9:
		a9=str(Ex2)
	
	if a10 != b10:
		a10=str(Ex2)
	
	if a11 != b11:
		a11=str(Ex2)
	
	if a12 != b12:
		a12=str(Ex2)
	
	if a13 != b13:
		a13=str(Ex2)
	
	if a14 != b14:
		a14=str(Ex2)
	
	if a15 != b15:
		a15=str(Ex2)
	
	if a16 != b16:
		a16=str(Ex2)

	CCFF = str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+str(a8)+str(a9)+str(a10)+str(a11)+str(a12)+str(a13)+str(a14)+str(a15)+str(a16)
	
	table = sender.superview['tableview1'].data_source.items
	table.append(CCFF)

def copy_ccs(sender):
	table = sender.superview['tableview1'].data_source.items
	clipboard.set(str(table))

def run_extra_a():
	v = ui.load_view()
	v.present('sheet',hide_title_bar=True)

"""

PYFILE4 = """
from __future__ import print_function
import ui
import console
from time import sleep
import clipboard

# The Caesar Cipher Algorithm
translated = ''
key     = ''
mode    = ''

def main(sender):
	global translated, key, mode
	message = sender.superview['textview1'].text
	key     = console.input_alert('0.70','')
	key 		= int(key)
	mode    = console.alert('E/C','Deseas encriptar o desencriptar?','Encriptar','Desencriptar')
	


	message = encdec(message, key, mode)
	message = encdec2(message, key, mode)
	message = encdec3(message, key, mode)
	message = encdec4(message, key, mode)
	message = encdec5(message, key, mode)
	translated = encdec6(message, key, mode)
	
		   
	if mode == 1:
		sender.superview['textview2'].text = translated
	elif mode == 2:
		sender.superview['textview2'].text = translated
        
def encdec(message, key, mode):
    message    = message
    translated = ""
    LETTERS    = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890()!?,.@"
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode ==  1:
                num = num + key
            elif mode == 2:
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
            if mode ==   1:
                num = num + key
            elif mode == 2:
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
            if mode ==   1:
                num = num + key
            elif mode == 2:
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
            if mode ==   1:
                num = num + key
            elif mode == 2:
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
            if mode ==   1:
                num = num + key
            elif mode == 2:
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
            if mode ==   1:
                num = num + key
            elif mode == 2:
                num = num - key

            if num >= len(LETTERS):
                num -= len(LETTERS)
            elif num < 0:
                num += len(LETTERS)

            translated += LETTERS[num]
        else:
            translated += symbol
    return translated

def copy_ccs(sender):
	table = sender.superview['textview2'].text
	clipboard.set(str(table))

def run_b():
	v = ui.load_view()
	v.present('sheet',hide_title_bar=True)
"""

PYFILE5 = """
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
	save = console.alert('Guardar en .txt?','Selecciona Si/No\\nAl guardar se E: 10','Guardar','No Guardar',hide_cancel_button=True)
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
	f.write(account + '\\n')
	f.write(account1+ '\\n')
	f.write(str(passe))
	console.hud_alert('Listo')

def run_c():
	gen_pass()
"""
PYFILE6="""
[
  {
    "nodes" : [
      {
        "nodes" : [

        ],
        "frame" : "{{125, 295.66666666666663}, {70, 40}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "7C11980F-EE9E-4467-8A10-EFBF92C8A6FF",
          "image_name" : "iob:close_24",
          "font_size" : 20,
          "corner_radius" : 0,
          "frame" : "{{80, 104}, {80, 32}}",
          "tint_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "border_width" : 0,
          "title" : "",
          "action" : "start",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button1",
          "flex" : "LRTB"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{83, 137.66666666666663}, {150, 150}}",
        "class" : "Button",
        "attributes" : {
          "flex" : "LRTB",
          "action" : "info_b",
          "name" : "button2",
          "frame" : "{{121, 221}, {80, 32}}",
          "tint_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "",
          "uuid" : "EAF435B9-D6C7-4458-9E09-124F536289D4",
          "class" : "Button",
          "font_size" : 15,
          "image_name" : "iob:ios7_cog_outline_256"
        },
        "selected" : true
      }
    ],
    "frame" : "{{0, 0}, {321, 473}}",
    "class" : "View",
    "attributes" : {
      "enabled" : true,
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    },
    "selected" : false
  }
]
"""
PYFILE7="""
[
  {
    "nodes" : [
      {
        "nodes" : [

        ],
        "frame" : "{{30, 26}, {334, 45}}",
        "class" : "TextView",
        "attributes" : {
          "uuid" : "575C226B-9CEE-43F1-AF53-E93E88ED4F39",
          "font_size" : 17,
          "corner_radius" : 10,
          "frame" : "{{95, 178}, {200, 200}}",
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "editable" : true,
          "border_width" : 1,
          "custom_attributes" : "",
          "alignment" : "center",
          "autocorrection_type" : "no",
          "text" : "",
          "text_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "font_name" : "<System>",
          "spellchecking_type" : "no",
          "class" : "TextView",
          "name" : "textview1",
          "flex" : "W"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{30, 79}, {128, 32}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "E5E8E967-3A83-4410-B918-2873AC326B48",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "frame" : "{{155, 262}, {80, 32}}",
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "border_width" : 1,
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "title" : "Generar",
          "action" : "addbutton_tapped",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button1",
          "flex" : "W"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{32, 119}, {332, 378}}",
        "class" : "TableView",
        "attributes" : {
          "uuid" : "ECD05B24-CA90-46AE-8E08-0D18841AC5E2",
          "editing" : false,
          "corner_radius" : 10,
          "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "frame" : "{{95, 178}, {200, 200}}",
          "data_source_items" : "CCs Generadas:",
          "data_source_number_of_lines" : 1,
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "border_width" : 1,
          "data_source_move_enabled" : true,
          "alpha" : 1,
          "data_source_delete_enabled" : true,
          "data_source_font_size" : 18,
          "row_height" : 40,
          "class" : "TableView",
          "name" : "table",
          "flex" : "WH"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{236, 79}, {128, 32}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "75D8B824-BBF1-4027-87A4-ED85A7C48A09",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.505447,0.505447,0.505447,1.000000)",
          "frame" : "{{155, 262}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_width" : 0,
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "Copy",
          "action" : "copy_ccs",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button2",
          "flex" : "W"
        },
        "selected" : true
      }
    ],
    "frame" : "{{0, 0}, {392, 503}}",
    "class" : "View",
    "attributes" : {
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "enabled" : true,
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "name" : "CCGen",
      "flex" : ""
    },
    "selected" : false
  }
]
"""
PYFILE8="""
[
  {
    "nodes" : [
      {
        "nodes" : [

        ],
        "frame" : "{{20, 81}, {321, 47}}",
        "class" : "TextView",
        "attributes" : {
          "uuid" : "9AFF2075-876F-457A-BF0A-4797C4B433D3",
          "font_size" : 17,
          "corner_radius" : 10,
          "frame" : "{{20, 20}, {200, 200}}",
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "editable" : true,
          "border_width" : 1,
          "custom_attributes" : "",
          "alignment" : "center",
          "autocorrection_type" : "no",
          "text" : "",
          "text_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "font_name" : "<System>",
          "spellchecking_type" : "no",
          "class" : "TextView",
          "name" : "textview1",
          "flex" : "W"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{20, 26}, {321, 47}}",
        "class" : "TextView",
        "attributes" : {
          "uuid" : "3981AC6B-FBBA-4272-B726-2BE158DD6ECB",
          "font_size" : 17,
          "corner_radius" : 10,
          "frame" : "{{20, 20}, {200, 200}}",
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "editable" : true,
          "border_width" : 1,
          "custom_attributes" : "",
          "alignment" : "center",
          "autocorrection_type" : "no",
          "text" : "",
          "text_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "font_name" : "<System>",
          "spellchecking_type" : "no",
          "class" : "TextView",
          "name" : "textview2",
          "flex" : "W"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{6, 143}, {79.666666666666657, 39}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "7EFACBBD-E1C3-4779-A666-40749D7DDC4C",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "frame" : "{{124, 194}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_width" : 1,
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "Ex.Av",
          "action" : "extra_a",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button1",
          "flex" : "WLRB"
        },
        "selected" : true
      },
      {
        "nodes" : [

        ],
        "frame" : "{{20, 209}, {321, 274}}",
        "class" : "TableView",
        "attributes" : {
          "uuid" : "0468A0F6-6832-4937-982B-70D8A1939AF2",
          "corner_radius" : 10,
          "background_color" : "RGBA(1.0, 1.0, 1.0, 1.0)",
          "frame" : "{{64, 110}, {200, 200}}",
          "data_source_items" : "Resultado Extrapolaciones:",
          "data_source_number_of_lines" : 1,
          "border_width" : 1,
          "data_source_delete_enabled" : true,
          "data_source_font_size" : 18,
          "row_height" : 40,
          "class" : "TableView",
          "name" : "tableview1",
          "flex" : "WH"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{93.666666666666671, 143}, {79.666666666666643, 39}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "408C20A0-3211-421E-9E1C-C08303C6A0D7",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "frame" : "{{124, 194}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_width" : 1,
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "Ex.Av2",
          "action" : "extra_b",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button2",
          "flex" : "WLRB"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{181.33333333333331, 143}, {79.666666666666629, 39}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "F0699D3F-F1FC-4FF6-BD06-C105787034FA",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.009804,0.009804,0.009804,1.000000)",
          "frame" : "{{124, 194}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_width" : 1,
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "Ex.Ba",
          "action" : "extra_c",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button3",
          "flex" : "WLRB"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{287.66666666666674, 143}, {67.333333333333314, 39}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "3272002F-174E-4B79-8D6A-BDA062DB9192",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.504357,0.504357,0.504357,1.000000)",
          "frame" : "{{124, 194}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_width" : 0,
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "Copy",
          "action" : "copy_ccs",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button4",
          "flex" : "WLRB"
        },
        "selected" : false
      }
    ],
    "frame" : "{{0, 0}, {361, 516}}",
    "class" : "View",
    "attributes" : {
      "name" : "Extrapolador",
      "enabled" : true,
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    },
    "selected" : false
  }
]
"""
PYFILE9="""
[
  {
    "nodes" : [
      {
        "nodes" : [

        ],
        "frame" : "{{22, 25}, {241, 32}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "39C6AF88-B7B1-4782-8893-35924063F9DF",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "frame" : "{{103, 153}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_width" : 1,
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "Generar",
          "action" : "main",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button1",
          "flex" : "WB"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{22, 105}, {115, 100}}",
        "class" : "TextView",
        "attributes" : {
          "uuid" : "5FBCB733-3CB5-4D8F-BE4B-647424100A03",
          "font_size" : 17,
          "corner_radius" : 10,
          "frame" : "{{43, 69}, {200, 200}}",
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "editable" : true,
          "border_width" : 1,
          "custom_attributes" : "",
          "alignment" : "center",
          "autocorrection_type" : "no",
          "text" : "",
          "text_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "font_name" : "<System>",
          "spellchecking_type" : "no",
          "class" : "TextView",
          "name" : "textview1",
          "flex" : "WHR"
        },
        "selected" : true
      },
      {
        "nodes" : [

        ],
        "frame" : "{{148, 105}, {115, 100}}",
        "class" : "TextView",
        "attributes" : {
          "uuid" : "E89D4BB3-5C4F-4CDA-A0FF-E9B0A9F06231",
          "font_size" : 17,
          "corner_radius" : 10,
          "frame" : "{{43, 69}, {200, 200}}",
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "editable" : true,
          "border_width" : 1,
          "custom_attributes" : "",
          "alignment" : "center",
          "autocorrection_type" : "no",
          "text" : "",
          "text_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "font_name" : "<System>",
          "spellchecking_type" : "no",
          "class" : "TextView",
          "name" : "textview2",
          "flex" : "WHL"
        },
        "selected" : false
      },
      {
        "nodes" : [

        ],
        "frame" : "{{22, 65}, {241, 32}}",
        "class" : "Button",
        "attributes" : {
          "uuid" : "B8514DD4-50F0-4EA0-BC4C-57D98100CCE0",
          "font_size" : 15,
          "corner_radius" : 5,
          "background_color" : "RGBA(0.505447,0.505447,0.505447,1.000000)",
          "frame" : "{{103, 153}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "border_width" : 0,
          "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
          "title" : "Copy",
          "action" : "copy_ccs",
          "font_bold" : true,
          "class" : "Button",
          "name" : "button2",
          "flex" : "WB"
        },
        "selected" : false
      }
    ],
    "frame" : "{{0, 0}, {285, 338}}",
    "class" : "View",
    "attributes" : {
      "enabled" : true,
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    },
    "selected" : false
  }
]
"""
PYFILE10="""
[
    {
        "class": "View",
        "attributes": {
            "background_color": "RGBA(1.000000,1.000000,1.000000,1.000000)",
            "tint_color": "RGBA(0.000000,0.478000,1.000000,1.000000)",
            "enabled": true,
            "border_color": "RGBA(0.000000,0.000000,0.000000,1.000000)",
            "flex": ""
        },
        "frame": "{{0, 0}, {240, 240}}",
        "nodes": [

        ]
    }
]
"""
PYFILE11="""
Este es el Manual de uso de Las Herramientas para Carding del Team. 
"""

PYFILE12="""
from __future__ import absolute_import
"""


def fix_quotes_out(s):
	return s.replace("\\\"\\\"\\\"", "\"\"\"").replace("\\\\", "\\")

def main():
	d1 = False
	d2 = False
	dest_path_short1 = '~/Documents/Δ'
	dest_path1 =os.path.expanduser(dest_path_short1)
	if os.path.isdir(dest_path1):
		shutil.rmtree(dest_path1)
		d1 = True
	if not os.path.isdir(dest_path1):
		os.mkdir(dest_path1) 
	
	dest_path_short2 = '~/Documents/site-packages-3/Tools'
	dest_path2 =os.path.expanduser(dest_path_short2)
	if os.path.isdir(dest_path2):
		shutil.rmtree(dest_path2)
		d2 = True 
	if not os.path.isdir(dest_path2):
		os.mkdir(dest_path2)
	
	
	if os.path.exists(NAME + ".py"):
		console.alert("Instalación Incompleta", NAME + ".py already exists.")
		return
	
	
	filename	=os.path.join(dest_path1,NAME)
	filename2	=os.path.join(dest_path2,NAME2)
	filename3	=os.path.join(dest_path2,NAME3)
	filename4	=os.path.join(dest_path2,NAME4)
	filename5	=os.path.join(dest_path2,NAME5)
	filename6	=os.path.join(dest_path1,NAME6)
	filename7	=os.path.join(dest_path2,NAME7)
	filename8	=os.path.join(dest_path2,NAME8)
	filename9	=os.path.join(dest_path2,NAME9)
	filename10=os.path.join(dest_path2,NAME10)
	filename11=os.path.join(dest_path1,NAME11)
	#filename12=os.path.join(dest_path2,INIT)
	
		
		
	with open(filename + ".py", "w") as f:
		f.write(fix_quotes_out(PYFILE))
		
	with open(filename2 + ".py", "w") as f:
		f.write(fix_quotes_out(PYFILE2))
		
	with open(filename3 + ".py", "w") as f:
		f.write(fix_quotes_out(PYFILE3))
	
	with open(filename4 + ".py", "w") as f:
		f.write(fix_quotes_out(PYFILE4))
		
	with open(filename5 + ".py", "w") as f:
		f.write(fix_quotes_out(PYFILE5))
	
	with open(filename6 + ".pyui", "w") as f:
		f.write(fix_quotes_out(PYFILE6))
	
	with open(filename7 + ".pyui", "w") as f:
		f.write(fix_quotes_out(PYFILE7))
		
	with open(filename8 + ".pyui", "w") as f:
		f.write(fix_quotes_out(PYFILE8))
		
	with open(filename9 + ".pyui", "w") as f:
		f.write(fix_quotes_out(PYFILE9))
	
	with open(filename10 + ".pyui", "w") as f:
		f.write(fix_quotes_out(PYFILE10))
	
	with open(filename11, "x") as f:
		f.write(fix_quotes_out(PYFILE11))
	
	#with open(filename12 + ".py", "w") as f:
		f.write(fix_quotes_out(PYFILE12)) 
	
	if d1 == True and d2 == True:
		ms	= 'Actualización Completa'
		msg = 'Δ Tools fue exitosamente actualizado'
	else:
		ms 	= 'Instalación Completa'
		msg = 'Δ Τools fue exitosamente instalado'
	console.alert(ms, msg, "OK", hide_cancel_button=True)
	
if __name__ == "__main__":
    main()
