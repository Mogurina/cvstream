import cv2
import socket as sc
import numpy as np
import time
import sys



def imgencode(img,quality=5):
    """画像を圧縮する関数"""
    param = [int(cv2.IMWRITE_JPEG_QUALITY),quality]
    result,encimg = cv2.imencode(".jpg",img,param)
    return encimg

def sendimg(sock,img):
    """画像を送信する関数"""
    totalsend = 0#送信した画像データ量が格納される
    funcnum = 0#何回送信したか記録する
    img = imgencode(img,25)#画像圧縮
    data= [img.size]#numpyで扱いやすくするためにいったんリストに格納している
    senddata = np.array(data + list(img.shape))#numpyで画像データを格納したリストを生成する
    print("送信画像データ:",senddata)#画像データの表示
    senddata = senddata.tostring()#画像データの入ったリストをバイナリに変換
    img = img.tostring()#画像をバイナリに変換
    n = sock.send(senddata)#送信予定の画像情報を先に送信する
    while totalsend < data[0]:#画像データをすべて送信できるまでループする
        n = sock.send(img[totalsend:])#最後に送信されたデータの一から送信する
        totalsend += n#送信したデータ量分加算する
        funcnum += 1#送信した回数を数える
        print("size:",totalsend,"funcnum",funcnum)#詳細の表示
        #time.sleep(0.5)
    return 


def recvimg(sock):
    """画像を受け取る関数"""
    recvdata = sock.recv(49)#事前に送られてくる画像についてのデータを受け取る
    recvdata = np.fromstring(recvdata,dtype=np.int32)#バイナリで受け取ったデータを変換
    print("受信画像データ:",recvdata)
    if recvdata is None:
        print("受信失敗")
        return False
    size = recvdata[0]#画像データのサイズを格納
    shape = tuple(num for num in recvdata[1:])#画像データの形を格納
    total = 0#受け取ったデータ量を格納
    img = bytes()#画像のバイナリデータを格納する変数の確保
    while total < size:#すべて受け取るまでループ
        data = sock.recv(size-total)#すでに受け取ってあるデータ量分減算して受け取る
        img += data#受け取ったバイナリデータの加算
        total = total + len(data)#受け取ったデータ量分加算
        print(total,"/",size)
    img = np.fromstring(img,dtype=np.uint8)#画像バイナリデータの変換
    img = np.reshape(img,shape)#画像の型に合わせて数値変換
    img = cv2.imdecode(img,1)#画像のデコード
    return img

def socket_set_up(ip,port):#ipアドレスと使用したいポート番号を受け取る
    """サーバー用関数"""
    sock = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    sock.bind((ip,port))
    sock.listen(5)
    print("接続待ち")
    conn,addr = sock.accept()
    print("接続完了")
    return conn

def connect(ip,port):#ipアドレスとポート番号を受け取る
    """クライアント用関数"""
    sock = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    sock.connect((ip,port))
    print("接続完了")
    return sock

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


