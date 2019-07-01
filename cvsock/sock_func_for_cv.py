import cv2
import socket as sc
import numpy as np
import time

def sendimg(sock,img):
    totalsend = 0
    nn = 0
    sendsize = img.size
    img = img.tostring()
    while totalsend < sendsize:
        n = sock.send(img[totalsend:])
        totalsend += n
        nn += 1
        print(totalsend,nn)
        time.sleep(0.5)
    return 



def recvimg(sock,size):
    total = 0
    img = bytes()
    while total < size:
        data = sock.recv(size-total)
        img += data
        total = total + len(data)
        print(total,"/",size)
    img = np.fromstring(img,dtype=np.uint8)
    img = np.reshape(img,(340,509,3))
    return img

def socket_set_up(ip,port):
    sock = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    sock.bind((ip,port))
    sock.listen(5)
    print("接続待ち")
    conn,addr = sock.accept()
    print("接続完了")
    return conn

def connect(ip,port):
    sock = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    sock.connect((ip,port))
    print("接続完了")
    return sock



def getimg():
    while True:
        imgname = input("送信したい画像名を入力してください:")
        img = cv2.imread(imgname,1)
        if img is None:
            print("画像がありません")
        else:
            print(imgname+"を出力します")
            break
    return img

def getwebcamimg():
    cam = cv2.VideoCapture(0)
    if not cam:
        print("can not open webcam!!")
    flag,img = cam.read()
    return img

