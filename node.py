import json
import socket
import os
from _thread import *

def node(client):
    global dataClients

    dataClients = json.loads(getFile("data/dataclients.json"))

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
        if os.path.exists(dataServerArray[2]):
            msg = ' [x] El archivo ' + dataServerArray[1] + ' ya existe. Pruebe de nuevo!'
        else:
            print(' [x] Se guardó el archivo: ', dataServerArray[2])
            file = open('node_files/' + dataServerArray[2], "w")# w -> write
            file.write(dataServerArray[3])
            file.close()
            save(dataServerArray[1], dataServerArray[2], dataServerArray[3])
            msg = ' [x] El archivo ' + dataServerArray[2] + ' se guardó correctamente!'
        conn.send(msg.encode())

    elif dataServerArray[0] == '2':
        print(' [x] Enviando los datos de la clave: ' + dataServerArray[1])
        get(dataServerArray[1])

    elif dataServerArray[0] == '3':
        print(' [x] Archivo a eliminar: ', dataServerArray[2])
        filename = 'node_files/' + dataServerArray[2]

        if os.path.exists(filename):                  
            os.remove(filename)
            print(' [x] Archivo ' + dataServerArray[2] + ' eliminado!')
            delete(dataServerArray[1], dataServerArray[2])
            msg = ' [x] El archivo ' + dataServerArray[2] + ' se eliminó correctamente!'
        else:
            msg = ' [x] El archivo ' + dataServerArray[2] + ' no existe!'       
        conn.send(msg.encode())

    elif dataServerArray[0] == '4':
        print(' [x] Archivo a actualizar: ', dataServerArray[2])
        filename = 'node_files/' + dataServerArray[2]
        
        if os.path.exists(filename):
            file = open('node_files/' + dataServerArray[2], "w")# w -> write
            file.write(dataServerArray[3])
            file.close()
            update(dataServerArray[1], dataServerArray[2], dataServerArray[3])
            msg = ' [x] El archivo se actualizó correctamente!'
        else:
            msg = ' [x] El archivo ' + dataServerArray[2] + ' no existe!'
        conn.send(msg.encode())

    elif dataServerArray[0] == '5':
        print(' [x] Archivo a descargar: ', dataServerArray[2])
        filename = 'node_files/'+ dataServerArray[2]

        if os.path.exists(filename):
            file = open(filename, "r") # r -> read
            data = file.read()
            file.close()
            msg = '1' + '||' +' [x] Se descargó el archivo: ' + dataServerArray[2] + '||' + data 
        else:
            msg = '0' + '||' + ' [x] El archivo ' + dataServerArray[2] + ' no existe!'
        conn.send(msg.encode())

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
    saveFile("data/dataclients.json", dataClients)

def get(key):
    msg = ""
    if key in dataClients.keys():
        msg = ' [x] ' + key + ': ' + ', '.join([str(elem) for elem in dataClients[key]])
        conn.send(msg.encode())
    else:
        msg = ' [x] Clave no encontrada!'
        conn.send(msg.encode())

def delete(key, filename):
    cont = 0
    if key in dataClients.keys():
        for n in dataClients[key]:
            if n[0] == filename:
                dataClients[key].pop(cont)
                break
            cont = cont + 1
        saveFile("data/dataclients.json", dataClients)
    else:
        msg = ' [x] La clave del archivo no fue encontrada!'
        conn.send(msg.encode())
    
def update(key, filename, value):
    cont = 0
    if key in dataClients.keys():
        for n in dataClients[key]:
            if n[0] == filename:
                delete(key, filename)
                save(key, filename, value)
                break
            cont = cont + 1
    else:
        msg = ' [x] La clave del archivo no fue encontrada!'
        conn.send(msg.encode()) 
    

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
