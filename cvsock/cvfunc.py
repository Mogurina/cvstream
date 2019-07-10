import cv2


def getimg():
    """画像取得関数"""
    while True:
        imgname = input("送信したい画像名を入力してください:")
        img = cv2.imread(imgname,1)
        if img is None:
            print("画像がありません")
        else:
            print(imgname+"を出力します")
            break
    return img


def imgencode(img,quality=5):
    """画像を圧縮する関数"""
    param = [int(cv2.IMWRITE_JPEG_QUALITY),quality]
    result,encimg = cv2.imencode(".jpg",img,param)
    return encimg


def persondetection(img):
     # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # HoG特徴量 + SVMで人の識別器を作成
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}
    # 作成した識別器で人を検出
    human, r = hog.detectMultiScale(gray, **hogParams)

    # 人の領域を赤色の矩形で囲む
    for (x, y, w, h) in human:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)
        cv2.putText(img, 'person', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), thickness=2)
    return img

def imshow_fullscreen(winname, img):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(winname, img)
