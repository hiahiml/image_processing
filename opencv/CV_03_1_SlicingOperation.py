"""
1. 개요
 1) Slicing 동작을 통해 영상의 일부 영역을 접근하여 처리하는 방법을 보인다.
 2) img = img2를 행하면 img2의 영상이 img에 복사되는 것은 아니다.
    단지 2개의 영상 객체의 포인터가 같은 위치를 가리키게 된다.
    따라서 둘 중 하나의 영상을 바꾸면 다른 것도 바뀔 수도 있다.(그렇다고 반드시 그런 것도 아님.)
    복사하는 방법의 사례: image2 = image.astype('uint8') 혹은 image2 = image.copy() 등..

2. 주요 함수
    ndarray.astype('uint8'): ndarray를 uint8형으로 만들어 반환한다.
    ndarray.astype(dtype=np.uint8): ndarray를 uint8형으로 만들어 반환한다.

3. 주의 사항
    python 3에서는 정수에 나누기를 행하면 부동소수 데이터가 만들어진다. 스칼라 값을 정수로 바꾸려면;
    1) int() 함수를 통해 변환한다. 예: int(3.95) => 3
    2) 몫을 구하는 // 연산자를 통해 정수 데이터를 얻을 수도 있다. 예: 487 //2 => 246

3. 미션
    소스 하단의 미션 과제와 도전 과제(2개)를 수행하시오.

"""

import cv2 as cv
import numpy as np              # 아직은 사용 안함.

"""
# ========================================================================================================
# 사전 연습
# 슬라이싱의 기초: (연습) 리스트, 스트링 자료형에 대한 slicing 액세스 기법을 익힌다.
# ========================================================================================================
string = "1234567890ABCDEFG"         # slicing 표현법 start:stop[:step]
print (string[1:5])                 # 1에서 4까지 1씩 증가시키면서
# 2345

print (string[2:])                  # 3에서 끝까지 1씩 증가시키면서
# 34567890ABCDEFG

print (string[1:5:2])               # 1에서 4까지 2씩 증가시키면서
# 24

print (string[0::2])                # 0에서 끝까지 2씩 증가시키면서
# 13579ACEG

print(string[-1])
# G

print(string[-1:])
# G

print(string[-2:])
# FG

print(string[-3:])
# EFG

print(string[-len(string):])
# 1234567890ABCDEFG

print(string[-1:0:-1])
# GFEDCBA098765432

print(string[-1::-1])
# GFEDCBA0987654321

print(string[::-1])
# GFEDCBA0987654321

print(string[:-1])
# 1234567890ABCDEF

print(string[-1::])
# G

a = np.arange(4 * 8)
b = a.reshape(4, 8)
print("b=\n", b)
print("b[:, 4:]=\n", b[:, 4:])         # row: for all row,         col: from 4 to the end
print("b[2:, :]=\n", b[2:, :])         # row: from 2 to the end.   col : row: for all row
print("b[2:, ]=\n", b[2:, ])         # row: from 2 to the end.   col : row: for all row

exit(0)
"""


# ========================================================================================================
# 단계 0:  영상이 존재하는 폴더와 파일 이름을 지정하기.
# ========================================================================================================
# 다음 사례를 활용하여 영상 파일이 있는 폴더를 적절히 지정하시오.
Path = './data/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = 'd:/CV/Images/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/@@DIP/Images/'
Name = 'lenna.bmp'
Name = 'monarch.bmp'
#Name = 'colorbar_chart2.jpg'
FullName = Path + Name

#"""
# ========================================================================================================
# 단계 1 : 영상 파일을 열어 화면에 출력하기
# ========================================================================================================
image = cv.imread(FullName)
assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.
cv.imshow('step 1: Original', image)
cv.waitKey(0)
cv.destroyWindow('step 1: Original')

# ========================================================================================================
# 단계 2 : 영상데이터의 정보를 출력한다.
# ========================================================================================================
print('\nStep 2: image.shape=', image.shape)
row, col = image.shape[:2]          # 0에서 1까지 원소를 assign한다.
ch = image.shape[-1]                # -1은 제일 마지막 원소를 의미한다.
#print('row={} col={} ch={}'.format(row, col, ch) )
print(f'row={row} col={col} ch={ch}')
# .format은 ()변수에 가장 적합한 문자열을 만들어 {}자리에 넣는다..

col, row = image.shape[1::-1]   # reverse indexing. shape[1]에서 끝(:)까지. step=-1
#print('garo={} sero={}'.format(col, row))  # 때로 가로x세로 순으로 정보가 필요할 때가 있다.
print(f'garo={col} sero={row}')
# 예: cv.resize(영상, (가로*세로)) 영상을 (가로*세로) 크기로 조절하고 싶을 때.

# ========================================================================================================
# 단계 3 : 영상의 일부를 역상으로 반전하여 출력한다.
# image가 매트릭스형 자료이므로 indexing 처리가 가능...
# ========================================================================================================

# 아래 1, 2, 3, 4의 방법 중에서 하나를 선택하여 결과를 분석하시오. => 2c 영상이 파일에서 읽어 들인 원영상이 나오는지 확인.
image2 = image                      #1. 복사하는 것이 아니다. 포인터가 서로 같아진다.
#image2 = image.astype('uint8')     #2. 원래는 데이터형을 바꾸는 목적인데 같은 형으로 복사하여 새로 만든다.
#image2 = image.astype(dtype=np.uint8)  #3. 원래는 데이터형을 바꾸는 목적인데 같은 형으로 복사하여 새로 만든다.
#image2 = image.copy()           #4. 복사하여 새로 만든다.

# 영상 일부 영역에 대하여 반전 처리
# [row, col, ch] : ','로 dimension을 구분한다.
# 3차원 데이터인데 [row, col]만 지정하면 나머지 ch의 각 채널에 대해서도 같은 처리가 이루어진다.
# 즉, [row, col, :] 지정한 것과 같은 결과를 낳는다. 맨 뒤에 있는 :은 생략 가능하다.
# [:, col, ch]은 for all row 의 의미이다. 맨 위에 있으면 아예 생략가능한데 앞에 있을 때는 :로 그 의미를 대신한다.
# 각 디멘전에서 A:B:C 로 표기 가능하다. A부터 (B-1)까지 C 간격으로 slicing 한다.
#image2[:, int(col/2):]  = 255-image[:, int(col/2):]    # col/2는 부동소수가 됨에 유의
image2[:, col//2:]  = 255-image[:, col//2:]             # int(col/2) 대신 활용 가능
cv.imshow('step 3a. right half inverted(3 channel)', image2)

image2[:, 0:int(col/2),1]  = 255-image[:, 0:int(col/2),1]       # col/2는 부동소수가 됨에 유의
cv.imshow('step 3b. right half inverted + left half inverted(G channel)', image2)
cv.imshow('step 3c. original again(Not Equal)', image)          # 질문: 원본이 손상된 이류를 설명하시오.
cv.waitKey(0)
cv.destroyAllWindows()

# ========================================================================================================
# 단계 4 : 원영상 상부를 밝게 표현하여 본다.
# ========================================================================================================
image = cv.imread(FullName)
image3 = image.astype('float64')/255
image3[int(row/2):,:]  = 1.5 * image3[int(row/2):,:]     # row/2는 부동소수가 됨에 유의
cv.imshow('step 4a. lower half brightened', image3)
cv.imshow('step 4b. original again(Equal)', image)          # image와 image2가 모두 같은 영상 어레이를 가리킨다.
cv.waitKey(0)


cv.destroyAllWindows()     # This does not work in 2.7. Fine in 3.6
exit(0)
#"""

"""
# ========================================================================================================
# 미션 과제
# 영상의 10번째 줄부터 20번째 줄까지 가로 한 줄을 특정 색상(붉은 색)으로 바꾸시오.
# ? 부분을 적절한 표현으로 작성하면 됩니다...
# ========================================================================================================
img = cv.imread(FullName)
assert img is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.
cv.imshow('Original', )                 # 읽어들인 영상 출력하기

col=img.shape[?]        # col=Number of column
RandomColor = [0, 0, 255]       # RandomColor를 붉은 색으로 지정    
img[?:?, 0:col] = RandomColor  # 특정 위치를 지정하여 가로 한 줄을 RandomColor로 대치
cv.imshow('Answer', img)        # 처리한 결과 보이기
cv.waitKey(0)
exit(0)
"""


# ========================================================================================================
# 도전과제(1)
# 본 영상의 중심부만을 칼라로 표시하고 나머지 부분은 흑백으로 표시하시오.
# 힌트: cvtColor
#   color conversion code : https://docs.opencv.org/3.4.3/d7/d1b/group__imgproc__misc.html#ga4e0972be5de079fed4e3a10e24ef5ef0
#   imgM = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# 주의: 3채널로 흑백영상을 표현하는 방법 => BGR 3개 채널을 같은 값으로 채워 넣는다.
# ========================================================================================================


# ========================================================================================================
# 도전과제(2)
# monarch.bmp 영상의 좌측 상단을 제공된 흑백영상(예: chelsea.png)을 --->>overwrite시켜라
# 가로, 세로 각각 1/2 축소한 영상으로 교체한 영상을 화면에 출력하시오.
# 이렇게 만든 영상의 픽셀 값의 RGB 각각의 총계를 제시하시오.
# ========================================================================================================
