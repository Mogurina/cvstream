import cv2
import numpy as np

#HAAR分類器の顔検出用の特徴量
cascade_path = "C:\opencv\sources\data\haarcascades\haarcascade_frontalface_alt.xml"

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
        #cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)
        cv2.putText(img, 'person', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), thickness=2)
        img = mosaic_area(img,x,y,w,h,0.1)
    return img

def facedetection(image):
    #グレースケール変換
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #カスケード分類器の特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)

    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    #facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)


    if len(facerect) > 0:
        #検出した顔を囲む矩形の作成
        #for rect in facerect:
        #    cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), (255,0,0), thickness=2)

        for x, y, w, h in facerect:
            image = mosaic_area(image, x, y, w, h,0.05)

    return image



def pointdetection(img):
    # ORB (Oriented FAST and Rotated BRIEF)
    detector = cv2.ORB_create()

    # 特徴検出
    keypoints = detector.detect(img)

    # 画像への特徴点の書き込み
    out = cv2.drawKeypoints(img, keypoints, None)
    return out

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

def imshow_fullscreen(winname, img):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(winname, img)
