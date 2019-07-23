import cv2
import sock_func_for_cv as scv
import cvfunc as cvf
import numpy as np
import pyaudio


def main():

    CHUNK=2048
    RATE=44100

    #frame = scv.getimg()
    print("webカメラのセットアップ中")
    cap = cv2.VideoCapture(0)
    if cap is None:
        print("セットアップ失敗")
    print("セットアップ完了")

    p=pyaudio.PyAudio()

    stream=p.open(    format = pyaudio.paInt16,channels = 1,rate = RATE,frames_per_buffer = CHUNK,input = True,output = True) # inputとoutputを同時にTrueにする

    with scv.socket_set_up("172.16.10.104",55002) as sock:
        #cv2.namedWindow("server", cv2.WINDOW_NORMAL)
        while stream.is_active():
            flag,frame = cap.read()
            print("image data:",frame.shape)
            #frame = cvf.persondetection(frame)
            #frame = cvf.facedetection(frame)
            #frame = cvf.pointdetection(frame)
            #frame = cv2.bilateralFilter(frame,9,75,75)
            #cv2.imshow("server",frame)

            input = stream.read(CHUNK)

            scv.sendimg(sock,frame)
            scv.sendf(sock,input)
            k = cv2.waitKey(1) # 1msec待つ
            if k == 27: # ESCキーで終了
                break
            
    cv2.destroyAllWindows()   
    stream.stop_stream()
    stream.close()
    p.terminate()        

if __name__ == "__main__":
    main()