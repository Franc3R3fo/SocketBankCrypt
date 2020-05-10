import socket, pickle, STEAM,os

def clear():
	os.system("")

from BANK_ASSET import *

global HOST,PORT,s,Command_Scheme,Syntax_Scheme,Help_Scheme
Command_Scheme = [ "pay","load","trasfer","EOF","help" ]
Syntax_Scheme = [ "pay <positive int value>","load <positive int value>","transfer <positive int value> <destination>","EOF","help [command]" ]
Help_Scheme = ["is used to remove money from your profile","is used to add money to your profile","is used to perform a wire transfer (in italiano \"bonifico bancario\")","is used to break the connection","is used to get informations about utility"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'  # localhost
PORT = 65432        # non-privileged ports are > 1023

def isint(x):
	try:
		y = int(str(x))
		return True
	except:
		return False

def ispos(x):
	if isint(x):
		if int(x)>=0:
			return True
		else:
			return False

def print_help_scheme(s = "all"):
	if s == "all":
		print("======== HELP SCHEME ========")
		for obj in Command_Scheme:
			print(obj,Help_Scheme[Command_Scheme.index(obj)])
		print("======= SYNTAX SCHEME =======")
		for obj in Syntax_Scheme:
			print(obj)
		print("Legend : \n[] -> Optional Parameter\n<> -> Required Parameter")
	else:
		if s in Command_Scheme:
			print("Legend : \n[] -> Optional Parameter\n<> -> Required Parameter")
			i = Command_Scheme.index(s)
			print(Command_Scheme[i],"-",Help_Scheme[i])
			print(Syntax_Scheme[i])
		else:
			print("Cannot find")

def request_transfer(v,acs):
	print("Requesting Transfert")
	print("TO : ",acs)
	print("OF : ",v)
	print("===========================\n---------------------------\n===========================")
	OBJ = CryptedTRANSFER(v,"",acs)
	OBJ.CRYPT()
	s.sendall(pickle.dumps(OBJ))
	data = s.recv(1024)
	print('SERVER RESPONSE : ', pickle.loads(data))

def request_pay(v): # This function is symbolic. it's an example of other types of operation.
	print("Requesting : -")
	print("OF : ",v)
	print("===========================\n---------------------------\n===========================")
	OBJ = CryptedORDER(v,"-","")
	OBJ.CRYPT()
	s.sendall(pickle.dumps(OBJ))
	data = s.recv(1024)
	print('SERVER RESPONSE : ', pickle.loads(data))

def request_load(v): # Also this function is symbolic. it's another example of other types of operation.
	print("Requesting : +")
	print("OF : ",v)
	print("===========================\n---------------------------\n===========================")
	OBJ = CryptedORDER(v,"+","")
	OBJ.CRYPT()
	s.sendall(pickle.dumps(OBJ))
	data = s.recv(1024)
	print('SERVER RESPONSE : ', pickle.loads(data))

if __name__=="__main__":
	s.connect((HOST,PORT))
	data = ""
	# MAIN #
	while(data != "Login" and data != "Register" and data!="LOGGED IN." and data!="PASS"):
		print(pickle.loads(s.recv(1024)))
		data = input("")
		s.sendall(pickle.dumps(data))
		if data=="Register":
			while(data!="RegPAS"):
				s.sendall(pickle.dumps(STEAM.encode(input("Insert Username : "),table)))
				data = pickle.loads(s.recv(1024))
				if data!="RegPAS":
					print(data)
			while(data!="PASS"):
				s.sendall(pickle.dumps(STEAM.encode(input("Insert Password : "),table)))
				data = pickle.loads(s.recv(1024))
				if data!="PASS":
					print(data)
			print("Account successfully Created")
		if data=="Remove":
			s.sendall(pickle.dumps(STEAM.encode(input("Insert UserName : "),table)))
			data = pickle.loads(s.recv(1024))
			if data!="Account Found. Insert password : ":
				print(data)
			else:
				print(data)
				s.sendall(pickle.dumps(STEAM.encode(input(" : "),table)))
				data = pickle.loads(s.recv(1024))
				print(data)
				if data!="REMOVED.":
					print(data)
				else:
					print(data)
		if data=="Login":
			s.sendall(pickle.dumps(STEAM.encode(input("Insert UserName : "),table)))
			data = pickle.loads(s.recv(1024))
			if data!="Account Found. Insert password : ":
				print(data)
				s.close()
			else:
				print(data)
				s.sendall(pickle.dumps(STEAM.encode(input(" : "),table)))
				data = pickle.loads(s.recv(1024))
				print(data)
	print("Command Line Breaks with \"EOF\" in a single input line")
	print("To recieve information about syntax insert \"help\", optionally followed by a command.\nInserting only \"help\" will show informations about all commands")
	line = ""
	while(line!="EOF"):
		line = input(">>>")
		clear()
		t = token(line)
		if len(t)>1:
			if t[0]=="pay":
				if ispos(t[1]):
					request_pay(int(t[1]))
				else:
					print("Syntax : pay <positive int value>")
			elif t[0]=="transfer":
				if ispos(t[1]):
					request_transfer(int(t[1]),t[2])
				else:
					print("Syntax : transfer <positive int value> <destination>")
			elif t[0]=="load":
				if ispos(t[1]):
					request_load(int(t[1]))
				else:
					print("Syntax : load <positive int value>")
			elif t[0]=="help":
				print_help_scheme(t[1])
		elif t[0]=="help":
			print_help_scheme()
		elif line=="EOF":
			break
		else:
			print("Syntax Error : not recognised\nPlease use \"help\" to see correct syntax")
	s.sendall(pickle.dumps(close_msg()))
	s.close()