# Título
Proyecto 1

# Autores
Juan Pablo Peña F.

Juan Sebastián Sanín V.

# Software
Aplicación para manejar archivos de texto (_.txt_).

# Descripción
Aplicación que permite a un usuario guardar, leer, eliminar, actualizar y descargar archivos _.txt_. Esto lo hace conectandose a un servidor el cual se encarga de hacer responsable a un nodo del manejo de los archivos y las operaciones anteriormente mencionadas. Además, los archivos son guardados en un _json_ para asegurar su persistencia.

# Detalles del diseño
La aplicación fue desarrollada en _Python_ haciendo uso de _Sockets_ para permitir la comunicación. El servidor y los nodos fueron montados en _AWS Educate_.

## Cliente
- La aplicación _client.py_ se encarga de hacer la conexión con el servidor a través de _Sockets_ y permite al usuario ejecutar la operación que desee como se indica en la aplicación misma.
- El cliente siempre envía mínimo la operación que desea ejecutar y una clave.
- En algunos casos la clave se crea automáticamente, pues nosotros para esta aplicación decidimos usar como clave la primera letra del archivo con el que se vayan a hacer operaciones. Por ejemplo, para un archivo llamado _test.py_ su clave sería la letra _'t'_.
- Todos los archivos van a estar destinados en la carpeta _client_files_, es decir, si un usuario desea guardar un archivo en un nodo, primero deberá subirlo a esta carpeta, o si por otro lado, desea descargar un archivo de un nodo, este archivo se descargará en esta carpeta.

## Servidor
- La aplicación _server.py_ se encarga de recibir por medio de _Sockets_ los datos enviados por el usuario y decidir que nodo va a ser el responsable de trabajar con la información.
- Para decidir que nodo usar, lo que hicimos fue tomar la clave que envió el usuario y pasarla a código _ASCII_. Luego de tener el número de la letra según ASCII, el servidor le asginó 8 letras al primer nodo (a..h), 9 letras para el segundo nodo (i..q) y 9 letras para el tercer nodo (r..z). Entonces, en el caso de tener la clave _'t'_, el servidor elegiría al tercer nodo para hacer la operación requerida por el usuario.
- Tras elegir el nodo, el servidor le envía al nodo a través de _Sockets_ la operación solicitada por el usuario. 

## Nodo
- La aplicación _node.py_ se encarga de recibir por medio de _Sockets_ la información enviada por el servidor para ejecutarla y enviarle respuesta, para que así mismo le devuelva la respuesta al usuario que solicitó la operación.
- Para el manejo de los archivos se hizo uso del módulo _os_ el cual permite crear, leer, eliminar y actualizar archivos.
- Entonces, según la operación enviada por el cliente el nodo se encarga de verificar si es posible de ejecutar y en caso de serlo ejecutarla.
- Los archivos se guardan en cada nodo en la carpeta _node_files_.
- Además, para tener persistencia de la información cada nodo cuenta con un archivo _dataclients.json_ que se encuentra dentro de la carpeta _data_, en el cual también se guarda toda la información. Para el manejo de archivos _.json_ se hizo uso del módulo _json_.

# Instalación
Es necesario tener _python3_.

Para instalar la aplicación:
Clonar el repositorio. Para hacerlo se debe instalar git en su máquina de esta manera:
```
$ sudo yum install git
```
Ya para clonarlo debe usar:
```
$ git clone https://github.com/JPabloPena/ST0263-Proyecto1.git
```

# Ejecución
Primero debe ejecutar el servidor, luego los nodos y por último el cliente.

## Servidor (_server.py_)
Para ejecutar el servidor debe acceder al archivo _server.py_ que se encuentra en la carpeta _server_ y modificar las direcciones IP que tiene para sus nodos. Lo puede hacer de la siguiente manera:
```
$ cd ST0263-Proyecto1/server/
$ nano server.py
```
Remplace _ip-node_ por la IP de su nodo (sin quitar las comillas) y remplace _port_ por el puerto de su nodo.
```
nodes = {
    'node1' : ('ip-node', port),
    'node2' : ('ip-node', port),
    'node3' : ('ip-node', port)
}
```
Para guardar presione Ctrl+s Ctrl+x.

Ya puede proceder a ejecutar el servidor de la siguiente manera:
```
$ python3 server.py <port>
```
Para mi caso fue:
```
$ python3 server.py 8000
```
Ya tiene su servidor corriendo!

## Nodo (_node.py_)
Para ejecutar un nodo, primero debe acceder a la carpeta _node_ y luego ejecutar el siguiente comando:
```
$ cd ST0263-Proyecto1/node/
$ python3 node.py <port>
```
Para mi caso fue:
```
$ python3 node.py 8000
```
Ya tiene su nodo corriendo!

## Cliente (_client.py_)
Para ejecutar el cliente, primero debe acceder a la carpeta _client_, luego si desea guardar archivos en los nodos debe acceder a la carpeta _client_files_ y guardar los archivos allí, para hacerlo ejecute los siguientes comandos:
```
$ cd ST0263-Proyecto1/node/
$ cd client_files/
```
La carpeta _client_files_ ya viene con unos archivos para que los pueda usar como prueba si desea. Para verlos ejecute dentro de la carpeta:
```
$ ls
color.txt  lamp.txt  soup.txt
```
Para salir de _client_files_ ejecute:
```
$ cd ..
```
Ya para iniciar el cliente debe ejecutar el siguiente comando estando en la carpeta _client_:
```
$ python3 client.py <ip-server> <port>
```
Para mi caso fue:
```
$ python3 publisher.py 54.152.39.112 8000
```
Ya tiene su cliente corriendo! Para ejecutar las operaciones, siga las instrucciones que da la aplicación.
