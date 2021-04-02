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
-- Actualizar los sueldos de los empleados que ganen $5000 o menos, de acuerdo al reajuste anual del continente al que pertenecen.

CREATE TABLE `countries` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `continent_id` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `continents` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `anual_adjustment` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `employees` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `salary` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

insert into continents values (null, 'América', 4);
insert into continents values (null, 'Europa', 5);
insert into continents values (null, 'Asia', 6);
insert into continents values (null, 'Oceanía', 6);
insert into continents values (null, 'Africa', 5);

insert into countries values (null, 1, 'Chile');
insert into countries values (null, 1, 'Argentina');
insert into countries values (null, 1, 'Canadá');
insert into countries values (null, 1, 'Colombia');
insert into countries values (null, 2, 'Alemania');
insert into countries values (null, 2, 'Francia');
insert into countries values (null, 2, 'España');
insert into countries values (null, 2, 'Grecia');
insert into countries values (null, 3, 'India');
insert into countries values (null, 3, 'Japón');
insert into countries values (null, 3, 'Corea del Sur');
insert into countries values (null, 4, 'Australia');

insert into employees values (null, 1, 'Pedro', 'Rojas', 2000);
insert into employees values (null, 2, 'Luciano', 'Alessandri', 2100);
insert into employees values (null, 3, 'John', 'Carter', 3050);
insert into employees values (null, 4, 'Alejandra', 'Benavides', 2150);
insert into employees values (null, 5, 'Moritz', 'Baring', 6000);
insert into employees values (null, 6, 'Thierry', 'Henry', 5900);
insert into employees values (null, 7, 'Sergio', 'Ramos', 6200);
insert into employees values (null, 8, 'Nikoleta', 'Kyriakopulu', 7000);
insert into employees values (null, 9, 'Aamir', 'Khan', 2000);
insert into employees values (null, 10, 'Takumi', 'Fujiwara', 5000);
insert into employees values (null, 11, 'Heung-min', 'Son', 5100);
insert into employees values (null, 12, 'Peter', 'Johnson', 6100);

