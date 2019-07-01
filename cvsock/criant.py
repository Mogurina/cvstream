import cv2
import socket
import sock_func_for_cv as scv
import numpy as np
import time
def main():
    s = scv.connect("10.0.2.15",55028)
    with s:
        cv2.namedWindow("criant", cv2.WINDOW_NORMAL)
        while(1):
            img = scv.recvimg(s,519180)
            cv2.imshow("criant",img)
            k = cv2.waitKey()
            if k == 27:
                break
    print("終了")
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

