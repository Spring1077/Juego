# Filtro de Camara
## Filtro que invierte los colores a la webcam

## Bryan
## Gerardo
## Karla
## John Paul

## Lo que hicimos en este proyecto fue crear un código de Python que nos pudiera mostrar un filtro en vivo de cámara. En este caso utilizamos el filtro de colores invertidos. Para hacerlo utilizamos como base el código que llama a la cámara 0 o dafault del dispositivo en donde se corre el código, y luego agregamos otras líneas de código que nos mostrara la imágen de la cámara pero con los colores invertidos. 

## Código 

import cv2

import time

import argparse


if __name__ == '__main__':

    script_start_time = time.time()
    
    parser = argparse.ArgumentParser(description='Camera visualization')
   
    ### Positional arguments
    
    parser.add_argument('-i', '--cameraSource', default=1, help="Introduce number or camera path, default is 0 (default cam)")
    
    args = vars(parser.parse_args())
    
    cap = cv2.VideoCapture(args["cameraSource"])  # 0 local o primary camera
    
    ### Invert colors
    
    def apply_invert(img):
    
        return cv2.bitwise_not(img)
    
    while cap.isOpened():
    
        # BGR image feed from camera
        
        success, img = cap.read()
        
        invert = apply_invert(img)
        
        if not success:
        
            break
        
        if img is None:
        
            break
        
        cv2.imshow("Output", invert)
        
        k = cv2.waitKey(10)
        
        if k == 27:
        
            break
    
    cap.release()
    
    cv2.destroyAllWindows()
    
    print('Script took %f seconds.' % (time.time() - script_start_time))
