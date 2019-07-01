import cv2
import socket 
import sock_func_for_cv as scv
import time
def main():
    with scv.socket_set_up("10.0.2.15",55028) as sock:
        cv2.namedWindow("server", cv2.WINDOW_NORMAL)
        img = scv.getimg()
        while(True):
            scv.sendimg(sock,img)
            cv2.imshow("server",img)
            k = cv2.waitKey()
            if k == 27:
                break
    cv2.destroyAllWindows()           


if __name__ == "__main__":
    main()

