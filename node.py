import json
import socket
from _thread import *

def node(client):
    global dataClients

    #try:
    dataClients = json.loads(getFile("data/dataclients.json"))
    print(dataClients)
    #except:
    #    print('FALLOOOO!!!!')
    #    dataClients = dict()

    while True:

        try:
            dataServer = client.recv(1024).decode()
        except error:
            print('Error de lectura.')
            break

        operations(dataServer)

def operations(dataServer):
    dataServerArray = dataServer.split('||')

    if dataServerArray[0] == '1':
        print(' [x] Se recibió el archivo: ', dataServerArray[2])
        file = open('node_files/' + dataServerArray[2], "w")# w -> write
        file.write(dataServerArray[3])
        file.close()
        save(dataServerArray[1], dataServerArray[2], dataServerArray[3])

def getFile(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    return data

def saveFile(filename, data):
    file = open(filename, "w")
    json.dump(data, file)
    file.close()

def save(key, filename, value):
    tuple = (filename, value)
    if key in dataClients.keys():
        dataClients[key].append(tuple)
    else:
        dataClients[key] = []
        dataClients[key].append(tuple)
    msg = ' [x] El archivo se guardó correctamente!'
    conn.send(msg.encode())
    saveFile("data/dataclients.json", dataClients)

if __name__ == '__main__':
    try:
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '0.0.0.0'
        #port = int(parameters())
        mySocket.bind( (host, 8000) )
        #mySocket.bind( ('172.31.15.122', 3000) )
        #mySocket.bind( (host, port) ) 
        mySocket.listen(5) 

        print('------ Runnning Node Application ------')
        
        while True:
            conn, addr = mySocket.accept()
            print(" [x] Conexión desde: " + str(addr))
            start_new_thread(node, (conn, ))

    except Exception as error:
        print(socket.error)
