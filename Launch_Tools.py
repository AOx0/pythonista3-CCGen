
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
	console.alert('Informacion','Version 3.8\nBy Alecz\nPython 3.6.1\nPythonista 3\n(c)Alecz2018')
			
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
