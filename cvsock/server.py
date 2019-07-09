import cv2
import socket 
import sock_func_for_cv as scv
import time
def main():
    #frame = scv.getimg()
    print("webカメラのセットアップ中")
    cap = cv2.VideoCapture(0)
    if cap is None:
        ("セットアップ失敗")
    print("セットアップ完了")
    with scv.socket_set_up("172.16.10.104",55002) as sock:
        #cv2.namedWindow("server", cv2.WINDOW_NORMAL)
        while True:
            flag,frame = cap.read()
            print("image data:",frame.shape)
            cv2.imshow("server",frame)
            scv.sendimg(sock,frame)
            k = cv2.waitKey(1) # 1msec待つ
            if k == 27: # ESCキーで終了
                break
            
    cv2.destroyAllWindows()           


if __name__ == "__main__":
    main()