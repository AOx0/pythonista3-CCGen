 #Introduccion

Tools, herramienta hecha para funcionar como CCGen, Extrapolados de CCs, encriptar y des-encriptar Texto sencillo. Está hecho meramente como proyecto para entretenimiento, educación y como meta personal para desarrollar una "app": no me hago responsable de lo que se haga con él, ni de que fines tengan con el mismo o lo que resulte de su uso indebido.
*Es solo por entretenimiento y educación*

No me hago responsable de lo que se haga con él

La app está escrita en Español con Python3.6.1

#Instalación

El CCGen está hecho para que funcione con UI en [Pythonista3](Pythonista 3 de omz:software https://apps.apple.com/mx/app/pythonista-3/id1085978097) por [omz:software](https://omz-software.com).

* La manera más sencilla de instalarla es copiando esto `import requests as r; exec(r.get('http://bit.ly/2RztLbf').text)` en un nuevo archivo de extensión .py en Pythonista.

* Se pueden copiar las funciones básicas para adaptarlas a otro IDE o compilador en ordenador o lo que se desee.

• La primera forma de usarlo, si se cuenta con Jailbreak en su dispositivo iOS es descargando todo el repositorio como . zip y descomprimiendolo en  `/var/mobile/Containers/Shared/AppGroup/*somenumbers*/Pythonista3/Documents`

• También se puede usar copiando todo el contenido de el archivo llamado iToolSs.py y cópialo en un nuevo archivo de extensión .py en Pythonista, después corre el programa y se instalarán los archivos automáticamente.

Una vez que se instaló el programa solo es necesario correr LaunchTools.py, si instalaste el programa con Install.py o con `import requests as r; exec(r.get('http://bit.ly/2RztLbf').text)` LauchTools se encontrará en una carpeta llamada *Δ*

#Archivos

1. *LaunchTools.py*: El archivo principal que corre todo el programa
2. *configuracion1.py*: El archivo que contiene todas las funciones para correr el CCGen. Es básico.
3. *configuracion2.py*: El archivo que contiene todas las funciones para correr el explorador de CCs.
El extrapolado cuenta con 3 maneras distintas de extrapolar un Bin. Es necesario contar con 2 CCs distintas para que funcione. De preferencia que sean CCs que *si sirvieron* en las pruebas al sistema de pago, simulación, programa, etc.
5. *configuracion3.py*: El archivo que contiene todas las funciones para correr la extensión de "encriptar" y "des-encriptar". Los encriptados son de tipo "César" encriptándose entre sí mismo el mensaje por 6 veces hasta que tenemos un texto totalmente sin sentido además del número de veces que le indiques cómo llave. Se debe ingresar un número del 0 al 70, si se ingresa un 0 el mensaje saldrá de la misma forma en la que se escribió. Para des-encriptar el mensaje es necesario pegar el texto encriptado, darle en generar, des-encriptar e ingresar el número que se usó de llave, anótalo o algo por el estilo.
6. *configuracion4.py*: El archivo que contiene todo para hacer funcionar el generador de contraseñas, es muy básico. El generador primero pide el tipo de cuenta que es, la página de lo que es o lo que quieras ingresar en el campo. Después te pide en correo con el que realizarás o realizaste la cuenta. Luego te pregunta si deseas usar caracteres especiales como @=%. Al final te pregunta si quieres guardar en un archivo .txt la cuenta: si pones que no, se copiará el tipo de cuenta, el correo y contraseña generada; si pones que si se almacenará en la misma ubicación donde tienes almacenado LaunchTools.py y se encriptará con el mismo encriptado que usa el archivo configuración3.py con un *10 como llave de encriptado* de la herramienta. Se puede des-encriptar en la herramienta usándose esa llave. (10).
7. Los demás archivos son de tipo .pyui que almacenan la interfaz de todo el programa, cada archivo .pyui se llama igual al script con el que funciona.