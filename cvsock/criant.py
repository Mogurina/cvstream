import cv2
import sock_func_for_cv as scv
import cvfunc as cvf

def main():
    sock = scv.connect("172.16.10.104",55002)
    with sock:
        #cv2.namedWindow("criant", cv2.WINDOW_NORMAL)
        while True:
            img = scv.recvimg(sock)
            if img is False:
                break
            print("image data:",img.shape)
            cvf.imshow_fullscreen("criant",img)
            #cv2.imshow("criant",img)

            k = cv2.waitKey(1) # 1msec待つ
            if k == 27: # ESCキーで終了
                break
    print("終了")
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

