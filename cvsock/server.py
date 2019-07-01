import cv2
import socket 
import sock_func_for_cv as scv
import time
def main():
    cap = cv2.VideoCapture(0)
    with scv.socket_set_up("172.16.10.104",55000) as sock:
        #cv2.namedWindow("server", cv2.WINDOW_NORMAL)
        #img = scv.getimg()
        while(cv2.waitKey() != "q"):
            flag,frame = cap.read()
            scv.sendimg(sock,frame)
            cv2.imshow("server",frame)
            
    cv2.destroyAllWindows()           


if __name__ == "__main__":
    main()