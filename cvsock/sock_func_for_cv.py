import cv2
import socket as sc
import numpy as np
import time
import sys
import cvfunc as cvf



def sendimg(sock,img):
    """画像を送信する関数"""
    img = cvf.imgencode(img,50)#画像圧縮
    data= [img.size]#numpyで扱いやすくするためにいったんリストに格納している
    senddata = np.array(data + list(img.shape))#numpyで画像データを格納したリストを生成する
    print("送信画像データ:",senddata)#画像データの表示
    senddata = senddata.tostring()#画像データの入ったリストをバイナリに変換
    img = img.tostring()#画像をバイナリに変換
    sendf(sock,senddata)
    sendf(sock,img)
    return 


def sendf(sock,string,):
    total = 0
    funcnum = 0
    size = len(string)
    while total < size:
        n = sock.send(string[total:])
        total += n
        funcnum += 1
        print("send size:",total,"funcnum",funcnum)#詳細の表示
    return 

def recvimg(sock):
    """画像を受け取る関数"""
    recvdata = recvf(sock,12)
    recvdata = np.fromstring(recvdata,dtype=np.int32)#バイナリで受け取ったデータを変換
    print("受信画像詳細データ:",recvdata)
    size = recvdata[0]#画像データのサイズを格納
    shape = tuple(num for num in recvdata[1:])#画像データの形を格納
    img = recvf(sock,size)
    img = np.fromstring(img,dtype=np.uint8)#画像バイナリデータの変換
    img = np.reshape(img,shape)#画像の型に合わせて数値変換
    img = cv2.imdecode(img,1)#画像のデコード
    return img


def recvf(sock,size):
    total = 0
    funcnum = 0
    #size = 4096
    string = bytes()
    while total < size:
        buff = sock.recv(size - total)
        string += buff
        total += len(buff)
        funcnum += 1
        print("受信:",total,"/",size,funcnum)
        if funcnum > 1000:
            print("受け取り失敗")
            return False
    return string



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