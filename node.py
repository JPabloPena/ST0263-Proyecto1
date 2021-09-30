#https://tutorialpython.com/listas-en-python/
from os import pardir
from socket import socket
import sys

def Client():

    #server, port = parameters()    

    mySocket = socket() #Se llama al método socket
    #mySocket.connect( (server, int(port)) ) #Se establece una conexión con el servidor mediante el método socket recibiendo un servidor y puerto
    mySocket.connect( ('localhost', 8000) )
    #mySocket.connect( ('35.153.31.234', 3000) )

    print('------ Runnning Node Application ------')
       
    msg = ""

    while True:

        print(' [x] Escriba el nombre del archivo que desea guardar: ')
        msg = "Hola"
        mySocket.send(msg.encode())
        serverData = mySocket.recv(1024).decode()

    mySocket.close() #Se termina la conexión con el servidor






def node(value):
    hash = {}
    node1 = []
    node2 = []
    node3 = []
    key = 0
    v = value
    
    hash[key] = value
    node1.append(hash)
    key = key + 1

    hash[key] = 'minecraft'
    node1.append(hash)

    for n in node1:
        print(n)

    #key = key + 1

node('file_test.txt')