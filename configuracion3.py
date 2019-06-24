
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
