### Backend Test: Desafío Envíame

El siguiente README entrega las instrucciones para ejecutar cada uno de los ejercicios, de acuerdo a lo solicitado.


### Ejercicio 1: Docker

Dentro del directorio `ejercicio-1` se encuentran un archivo Dockerfile y un docker-compose.yml. Para levantar el entorno, basta con ejecutar un `docker-compose up --build`

### Ejercicio 2: API REST + CRUD

Una vez levantado y ejecutado el entorno docker del ejercicio 1, se habrá iniciado un servicio web en el puerto 80. Una query a `http://localhost/hello` les dará un saludo.
Para revisar cada endpoint y sus métodos de uso, pueden visitar `http://localhost/docs`

Las credenciales para acceso al API se entregaron vía correo.
### Ejercicio 3: Análisis + Desarrollo 

Dentro del directorio `ejercicio-3` se encuentra un script en Python 3 que recibe input desde stdin. Si la línea es "exit", el script termina ejecución. De lo contrario, el script lee la línea proveniente de stdin e imprime en pantalla todos los substrings palíndromos de largo máximo encontrados en el string, y su largo. Este script además puede recibir archivos de texto desde consola vía redirección de input.

El string indicado como input para el problema se encuentra en `ejercicio-3/input.txt`. Para obtener el resultado, basta ejecutar en consola `python3 ejercicio-3/main.py < ejercicio-3/input.txt` desde el directorio raíz del repositorio.

Adicionalmente, entrego el archivo `test.txt` con strings de prueba que utilicé para testear y debuggear el script.

### Ejercicio 4: Consumo API Envíame para la creación de un envío
Dentro del directorio `ejercicio-4` se encuentra un script en Python 3 que ejecuta una llamada al endpoint entregado en la documentación y almacena la respuesta en el archivo `response.json`. Para llamarlo, solo se necesita ejecutar `python3 ejercicio-4/main.py` en el directorio raíz del repositorio. El resultado se encontrará en la raíz también.

Este script utiliza la librería **requests** de Python. En caso de no tenerla instalada, se puede instalar con un simple `pip3 install requests`

### Ejercicio 5

Dentro del directorio `ejercicio-5` se encuentra un script en Python 3 que imprime a consola números de la sucesión de Fibonacci y la cantidad de divisores que tienen, hasta que encuentre el primer número en la sucesión con más de 1000 divisores. El script no tiene dependencias fuera de la librería estándar de Python, así que se puede ejecutar directamente con `python ejercicio-5/main.py` desde el directorio raíz del repositorio.


### Ejercicio 6: Análisis + Desarrollo Aplicado a Negocio
El directorio `ejercicio-6` contiene un script en Python 3 que genera distancias aleatorias en el rango indicado, y devuelve los tiempos estimados de entrega en formato de texto. 
Puede ejecutarse usando `python3 ejercicio-6/main.py`. El script no tiene dependencias externas.

### Ejercicio 7: SQL
En el directorio `ejercicio-7` se encuentra un script .sql que ejecuta el seeding base y luego corre la actualización solicitada. El script utiliza notación estándar de SQL y por lo tanto debiera correr en cualquier motor de base de datos SQL. Sin embargo, se recomienda utilizar MySQL versión 5.6.
