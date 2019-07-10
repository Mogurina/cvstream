import cv2
import sock_func_for_cv as scv
import cvfunc as cvf
cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号
while True:
    # retは画像を取得成功フラグ
    ret, frame = cap.read()
    # フレームを表示する   
    frame = cvf.persondetection(frame)
    cvf.imshow_fullscreen('camera capture', frame)
    print(frame.shape)
    k = cv2.waitKey(1) # 1msec待つ
    if k == 27: # ESCキーで終了
        break
# キャプチャを解放する
cap.release()
cv2.destroyAllWindows()