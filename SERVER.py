import socket, pickle, STEAM

from BANK_ASSET import *

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

orders = []
log = []
DB = DataBase()

try:
	DB.load(r"C:\Users\Francesco\Desktop\DATABASE.crypt")
except:
	DB.InsertAccount("001",0,"Alstom11")
	DB.InsertAccount("002",0,"RefoLara")
	DB.InsertAccount("003",0,"RefoAndrea")
	DB.InsertAccount("004",0,"Andromeda")
	
DB.ListDB()

mono_opr = "-+"
double_opr = ["->"]

#while True:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	FLAG_IM_IN = True
	Session_Timer = 0
	Session_Limit_Timer = 1024
	with conn:
		log.append(['Connected by', addr])
		data = ""
		while(FLAG_IM_IN):
			Session_Timer+=1
			DB.load()
			while(data != "Login" and data != "Register"):
				conn.sendall(pickle.dumps("Available Options : Login | Register | Delete"))
				data = pickle.loads(conn.recv(1024))
				if data=="Login":
					user = DB.login(conn)
				elif data=="Register":
					user = DB.register(conn)
					DB.save()
					DB.load()
				elif data=="Delete":
					user = DB.register(conn)
					DB.save()
					DB.load()
			if user != "error":
				print("Server Side Notification : Ready To Serv",addr,user)
				log.append(["Server Side Notification : Ready To Serv",addr,user])
				while True:
					data = conn.recv(1024)
					if data:
						data = pickle.loads(data)
						if data.type == "CLOSE":
							FLAG_IM_IN = False
							break
						elif data.type == "OPERATION":
							data.DECRYPT()
							data.COMPLETE(user)
							orders.append([data,conn])
							if len(orders)>0:
								orders,DB = process_first_packet(orders,DB,mono_opr,double_opr)
			else:
				print("Server Side Notification : ",addr,"Failed to Perform Login")
				log.append(["Server Side Notification : ",addr,"Failed to Perform Login"])
				data = ""
			if Session_Timer>=Session_Limit_Timer:
				FLAG_IM_IN=False
	conn.close()
# FINAL SAVE OF DB
DB.save(r"C:\Users\Francesco\Desktop\DATABASE.crypt")
# UPDATING LOG FILE
log_file = open(r"C:\Users\Francesco\Desktop\log.txt","a")
for obj in log:
	s = ""
	for x in obj:
		s+=str(x)+" "
	s=s[0:len(s)-1]
	log_file.write(s)
log_file.close()