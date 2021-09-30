from os import pardir
from socket import socket
import sys

#Método que posee toda la lógica de negocio
def Client():

    #server, port = parameters()    

    mySocket = socket() #Se llama al método socket
    #mySocket.connect( (server, int(port)) ) #Se establece una conexión con el servidor mediante el método socket recibiendo un servidor y puerto
    mySocket.connect( ('localhost', 8000) )
    #mySocket.connect( ('35.153.31.234', 3000) )

    print('------ Runnning Client Application ------')
    print(' [x] ¿Qué operación desea realizar? Escriba únicamente el número: ')
    print('      1. Guardar \n      2. Eliminar \n      3. Actualizar \n      4. Descargar \n      5. Salir de la aplicación ')
         
    while True:

        operation = input(" >")
        msg = ""
        serverData = ""

        if operation == '1':
            print(' [x] Escriba el nombre del archivo que desea guardar: ')
            filename = input(" >")
            newFilename = filename
            filename = 'client_files/' + filename 
            file = open(filename, "r") # r -> read
            data = file.read()
            file.close()
            msg = operation + ',' + newFilename + ',' + data
            mySocket.send(msg.encode())
            serverData = mySocket.recv(1024).decode()
            print(serverData)          
            break

        elif operation == '2':
            print(' [x] Escriba el nombre del archivo que desea eliminar: ')
            filename = input(" >")
            msg = operation + ',' + filename
            mySocket.send(msg.encode())
            serverData = mySocket.recv(1024).decode()
            print(serverData)

            print('\n [x] ¿Qué operación desea realizar? Escriba únicamente el número: ')

        elif operation == '3':
            print(' [x] Escriba el nombre del archivo que desea actualizar: ')
            filename = input(" >")
            newFilename = filename
            filename = 'client_files/' + filename 
            file = open(filename, "r") # r -> read
            data = file.read()
            msg = operation + ',' + newFilename + ',' + data
            mySocket.send(msg.encode())
            serverData = mySocket.recv(1024).decode()
            print(serverData)
            file.close()
            break
        
        elif operation == '4':
            print(' [x] Escriba el nombre del archivo que desea descargar: ')
            filename = input(" >")
            msg = operation + ',' + filename
            mySocket.send(msg.encode())

            serverData = mySocket.recv(1024).decode()
            dataArray = serverData.split(',')

            if dataArray[0] == '1':
                file = open('client_files/' + filename, "w")# w -> write
                file.write(dataArray[2])
                file.close()
                print(dataArray[1])                
            elif dataArray[0] == '0':
                print(dataArray[1])
            break

        elif operation == '5':
            msg = operation
            mySocket.send(msg.encode())
            serverData = mySocket.recv(1024).decode()
            print(serverData)
            break

        else:
            print(' [x] Operación no válida, intente de nuevo:')

        #mySocket.send("file_test.txt".encode())
        #mySocket.send(data.encode())
        #serverData = mySocket.recv(1024).decode()

    mySocket.close() #Se termina la conexión con el servidor


def parameters():

    if len(sys.argv) == 3:
        server = sys.argv[1]
        port = sys.argv[2]
        print(' [x] Server:', server,'\n [x] Port:', port)
        
    else:
        print(' [x] Recuerde ingresar: $python3 client.py ip-sever port')
        print(' [x] Ejemplo: $python3 client.py 34.226.36.159 5672\n')

    return server, port

def prueba():
    print('Este es un mensaje desde el cliente')

if __name__ == '__main__':
    Client()
    