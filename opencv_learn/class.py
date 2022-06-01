from operator import le
import cv2
import numpy as np
import random

def img_display():
    img = cv2.imread(r"img\ford_mustang.png")
    # img = cv2.resize(img,(200,300)) 
    img = cv2.resize(img,(0,0),fx=2,fy=2) #以倍數放大 放大兩倍
    cv2.imshow("demo",img)
    cv2.waitKey(0) #等待鍵盤上按任一鍵按下

def video_display():
    video = cv2.VideoCapture(r"img\74622.t.mp4")

    while True:
        ref , frame = video.read() # 會讀取影片的每一幀圖片 回傳 是否成功 及 照片
        if ref == True:
            frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
            cv2.imshow("video",frame)
        else:
            break

        if cv2.waitKey(1) == ord("q"): #如果按q的話影片會停止 ord() =>取得鍵盤的編號
            break
        cv2.waitKey(1) #如果想調快或慢改變裡面的數字

def cam_display():
    cam = cv2.VideoCapture(0)

    while True:
        ref , frame = cam.read() # 會讀取影片的每一幀圖片 回傳 是否成功 及 照片
        if ref == True:
            frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
            cv2.imshow("video",frame)
        else:
            break

        if cv2.waitKey(1) == ord("q"): #如果按q的話影片會停止 ord() =>取得鍵盤的編號
            break
        cv2.waitKey(1) #如果想調快或慢改變裡面的數字


def craete_img():
    img = np.empty((300,300,3),np.uint8) # empty() 創建空的陣列 

    for row in range(300):
        for col in range(300):
            img[row][col]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

    cv2.imshow("img", img)
    cv2.waitKey(0)

def cut_img():
    img = cv2.imread(r"img\ford_mustang.png")
    img = img[:100,:200]
    cv2.imshow("img",img)
    cv2.waitKey(0)

def usual():
    img = cv2.imread(r"../img/paper0008-316.jpg")
    img = cv2.resize(img , (0,0), fx=0.5, fy= 0.5)
    kernel = np.ones((3,3),np.uint8)

    gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img , (1,1), 2) # cv2.GaussianBlur(img,(核),標準差)
    canny = cv2.Canny(img, 200, 250) #cv2.Canny(img, min, max)
    dilate = cv2.dilate(canny, kernel , iterations=1) #cv2.dilate(canny, 核 , iterations=次數)
    erode = cv2.erode(dilate, kernel, iterations=1)

    # cv2.imshow("img",img)
    # cv2.imshow("gary",gary)
    # cv2.imshow("blur",blur)
    # cv2.imshow("canny",canny)
    # cv2.imshow("dilate",dilate)
    # cv2.imshow("erode",erode)
    # new = dilate[1]
    # arr = np.array(dilate)
    # arr = arr[100:237,220:505]
    # arr = arr[142:186,220:505]
    temp = []
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         if 0 in arr[i][j]:
    #             try:
    #                 if (i - temp[-1]) >8:
    #                     print(i,temp[-1])
    #             except:
    #                 pass
    #             temp.append(i)
            
    # cv2.imshow("erode",arr)
    print(dilate[0][0])
    print(img.shape)
    # cv2.waitKey(0)
        

usual()



