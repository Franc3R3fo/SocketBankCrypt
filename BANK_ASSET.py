import STEAM, socket, pickle

global table

table = [['a', '.kèù_§è'], ['b', 'Ki)ù*Y§'], ['c', '7=FH/v.'], ['d', '$jQT0\n.'], ['e', 'iR;è\nK)'], ['f', 'jgx{H3é'], ['g', 'U+.)WDU'], ['h', 'z\n3BNàj'], ['i', '§s65lvA'], ['j', 'XshPH§§'], ['k', '!3wM">b'], ['l', '2eir,Z='], ['m', '_.M_sçk'], ['n', 'H8 2o:é'], ['o', 'jNej£+='], ['p', '=_"ì4òj'], ['q', ',ì@*Y2A'], ['r', 'tR@àA$;'], ['s', 'fèQ\nXXg'], ['t', 'NwJwo96'], ['u', 'é4AZ[5L'], ['v', 'ç[-zk0I'], ['w', 'ahjs\nEd'], ['x', '&çk= FX'], ['y', 'ù0WDb€J'], ['z', 'rpàKqìD'], ['A', 'zd<.J(|'], ['B', 'Y@§CW=+'], ['C', '<%2(wDù'], ['D', 'dA§gHW,'], ['E', "JYY8'qU"], ['F', 'Ga#qW@U'], ['G', '!2X&*VD'], ['H', 'E!a%|PE'], ['I', '0èfYw\t6'], ['J', '&Ndrz-:'], ['K', 'I[p<SUi'], ['L', 'FX#bUZh'], ['M', "ò<R\\':P"], ['N', '}§LwaGP'], ['O', 'q.[{çxù'], ['P', '9YYZ_+m'], ['Q', '56\tQw€}'], ['R', 'YVL=Mqk'], ['S', 't*$RL"*'], ['T', '\t&M!PgI'], ['U', 'r#Y2]£S'], ['V', 'm,PIyam'], ['W', '.fv.AQ '], ['X', '{U6iq+à'], ['Y', 'idi?\\n/'], ['Z', '4+}$cst'], ['0', '.FGF=@i'], ['1', 'B?£j#o{'], ['2', 'ff}DmLq'], ['3', '"c/W*q8'], ['4', '78$§F6 '], ['5', 'TòrZMG]'], ['6', '.\nç027\\'], ['7', 'tQbpHw:'], ['8', 'JQ{he_q'], ['9', 'd$LQIh#'], [',', "à^- 'I2"], ['.', '"/U=Wsò'], ['-', 'è!8] S&'], [';', '£?mOé,{'], [':', 'N*8]#xç'], ['_', 'f7|£Q\n?'], ['<', 'HK1JRET'], ['>', 'Q@bXP u'], ['!', ' <i&_-$'], ['£', 'vtx"I2Z'], ['$', '_kKg€.j'], ['%', 'Q00yeuH'], ['&', ' I}dYmt'], ['/', 'Ccbé21l'], ['(', 'KìUOPMW'], [')', '(v@r(0w'], ['=', 'ùzY@RL7'], ['?', 'PEgSq&J'], ['^', 'xTs\n6V('], ['ì', 'Wh7)#My'], ["'", 'èsw__;v'], ['"', 'éwpvf7W'], ['\\', '€(*i2$^'], ['|', 'o^F;P]j'], ['è', 'PFCQ[5\n'], ['+', '^Q/è.ye'], ['ò', 'H}l4LS{'], ['à', 'R&4i£a£'], ['ù', '%BqEzCç'], ['é', ';,;;p[D'], ['*', "5'n<E-)"], ['ç', 'V[vQùm4'], ['°', '7jiU?XA'], ['§', 'è|a=O95'], ['[', 'DmAZeér'], [']', '=;£%0Y:'], ['@', '%£H)*^H'], ['#', 'Sçz$9uv'], ['{', '|!gòp0G'], ['}', 'uB{9<"x'], ['€', '"Tgk5ì '], ['\t', 'èC(8ç9r'], ['\n', 'XgAW|FB'], [' ', 'XG/JTKu']]

def get_line(s):
	a = []
	b = ""
	for obj in s:
		if obj in "\n":
			if len(b)>0:
				a.append(b)
				b = ""
		elif obj in "\t":
			0
		else:
			b+=obj
	if len(b)>0:
		a.append(b)
	return a

def token(s):
	a = []
	b = ""
	for obj in s:
		if obj in " ":
			if len(b)>0:
				a.append(b)
				b = ""
		else:
			b+=obj
	if len(b)>0:
		a.append(b)
	return a

class close_msg:
	def __init__(self):
		self.type = "CLOSE"

class CryptedORDER:
	def __init__(self,V,OP,AC):
		self.V = V
		self.OP = OP
		self.AC = AC
		self.s = ""
		self.type = "OPERATION"
	
	def COMPLETE(self,user):
		self.AC = user
	
	def ASSEMBLE_ORDER(self):
		self.s = """
		VALUE = """ + str(self.V) + """
		OPERATION = """ + self.OP + """
		ACCOUNT = """ + self.AC + """
		"""
		del self.V
		del self.AC
		del self.OP
		
	def PARSE(self):
		for line in get_line(self.s):
			t = token(line)
			if len(t)!=0:
				if t[0] == "VALUE":
					self.V = int(t[2])
				elif t[0] == "OPERATION":
					self.OP = t[2]
				elif t[0] == "ACCOUNT":
					try:
						self.AC = t[2]
					except:
						0
	
	def CRYPT(self):
		self.ASSEMBLE_ORDER()
		self.s = STEAM.encode(self.s,table)
	
	def DECRYPT(self):
		self.s = STEAM.decode(self.s,table)
		self.PARSE()

class CryptedTRANSFER:
	def __init__(self,V,ACP,ACS):
		self.V = V
		self.OP = "->"
		self.ACP = ACP
		self.ACS = ACS
		self.s = ""
		self.type = "OPERATION"
	
	def COMPLETE(self,user):
		self.ACP = user
	
	def ASSEMBLE_ORDER(self):
		self.s = """
		VALUE = """ + str(self.V) + """
		OPERATION = """ + self.OP + """
		ACCOUNTP = """ + self.ACP + """
		ACCOUNTS = """ + self.ACS + """
		"""
		del self.V
		del self.ACP
		del self.ACS
		del self.OP
		
	def PARSE(self):
		for line in get_line(self.s):
			t = token(line)
			if len(t)!=0:
				if t[0] == "VALUE":
					self.V = int(t[2])
				elif t[0] == "OPERATION":
					self.OP = t[2]
				elif t[0] == "ACCOUNTP":
					try:
						self.ACP = t[2]
					except:
						0
				elif t[0] == "ACCOUNTS":
					try:
						self.ACS = t[2]
					except:
						0
	
	def CRYPT(self):
		self.ASSEMBLE_ORDER()
		self.s = STEAM.encode(self.s,table)
	
	def DECRYPT(self):
		self.s = STEAM.decode(self.s,table)
		self.PARSE()

# SERVER SPECIFIC FUNCTIONS #

class DataBase:
	def __init__(self):
		self.DB = []
	
	def login(self,conn):
		user = conn.recv(1024)
		user = STEAM.decode(pickle.loads(user),table)
		i = self.trace(user)
		if self.DB[i][0]!=user:
			conn.sendall(pickle.dumps("Cannot find your account."))
			return "error"
		else:
			conn.sendall(pickle.dumps("Account Found. Insert password : "))
			pswd = conn.recv(1024)
			pswd = STEAM.decode(pickle.loads(pswd),table)
			if pswd != self.DB[i][2]:
				conn.sendall(pickle.dumps("password isn't correct. \n Closing comunication."))
				return "error"
			else:
				conn.sendall(pickle.dumps("LOGGED IN."))
				return user
	def register(self,conn):
		user = self.DB[0][0]
		i = self.trace(user)
		while((self.DB[i][0]==user) or (user=="")):
			user = conn.recv(1024)
			user = STEAM.decode(pickle.loads(user),table)
			i = self.trace(user)
			if self.DB[i][0]==user:
				conn.sendall(pickle.dumps("This username already exists."))
		conn.sendall(pickle.dumps("RegPAS"))
		pswd = " "
		while(" " in pswd):
			pswd = conn.recv(1024)
			pswd = STEAM.decode(pickle.loads(pswd),table)
			i = self.trace(pswd)
			if self.DB[i][0]==pswd:
				conn.sendall(pickle.dumps("Password cannot contain spaces."))
		conn.sendall(pickle.dumps("PASS"))
		self.InsertAccount(user,0,pswd)
		return user
	
	def remove(self,conn):
		user = conn.recv(1024)
		user = STEAM.decode(pickle.loads(user),table)
		i = self.trace(user)
		if self.DB[i][0]!=user:
			conn.sendall(pickle.dumps("Cannot find your account."))
			return "error"
		else:
			conn.sendall(pickle.dumps("Account Found. Insert password : "))
			pswd = conn.recv(1024)
			pswd = STEAM.decode(pickle.loads(pswd),table)
			if pswd != self.DB[i][2]:
				conn.sendall(pickle.dumps("password isn't correct. \n Closing comunication."))
				return "error"
			else:
				conn.sendall(pickle.dumps("REMOVED."))
				self.RemoveAccount(user)
				return ""
	
	def RESET(self):
		self.DB = []
	
	def sortDB(self):
		self.DB = sorted(self.DB,key=lambda k: k[0])
	
	def InsertAccount(self,AC,V,pswd):
		self.DB.append([AC,V,pswd])
	
	def trace(self,AC):
		new = sorted(self.DB,key=lambda k: k[0]!=AC)
		return self.DB.index(new[0])
	
	def RemoveAccount(self,AC):
		self.DB.remove(self.DB[self.trace(AC)])
	
	def ListDB(self):
		self.sortDB()
		print("ACCOUNT - VALUE")
		for obj in self.DB:
			print(obj[0]," - ",obj[1]," - ",obj[2])
	
	def load(self,address=""):
		print("loading database")
		if address=="":
			address = self.add
		else:
			self.add = address
		self.RESET()
		in_file = open(address,"r")
		text = ""
		for line in in_file:
			text+=line
		text = STEAM.decode(text,table)
		if text not in STEAM.error_codes_n:
			for line in get_line(text):
				t = token(line)
				self.InsertAccount(t[0],int(t[1]),t[2])
		in_file.close()
		print("UPDATED LIST OF DB ENTRIES\n===========================")
		self.ListDB()
		print("\n===========================")
	
	def save(self,address=""):
		print("saving database")
		if address=="":
			address = self.add
		out_file = open(address,"w")
		current = self.DB[0]
		text = current[0]+" "+str(current[1])+" "+current[2]
		for i in range(1,len(self.DB)):
			current = self.DB[i]
			text+="\n"+current[0]+" "+str(current[1])+" "+current[2]
		text = STEAM.encode(text,table)
		out_file.write(text)
		out_file.close()

def send_Server_Response(res,s):
	s.sendall(pickle.dumps(res))

def process_first_packet(order,DB,mono_opr,double_opr):
	current_ip = order[0][1]
	current,block = order[0][0],order[1:len(order)]
	flag_AC_ERROR,flag_INS_MON_ERROR = False,False
	# processing 
	try:
		if DB.DB[DB.trace(current.AC)][0]!=current.AC:
			send_Server_Response("Cannot find your account.",current_ip)
			flag_AC_ERROR = True
	except:
		0
	try:
		if (DB.DB[DB.trace(current.ACP)][0]!=current.ACP):
			send_Server_Response("Cannot find your account.",current_ip)
			flag_AC_ERROR = True
		elif (DB.DB[DB.trace(current.ACS)][0]!=current.ACS):
			send_Server_Response("Cannot find "+current.ACS+" account.",current_ip)
			flag_AC_ERROR = True			
	except:
		0
	if flag_AC_ERROR:
		0
	elif current.OP in mono_opr:
		i = DB.trace(current.AC)
		if current.OP=="-":
			if DB.DB[i][1]>=current.V:
				DB.DB[i][1]-=current.V
			else:
				send_Server_Response("Cannot pay "+str(current.V)+" €. Insufficient Credit on your bank profile.",current_ip)
				flag_INS_MON_ERROR = True
		elif current.OP=="+":
			DB.DB[i][1]+=current.V
	
	elif current.OP in double_opr:
		i_p = DB.trace(current.ACP)
		i_s = DB.trace(current.ACS)
		if DB.DB[i_p][1]>=current.V:
				DB.DB[i_p][1]-=current.V
				DB.DB[i_s][1]+=current.V
		else:
			send_Server_Response("Cannot pay "+str(current.V)+" €. Insufficient Credit on your bank profile.",current_ip)
			flag_INS_MON_ERROR = True
	
	# sending response and exiting
	if flag_AC_ERROR or flag_INS_MON_ERROR:
		0
	else:
		send_Server_Response("SUCCESS",current_ip)
	return block,DB

#-------------------------------------------------------------------------------------------------------------------