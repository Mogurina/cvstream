import cv2
import socket 
import sock_func_for_cv as scv
import time
def main():
    frame = scv.getimg()
    #print("webカメラのセットアップ中")
    #cap = cv2.VideoCapture(0)
    #if cap is None:
    #    ("セットアップ失敗")
    #print("セットアップ完了")
    with scv.socket_set_up("192.168.0.31",55001) as sock:
        #cv2.namedWindow("server", cv2.WINDOW_NORMAL)
        while(cv2.waitKey() != "q"):
            #flag,frame = cap.read()
            print("image data:",frame.shape)
            scv.sendimg(sock,frame)
            cv2.imshow("server",frame)
            
    cv2.destroyAllWindows()           


if __name__ == "__main__":
    main()