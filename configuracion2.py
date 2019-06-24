
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

