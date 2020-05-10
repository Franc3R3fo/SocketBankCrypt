help_error = """

ERRORS SCHEME: 

- 01 - MSG length doesn't match ENCODED_MSG length.

- 02 - ENCODED_MSG length doesn't match with HASH TABLE.

- 03 - ENCODED_MSG length doesn't match DECODED_MSG length.

- 04 - MSG is equal to \"\"

- 05 - ENCODED_MSG is equal to \"\"

"""
# importation #
from random import randint
import os

# globals definitions #

global chars,error_codes,error_codes_n

# determinant variable #

def string(table):
	s = "[ "
	for obj in table:
		s+="[\'"+obj[0]+"\',\'"+obj[1]+"\'],"
	return s

error_codes = [ ["MSG length doesn't match ENCODED_MSG length.",1],["ENCODED_MSG length doesn't match with HASH TABLE.",2],["ENCODED_MSG length doesn't match DECODED_MSG length.",3],["MSG is equal to \"\"",4],["ENCODED_MSG is equal to \"\"",5] ]
error_codes_n = []
for obj in error_codes:
	error_codes_n.append(obj[1])
chars = "abcdefghijklmnopqrstuvwxyz"                  # lowercase alphabate
chars +="ABCDEFGHIJKLMNOPQRSTUVWXYZ"                  # uppercase alphabate
chars +="0123456789"                                  # numbers
chars +=",.-;:_<>!£$%&/()=?^ì\'\"\\|è+òàùé*ç°§[]@#{}€\t\n " # special chars

# functions table and input #

def PrintError(n):
	new = sorted(error_codes,key=lambda k: k[1]==n)
	print(new[-1][0])

def unload_key_from(table):
	s = ""
	for obj in table:
		s+=obj[1]
	return s

def load_table_from(key):
	t = []
	n = int(len(key)/len(chars))
	q = 0
	for obj in chars:
		k = key[q:q+n]
		t.append([obj,k])
		q+=n
	return t

def get_multi_line_input():
	s = ""
	inp = "" 
	print("Insert your input message, terminate it with a ending \"EOF\" only line.")
	while(inp!="EOF"):
		inp = input("")
		if inp!="EOF":
			s+="\n"+inp
	return s

def get_key_comp(n):
	s = ""
	for i in range(0,n):
		x = randint(0,len(chars)-1)
		s+=chars[x]
	return s

def get_key(n):
	a = []
	b = []
	for obj in chars:
		key = get_key_comp(n)
		while(key in b):
			key = get_key_comp(n)
		a.append([obj,key])
		b.append(key)
	# print("HASH TABLE GENERATED : ",a)
	return a

# functions encode decode #

def get_encoded_char(char,table):
	new = sorted(table, key=lambda k: k[0]!=char)
	return new[0][1]

def get_decoded_char(char,table):
	new = sorted(table, key=lambda k: k[1]!=char)
	return new[0][0]

def chain(str3,str2,n):
	l = len(str3)
	block,str1 = str3[0:l-n],str3[l-n:l]
	return block + str1[0:n-1] + str2[0] + str1[n-1] + str2[1:n]

def de_chain(to_be,n):
	str1,str2,block = to_be[0:n],to_be[n:2*n],to_be[2*n:len(to_be)]
	return str1[0:n-1] + str2[0] + str1[n-1] + str2[1:n] + block

def encode(msg,table):
	if len(msg)==0:
		return 4
	n = len(table[0][1])
	enc_msg = ""
	bec = []
	for obj in msg:
		bec.append(get_encoded_char(obj,table))
	while(len(bec)>1):
		bec = [chain(bec[0],bec[1],n)] + bec[2:len(bec)]
	if len(bec[0])==(len(msg)*n):
		return bec[0]
	else:
		return 1

def decode(ori,table):
	if len(ori)==0:
		return 5
	msg = ori
	n = len(table[0][1])
	
	if len(msg)%n!=0:
		return 2
	
	t_msg,i,cur_i = [],n,0
	sup_t = ""
	
	for obj in msg:
		if i==cur_i:
			t_msg.append(sup_t)
			sup_t = obj
			cur_i = 0
		else:
			sup_t+=obj
		cur_i+=1
	if len(sup_t)>0:
		t_msg.append(sup_t)
	
	while(len(t_msg)>1):
		l = len(t_msg)
		t_msg = t_msg[0:l-2] + [de_chain(t_msg[l-2]+t_msg[l-1],n)]
	t_msg = t_msg[0]
	msg,i,cur_i = [],n,0
	sup_t = ""
	for obj in t_msg:
		if i==cur_i:
			msg.append(sup_t)
			sup_t = obj
			cur_i = 0
		else:
			sup_t+=obj
		cur_i+=1
	if len(sup_t)>0:
		msg.append(sup_t)
	decoded_msg = ""
	for obj in msg:
		decoded_msg += get_decoded_char(obj,table)
	if len(ori)/n==len(decoded_msg)or True:
		return decoded_msg
	else:
		return 3

if __name__ == '__main__':
	#RANDOMI TABLE
	table = get_key(7)
	
	file = open(r"C:\Users\Francesco\Desktop\DATABASE.crypt","a")
	file_out = open(r"C:\Users\Francesco\Desktop\DATABASE.vita","a")
	# table = [['a', ',{à\\q#*PWrò"JNLE?'], ['b', 'XNà1MWxZC,(MOnV5€'], ['c', '@M§*Kù9Mmq1X"/iç+'], ['d', 'i$Nu<;€gPF£.yu|34'], ['e', 'Rc_Hf]xu>}(ùgR#h?'], ['f', 'g26.J°R{éè:N7n45p'], ['g', "\\€PBrj1:€z&K'\tfMB"], ['h', 'u3vò>6i\tEàcn_tPD}'], ['i', 'e8n=YXv[n=ez|r&Vù'], ['j', 'BJ* HFOfBM;eBZcyj'], ['k', '{s;Lk[B3°ò\nò+ùv#.'], ['l', 'ù3uqwYd0Xzdsèùù&^'], ['m', 'qIQ-yW1enF[Z\t<d1.'], ['n', '55y&32w-:nw/YT\\1I'], ['o', "]]&D,wLQ00S'l2ùa$"], ['p', "<KuJPB F^' t?u:1Y"], ['q', ']L/ù+d$[^7ùSA6x^G'], ['r', 'OX+-qVy(,TA0zfi09'], ['s', '([#adhU5.t=§=£8l0'], ['t', '.I€WYò*x{s2My^1g2'], ['u', '<jl=u6&!°X23A£x5b'], ['v', "C'Hdm#Sò38tiò#eJl"], ['w', 'N*jYOe.;lé^n[-C/A'], ['x', 'fmH$6B8my>c!2"ItX'], ['y', "nmà2Qj+'+>W_Q>>1m"], ['z', 'ZWìUòN53CQàbq{%J['], ['A', '#5£4?€E}8Wq3p>Qg°'], ['B', ",DT,.;Ye°c)$1q'b_"], ['C', "à_ 4O£<7}vr'YQCK*"], ['D', ':q>OéEfdìk5T)scEI'], ['E', '+@\t>5kZò;8à6ì0?ì?'], ['F', '-|@.6:fimG1q)y9#L'], ['G', ';DìFùpiì}+PuH"0\tJ'], ['H', '7^€\tJR7l<9;Wqz<mE'], ['I', '\n6CEzol+#urB p{;$'], ['J', "IWH]O>8?SMA&q'2?F"], ['K', '|(Y>k$kèw7$L1L |}'], ['L', ';SCér<!V\\21I=(t)}'], ['M', '21DnDiDdà ,EKçIò#'], ['N', 'J\nti2#. u8t/"|*!v'], ['O', ']gmUçw!97€%ktlu7ù'], ['P', '/lksù/Swf))NFc9eO'], ['Q', '-dT£  cFSG_*W\\[ù['], ['R', '4XKl6Gbv$\nk\n<4WçJ'], ['S', '\\|h(€,fT1Té°eALL8'], ['T', '-k&è=FG9c+q£9}_-o'], ['U', "\t\\&QBcjLYM),,%'\n6"], ['V', 'R($v§#b\\D TPH*G&{'], ['W', 'c]wXmTNIdu:Plv§òK'], ['X', '-FtdkF|§A>UW$m#e_'], ['Y', 'S:€}>Ué%q($3ro^\\2'], ['Z', 'òxcs°a\\§{5.O#Eq[M'], ['0', "h'v[§9JECBòSJML!>"], ['1', 'Wd4WOç@+)B OC\\@=ò'], ['2', '£1j{a€#!lM{ùXK&)X'], ['3', 'vF&b;q,c&^èCxì$§G'], ['4', 'ìzYu]ù§vDZ°F3-B1]'], ['5', "'0€9UJ=yd0!!hgPsp"], ['6', 'jò2A66r#v&jB|}t1,'], ['7', '€òOJKb,h-"§f\tv^7p'], ['8', 'fG/GIIQ%kDd\tFKgn-'], ['9', 'ZtQ/^LN;emhJ6ç[G)'], [',', 'NI\\\tç_aP*ZY0€|eH('], ['.', '5a:Z+RfT"h$fCnW\\,'], ['-', 'PìXHOudò,ReZ-NOG;'], [';', "sUgrJM'6xsièBf|qk"], [':', 'On{xGR4{;#Y97/sèp'], ['_', '!fF1tç1gùRmà\\k%U['], ['<', '1ìéH#Zbe§F.wJ]tèT'], ['>', '#3iUGA[hE]Ffz|Anr'], ['!', '5à;K=( ò!RF%&J5>è'], ['£', "?]$èç(vnBàv'sEhé°"], ['$', ';4\\6yrC)!L1Ng(uY"'], ['%', 'TmBGHOjyk{a8t00FP'], ['&', 'Ejoli\n8(W5vZj||.v'], ['/', ']*<mbìGU,+eà(OAKJ'], ['(', "xq*i{TZru'^=2.[Bè"], [')', 'XS=eP%D0rKzT, =G_'], ['=', '-6<792OCNoj§_&itI'], ['?', 'ù(; }TE!Jç§BZBM9B'], ['^', "K-€v°)}[a&o'Kw§Y:"], ['ì', 'M%pTma7MQ#w&iGDF+'], ["'", 'p5Qa?)8H>JzG(ùHQò'], ['"', 'gè]9Nkf&Y}al(z|)W'], ['\\', 'L ù)BX_-+t_)€a(20'], ['|', '5çùrYroòi}ct$Zf*u'], ['è', 'ù\tç§>K5MIuCVç^p(5'], ['+', 'Xf%QgG=E{zn8_(uF#'], ['ò', 'K1J]"9\t!*AxFvnN0J'], ['à', 'w87F GòfçYj=HèA?F'], ['ù', '] 4re"Coe/o<h^\\r*'], ['é', 'TJAK0m\\Zéù4ìm>f£>'], ['*', 'd-\nl°DùwhQdée]GòI'], ['ç', 'KwèOSzk?ak%hme"|j'], ['°', '°e:#rUU2Qà56SZoMK'], ['§', 'z/gp8bjxx@_[§0o{g'], ['[', '*8&C:^ZhBguèy6}Sv'], [']', '5#HU!TaVP£7l@ 4/#'], ['@', '.ìTqn""VOSAçd[tYd'], ['#', '\\4kQ{K8#Và2rW}-!A'], ['{', '§.£#t:°)LtìxcI8cV'], ['}', '4ò=2#]@k!Sw€b*S)%'], ['€', 'T;+è>Fl_£$^£ rWYò'], ['\t', 'gç^éQMP|4n6iYç*TW'], ['\n', 'Zz9j1@L>oUSrSç-3N'], [' ', 'è^3#[QEhrwè;ìì+wè']]

	print(table)
	# TRYING TO ENCODE A MSG #

	encoded_msg = encode(get_multi_line_input(),table)
	if encoded_msg not in error_codes_n:
		print(encoded_msg)
	else:
		PrintError(encoded_msg)

	# TRYING TO DECODE A MSG #
	if (encoded_msg not in error_codes_n):
		decoded_msg = decode(encoded_msg,table)
	else:
		decoded_msg = encoded_msg
	if (decoded_msg not in error_codes_n):
		print(decoded_msg)
	else:
		PrintError(decoded_msg)
		os.system("exit")

	key_unload = unload_key_from(table)
	table_load = load_table_from(key_unload)

	# if table_load==table:
		# print("table load and key unload : STATE = PERFECT")
	# else:
		# print("table load doesn't match table gended")
	file.write(encoded_msg)
	file.close()
	file_out.write(string(table))
	file.close()