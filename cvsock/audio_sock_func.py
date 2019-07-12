import socket as sc
import numpy as np

def sendaudio(sock,input):
    total = 0
    funcnum = 0
    size = len(input)
    while total < size:
        n = sock.send(input[total:])
        total += n
        funcnum += 1
        print("音声送信:",funcnum)
    return 

def recvaudio(sock):
    total = 0
    funcnum = 0
    size = 2048
    audio = bytes()
    while total < size:
        buff = sock.recv(size - total)
        audio += buff
        total += len(buff)
        funcnum += 1
        print("音声受信:",total,"/",size,funcnum)
    return audio

    