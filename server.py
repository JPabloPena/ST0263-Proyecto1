from os import pipe
import sys
from socket import socket, error
from threading import Thread

#Clase para conectarse con múltiples clientes al tiempo
class Client(Thread):

    #Método para indentificar cada cliente que se conecta al servidor
    def __init__(self, conn, addr):
        self.table = [None] * 127
        Thread.__init__(self) #Crea el hilo para el cliente

        self.conn = conn #Guarda la conexión
        self.addr = addr #Guarda la dirección de la conexión
    
    #Método que posee toda la lógica de negocio
    def run(self):
        
        while True:

            try:
                data = self.conn.recv(1024).decode()
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            
            dataArray = data.split(',')
            msg = ""
            

            if dataArray[0] == '1':
                print(' [x] Se recibió el archivo: ', dataArray[1])
                file = open('server_files/' + dataArray[1], "w")# w -> write
                file.write(dataArray[2])
                file.close()
                #H= Client()
               # H.Insert("hoa.txt")
                
                #key= add(self,dataArray[1],dataArray[1])
                key=getHash(dataArray[1])
               # print(key)
                #print(get(self,dataArray[1]))
                node(key, dataArray[1])
                #key = key + 1
                msg = ' [x] El archivo se guardo correctamente!'
                self.conn.send(msg.encode())

            elif dataArray[0] == '2':
                print(' [x] Se eliminó el archivo: ', dataArray[1])

            elif dataArray[0] == '3':
                print(' [x] Se descargó el archivo: ', dataArray[1])
            
            #file = open('server_files/' + filename, "w") # w -> write
            #file.write(data)
            #file.close()
            break
            #self.conn.send(datos.encode())
        print(' [x] Hasta luego...')
        self.conn.close() #Termina la conexión con el cliente

    
def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

def Insert(self, value): # Metodo para ingresar elementos
    hash = self.Hash_func(value)
    if self.table[hash] is None:
        self.table[hash] = value
   
def Search(self,value): # Metodo para buscar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
  
def Remove(self,value): # Metodo para eleminar elementos
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            print("No hay elementos con ese valor", value)
        else:
            print("Elemento con valor", value, "eliminado")
            self.table[hash] is None
        


def getHash(key):
    h = 0
    for char in key:
        h += ord(char)
    #print (h)
    return h % 100

def add(self,key,val):
    h=self.getHash(key)
    self.arr[h]=val

def get(self, key):
    h=self.getHash(key)
    return self.arr[h]



node1 = []
node2 = []
node3 = []
def node(key, value):
    hash = {}
    count = 0
    hash[key] = value
    node1.append(hash)
    print(node1[0])
    for n in node1:
        if(n!=NULL):
          count= count+1
          print(n)
    print(count)



def Main():
    
    mySocket = socket() #Se llama al método socket
    host = '0.0.0.0'
    #port = int(parameters())
    mySocket.bind( ('localhost', 8000) )
    #mySocket.bind( ('172.31.15.122', 3000) )
    #mySocket.bind( (host, port) ) #Escucha la conexión con el cliente
    mySocket.listen(5) #Define cuantos clientes se pueden conectar al servidor al mismo tiempo
    print('------ Runnning Server Application ------')

    while True:
        conn, addr = mySocket.accept()
        print(" [x] Conexión desde: " + str(addr))

        c = Client(conn, addr) #Crea el hilo con el cliente
        c.start() #Empieza la conexión con el cliente

def parameters():

    if len(sys.argv) == 2:
        port = sys.argv[1]
        print(' [x] Port:', port)
        
    else:
        port = '3000'
        print(' [x] Se estableción el puerto', port, 'por defecto. Si desea usar otro puerto cierre la aplicación y recuerde ingresar:')
        print(' [x] Recuerder ingresar: $python3 server.py port')
        print(' [x] Ejemplo: $python3 server.py', port)
        
    return port

if __name__ == '__main__':
    Main()