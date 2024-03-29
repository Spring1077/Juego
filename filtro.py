#Codigo creado por Bryan, Karla, Paul y Gerardo
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
