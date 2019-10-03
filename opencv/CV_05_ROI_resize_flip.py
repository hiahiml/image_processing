"""
1. 동작 개요
    1) 영상의 특정 영역(ROI, Region Of Interest)을 변수로 설정하여 특정 지역 데이터만 편리하게 액세스한다.
    2) 영상의 크기를 변화시킨다.
    3) 영상을 상하좌우로 뒤집는다.
    4) 크기가 같은 두개 영상을 좌후, 상하로 이어 붙인다.


2. 주요 함수
    1) 영상의 크기를 변경하는 함수, resize()
    2) 영상 flipping: flip
        cv.flip(img2, 0)     # vertical flip
        cv.flip(img2, 1)     # horizontal flip
        cv.flip(img2, -1)    # vertical & horizontal flip
    3) 영상 이어붙이기: numpy.concatenate
    4) Accessing image data with numpy.array method
        - 잘 사용하지 않고 비추천. 속도 늦음.
        item(r,c,ch) :  특정 위치(row,column), channel을 지정
        itemset( (r,c,ch), value) :  특정 위치(row,column), channel에 value 값을 배정

3. 질문

"""

# ========================================================================================================
# 섹션 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
# ========================================================================================================
#Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = 'd:/StudyImages/Images/'        # 사용가능
Path = 'd:/Work/StudyImages/Images/'
Path = 'data/'

Name = 'colorbar_chart.jpg'
FullName = Path + Name
Name2 = 'lenna.tif'
FullName2 = Path + Name2

import cv2 as cv
import numpy as np


# ========================================================================================================
# 섹션 1 : 영상 파일을 읽어 들이기
# ========================================================================================================
img = cv.imread(FullName)
assert img is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.
img2 = cv.imread(FullName2)
assert img2 is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

#"""
# ========================================================================================================
# 실험 1: ROI: Region Of Interest 설정
# 영상의 특정 영역을 다른 변수로 지정하여 편리하게 접근(access)할 수 있다.
# ========================================================================================================
my_roi = img2[100:200, 100:200]
my_roi = 255-my_roi
cv.imshow('ROI: Region Of Interest', my_roi)
print ('Test 1 ---- \nmy_roi.shape=', my_roi.shape)
img[100:200, 300:400, :] = my_roi
cv.imshow('ROI: Region Of Interest', img)
cv.waitKey(0)
#"""

"""
# ========================================================================================================
# 실험 2: 영상의 크기를 변경하는 함수, resize()
# 예: cv.resize(영상, (가로*세로)) 영상을 (가로*세로) 크기로 조절하고 싶을 때.
# 주의 사항:
# resize()에 사용하는 사각형의 정보는 width x height이다. row x col을 사용하는 ndarray.shape와 반대이다.
# ========================================================================================================

# 1) 고정된 크기로 조정
width, height = 640, 480    # 크기를 지정하여 조정
resized_img = cv.resize(img2, (width, height))
cv.imshow('1) fixed size(640x440)', resized_img)

# 2) 지정하는 가로, 세로 비율로 조정. interpolation 알고리즘 조정
resized_img = cv.resize(img2, dsize=(0, 0), fx=1/2, fy=1/2, interpolation=cv.INTER_LINEAR)
cv.imshow('2) proportional', resized_img)

# 3) 자체의 속성 정보를 바탕으로 조정. 가로는 늘리고(x2) 세로는 줄여(//2) 본다.
width, height = int(img2.shape[1]*2), (img2.shape[0])//2    # //은 몫을 구하는 연산자. int()함수를 써도 같은 결과.
resized_img = cv.resize(img2, (width, height))
cv.imshow('3) width *=2, height /= 2)', resized_img)

# 4) 다른 영상(img)와 같은 크기로 조정(잘못된 방법).
# 그런데 이런 방식으로 하면 세로, 가로 정보가 뒤바뀐다. --- 주의!!! 가로 x 세로
resized_img = cv.resize(img2, img.shape[0:2])
cv.imshow('4) Incorrect img size', resized_img)

# 5) 다른 영상(img)와 같은 크기로 조정(올바른 방법).
# ndarray.shape를 사용하려면 row x col의 순서를 바꾸어 주어야 한다.
resized_img = cv.resize(img2, img.shape[1::-1]) # shape[2], shape[1]이 순서대로 만들어진다.=> 가로x세로
cv.imshow('5) Correct img size', resized_img)

cv.waitKey(0)
exit(0)
"""


# ========================================================================================================
# 실험 3, 4: 영상 flipping & image stacking
# ========================================================================================================
img_flip_along_x = cv.flip(img2, 0)     # vertical flip
img_flip_along_y = cv.flip(img2, 1)     # horizontal flip
img_flipped_xy = cv.flip(img2, -1)      # vertical & horizontal flip

cv.imshow('1) original image', img2)
cv.imshow('2) img_flip_along_x: vertical flip', img_flip_along_x)
cv.imshow('3) img_flip_along_y: horizontal flip', img_flip_along_y)
cv.imshow('4) img_flipped_xy', img_flipped_xy)
cv.waitKey(0)

# ========================================================================================================
# 실험 4: image stacking, 영상 이어붙이기
# To stack horizontally (img1 to the left of img2):
#   vis = np.concatenate((img1, img2), axis=1)
# To stack vertically (img1 over img2):
#   vis = np.concatenate((img1, img2), axis=0)
# ========================================================================================================


# 각각 2개씩 가로 방향으로 이어 붙인다.
upper = np.concatenate((img2, img_flip_along_y), axis=1)
lower = np.concatenate((img_flip_along_x, img_flipped_xy), axis=1)

# 위 2개의 영상을 세로로 이어 붙인다.
vis = np.concatenate((upper, lower), axis=0)

# 영상이 너무 커서 4개의 영상이 묶인 vis 영상을 가로, 세로 각각 1/2 축소하여 출력한다.
width, height = int(vis.shape[1]/2), int(vis.shape[0]/2)
vis2 = cv.resize(vis, (width, height))

cv.imshow('vis2', vis2)
cv.waitKey(0)



"""
# 기록용
# - 잘 사용하지 않고 비추천. 속도 늦음. 검토할 필요없음.
# 자습: 특정 위치 화소 값 읽기/쓰기 -------------------------------------------------
# item(위치): 특정 위치의 값을 읽어 반환한다.
# itemset(위치, 값): 특정 위치에 값을 설정한다
location = 150, 120, 0                  # row=150, col=120, channel=Blue
print ('Test4 ---- \nlocation=', location, '    value=', img2.item(location))             # 특정 위치와 채널의 값을 출력한다.
#print (img2.item(150, 120, 0))         # 같은 동작
img2.itemset( location, 254)            # 특정 위치의 특정 채널에 값을 배정한다.
print ('New value at the same location =', img2.item(location))             # 특정 위치와 채널의 값을 출력한다.
print (img2[5, 0:5, 0])                 # row=5, col=0~4, channel=Blue
cv.waitKey(0)

아래는 기록용
imgBayerBig = cv.resize(imgBayer, dsize=(0, 0), fx=4, fy=4, interpolation= cv.INTER_NEAREST)      # nearest neighbor interpolation
img = cv.resize(img, dsize=(0, 0), fx=1/4, fy=1/4, interpolation=cv.INTER_LINEAR)

"""