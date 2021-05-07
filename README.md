# Filtro de Camara
### Filtro que invierte los colores a la webcam

Bryan
Gerardo
Karla
John Paul

# Breve explicación
Lo que hicimos en este proyecto fue crear un código de Python que nos pudiera mostrar un filtro en vivo de cámara. En este caso utilizamos el filtro de colores invertidos. Para hacerlo utilizamos como base el código que llama a la cámara 0 o dafault del dispositivo en donde se corre el código, y luego agregamos otras líneas de código que nos mostrara la imágen de la cámara pero con los colores invertidos. 

### Imports
cv2
time
argparse

## Instrucciones para correr
Para correrlo debemos clonar y pegar el link dentro de la terminal.

### Archivo
El archivo filtro.py es el de los colores invertidos

## Otros códigos
También intentamos utilizar el código de cámara inicial para poder hacer un filtro que incertara una imágen en cierto lugar indicado, por ejemplo un cubrebocas o unos lentes que cubrieran esa parte del cuerpo cuando detecta la cara. En esta código el problema que tuvimos fue el ajustar el tamaño de la imagen png a la hora de alejarse o acercarse a la cámara. Por otro lado en el código de los lentes nos salía un error a la hora de correrlo y nunca supimos porque ni como solucionarlo, por eso quedan incompletos. Sin embargo, aquí se encuentran los archivos también.

Lentes.py es el código fallido de lentes. El error nace ya que pyrhon no está detectando el programa de cascades que ya está instalado dentro de opencv.

## Referencias para Lentes.py
Udell, A. (2021, March 10). Creating a Snapchat-Style Filter with Python - Towards Data Science. Medium. https://towardsdatascience.com/creating-a-snapchat-style-filter-with-python-b42ecfd2ff54
