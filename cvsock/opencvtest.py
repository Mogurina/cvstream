import cv2
import sock_func_for_cv as scv
cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号
while True:
    # retは画像を取得成功フラグ
    ret, frame = cap.read()
    # フレームを表示する   
    print(frame.size)
    frame = scv.imgencode(frame,25)
    print(len(frame))
    frame = cv2.imdecode(frame,-1)
    cv2.imshow('camera capture', frame)
    print(frame.shape)
    k = cv2.waitKey(1) # 1msec待つ
    if k == 27: # ESCキーで終了
        break
# キャプチャを解放する
cap.release()
cv2.destroyAllWindows()