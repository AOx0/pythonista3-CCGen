
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
	