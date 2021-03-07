#Liam Iverson
#lmi9555
#11192836


 
import socket, os


HOST = "localhost"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
 


inNode = True

print("-----------WELCOME TO GEOHASH CHAT ROOMS----------------")
print("Your are connected to node: " + HOST)
print("On port: " + str(PORT))




ROOMS = []
CHAT = []


inChat = False
currentRoom = ""
name = ""







name = input("What is your display name?: ")
#USED FOR CLEANING MESSAGES
def parseMessage(data):
	message = str(data)[2:len(str(data))-5]
	message = message.replace("[","").replace(",","").replace("]","")
	return message


#LOADS A SPECIFIC CHAT ROOM AND ITS CURRENT MESSAGES
def getChatRoom(room):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	sock.connect((HOST, PORT))
		
	sock.sendall("GETROOM\n".encode())

	data = sock.recv(1024)

	print(parseMessage(data))


	sock.sendall((room+"\n").encode())

	data = sock.recv(1024)

	message = str(data)[2:len(str(data))-5]
	CHAT = list(message.replace("[","").replace("]","").strip().split(",")) 
	for i in CHAT:
		print(i)
	sock.close()


def sendMessage(room,message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	sock.connect((HOST, PORT))
		
	sock.sendall("UPDATECHAT\n".encode())

	data = sock.recv(1024)

	print(parseMessage(data))


	sock.sendall((room+"\n").encode())

	data = sock.recv(1024)

	print(parseMessage(data))

	sock.sendall((message+"\n").encode())

	data = sock.recv(1024)

	print(parseMessage(data))

	sock.close()


def createRoom(roomname):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	sock.connect((HOST, PORT))
		
	sock.sendall("CREATEROOM\n".encode())

	data = sock.recv(1024)

	print(parseMessage(data))

	sock.sendall(str(roomname+"\n").encode())
	sock.close()



sock.sendall("ROOMS\n".encode())
data = sock.recv(1024)
ROOMS = list(parseMessage(data).split(" ")) 
sock.close()

while inNode:
	print("Available Rooms: " + str(ROOMS))
	command = input(":").strip()
	if(command.upper() == "QUIT"):
		inNode = False
	elif(command.upper() == "ENTER"):
		print("Which room?")
		for i in ROOMS:
			print(i)

		command = input(":")

		getChatRoom(command)
		currentRoom = command
		inChat = True
	
	elif(command.upper() == "CREATE ROOM"):
		roomName = input("Enter the name of the room:")
		createRoom(roomName)

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((HOST, PORT))
		sock.sendall("ROOMS\n".encode())
		data = sock.recv(1024)
		ROOMS = list(parseMessage(data).split(" ")) 
		sock.close()



	while(inChat):
		clear = lambda: os.system('cls') #on Windows System
		clear()

		getChatRoom(currentRoom)
		command = input("hit enter to refresh:")
		if(command.upper()  == "EXIT"):
			inChat = False
		if(command.upper() == "SEND"):
			message = input("Enter message: ")
			message = name+":"+message
			sendMessage(currentRoom,message)


		#print(data)





#sock.sendall("ROOMS\n".encode())
#data = sock.recv(1024)
#print(data)
 
#if ( data == "olleH\n" ):
    #sock.sendall("Bye\n")
    #data = sock.recv(1024)
    #print (data)
 
    #if (data == "eyB}\n"):
        #sock.close()
        #print("Socket closed")