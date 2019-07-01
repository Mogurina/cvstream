import cv2
import socket
import sock_func_for_cv as scv
import numpy as np
import time
def main():
    s = scv.connect("172.16.10.104",55000)
    with s:
        #cv2.namedWindow("criant", cv2.WINDOW_NORMAL)
        while(cv2.waitKey() != "q"):
            img = scv.recvimg(s,921600)
            cv2.imshow("criant",img)
    print("終了")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

