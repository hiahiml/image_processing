"""
1. 프로그램의 기능
    OpenCV 함수로 읽은 영상을 matplot.pyplot 함수로 영상의 색상 구성 성분인 RGB 정보를 해당 색상으로 표현한다.
    matplot 함수에서 제공하는 ineteractive mode를 on/off하여 그 차이를 경험한다.

2. 프로그램의 목표
    영상 정보에서 특성 색상 정보를 추출하여 표현할 수 있다.

3. 점검 포인트
    img2[:,:,i] = img[:,:,i] # img의 i번째 채널의 모든 데이터를 img2의 해당 채널에 복사한다.

4. 사례와 함께 살펴 본 주목해야 할 함수
    b, g, r = cv.split(image)
        : 3차원 영상어레이(image)를 3개의 2차원 어레이(b, g, r)로 분할한다.
    img = cv.merge([r,g,b])
        : 2차원 영상 어레이 3개(r, g, b)를 list 자료로 만들어 이를 입력으로 하여 3차원의 영상 어레이 img를 만들어 낸다.
    imgBlank = np.zeros(img.shape, dtype='uint8')
        : 데이터가 uint8로 구성된 img.shape에 지정한 차원의 내부요소가 0의로 채워진 어레이(imgBlank)를 반환한다.
    imgR = imgBlank.copy()
        : imgBlank와 똑 같은 영상 어레이 imgR을 복사하여 만들어 낸다. 이들은 자료를 서로 공유하지 않는다.
    plt.figure(num='window title')
        : 'window title'로 이름 붙여진 새로운 창을 하나 생성해 낸다.
    plt.subplot(221) => 221의 일반화 => nmk
        : 창을 n개의 row, m개의 column으로 나눈 수 k번에 창을 지정한다. 이후 imshow(), plot() 등으로 그림을 그린다.
    plt.imshow(img)
        : 영상 array img를 화면에 출력하지만 non-interactive mode에서는 이것만으로는 영상이 출력되지 않는다.
        : interactive mode에서는 화면에 출력하고 마우스 혹은 키보드를 입력하면 다음 줄로 넘어간다.
    plt.show()
        : non-interactive mode에서는 plt.imshow()를 수행할 때 화면에 출력된다.
        : 창을 닫지 않으면 닫을 때까지 기다린다. 창을 닫아야 다음 줄로 넘어간다.
    plt.title('Original')
        : 출력한 그림 위에 타이틀을 출력한다.
    plt.axis('off')
        : 가로, 세로의 눈금을 과 대표 값들을 표시하지 않는다.
    plt.ion()
        : interactive mode로 설정한다. plt.show() 없이 plt.imshow()만으로 출력된다.
    plt.waitforbuttonpress()
        : interactive mode 사용시 키 혹은 버튼 입력을 기다린다.


5. 공통 주의 사항
    OpenCV는 영상이 BGR 순으로 배열되어 있다.
    matplot는 영상 채널 배열이 RGB로 구성되어 있다.
    따라서, matplotlib를 이용해 영상을 화면에 출력하려면 사전에 BGR 배열을 RGB 배열로 바꾸는 작업이 필요하다.

6. 미션
    맨 아래 미션을 수행하시오.

"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


#===============================================================================
# 단계 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
#===============================================================================
Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = 'd:/Work/StudyImages/Images/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/@@DIP/Images/'
Name = 'RGBColors.JPG'
Name= 'colorbar_chart.jpg'
#Name = 'lenna.bmp'
#Name = 'monarch.bmp'
FullName = Path + Name

#===============================================================================
# 단계 1 : 영상 파일을 열어 화면에 출력하기
#===============================================================================
# ImreadMode: 영상 데이터의 반환 모드를 결정
#   IMREAD_COLOR = 1            # default. 모노 영상도 3채널(RGB) 영상이 된다.
#   IMREAD_GRAYSCALE = 0        # 칼라 영상도 모노로 변환하여 연다. 1채널 영상이 됨.
#   IMREAD_UNCHANGED = -1       # 있는 그대로 열기.
image = cv.imread(FullName)     # read as 3 channel. default.
cv.imshow('color in 3 channels', image)
assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.


"""
# ========================================================================================================
# 실습 1 : matplotlib 함수를 이용하여 한 화면에 4 개의 영상을 출력한다.
# 원본 영상과 해당 영상의 RGB 성분의 영상을 해당 색상으로 출력한다.
# 3채널의 R, G, B 3개 영상 어레이를 정의하여 두고 이들을 matplotlib 함수를 이용하여 화면에 출력한다.
# ========================================================================================================

# 1) BGR 배열의 영상을 RGB 순서로 재배열한다. matplotlib는 RGB 배열을 전제로 한다.
b, g, r = cv.split(image)   # cv2는 bgr 배열을 사용한다.
print('b.shape = ', b.shape, ': g.shape = ', g.shape, ': r.shape = ', r.shape)
img = cv.merge([r,g,b])    # matplotlib에서는 rgb를 사용한다. 영상을 RGB 순으로 배열한다.
print('img.shape=', img.shape)
print('img.data=', img.data)

# 2) 여러 목적으로 활용될 입력 영상과 같은 크기의 빈 영상을 정의한다.
imgBlank = np.zeros(img.shape, dtype='uint8')   # 원영상과 같은 크기의 빈 영상을 준비한다.
print('imgBlank.shape=', imgBlank.shape)
print('imgBlank.data=', imgBlank.data)

# 3) 입력 영상의 RGB 성분을 각각 해당 영상 어레이에 정의한다. 
# 입력 영상의 해당 되는 채널의 화면 정보를 화면 출력을 위한 어레이에 복사한다.
imgR = imgBlank.copy(); imgR[:,:,0] = img[:,:,0]    # r
imgG = imgBlank.copy(); imgG[:,:,1] = img[:,:,1]    # g
imgB = imgBlank.copy(); imgB[:,:,2] = img[:,:,2]    # b

# 4) 창을 열고 화면을 2x2로 나눈 다음 첫 번째 화면에 입력 영상을 출력한다. 
plt.figure(num='Original Image & their color components')
plt.subplot(221); 
plt.imshow(img)     # 이것만으로는 영상이 출력되지 않는다. plt.imshow()를 수행할 때야 화면에 출력된다.
plt.title('Original')
plt.axis('off')             # plt.xticks([]), plt.yticks([])

# 5) 나머지 창에 R, G, B 영상 성분을 해당 색상으로 출력한다.
ii=0
for color, array in [ ['Red', imgR], ['Green', imgG], ['Blue', imgB]]:
    plt.subplot(220+ii+2)
    plt.imshow(array)
    plt.xticks([]), plt.yticks([])
    plt.title(color)
    ii += 1

plt.show()  # 창을 닫지 않으면 닫을 때까지 기다린다. 창을 닫아야 다음 줄로 넘어간다.
exit(0)
"""


"""
# ========================================================================================================
# 실습 2 - matplotlib의 interactive mode 동작
# interactive mode로 설정하여 마우스를 클릭할 때마다 matplotlib 함수를 이용하여 차례로 서브 화면에 출력한다.
# RGB 3개 평면 어레이를 만들지 않고 필요할 때마다 원본의 칼라 채널 영상을 복사하여 해당 평면의 영상을 출력한다.
# 미리 영상을 RGB 배열로 만들어 만들어 두고 사용한다.
# ========================================================================================================

b, g, r = cv.split(image)
print('b.shape = ', b.shape, ': g.shape = ', g.shape, ': r.shape = ', r.shape)
img = cv.merge([r,g,b]);    # cv2는 bgr 배열을 사용하지만, matplotlib에서는 rgb를 사용한다.
print('img.shape=', img.shape)
print('img.data=', img.data)

# interactive mode로 설정한다. plt.show() 없이 plt.imshow()만으로 출력된다.
plt.ion()

imgBlank = np.zeros(img.shape, dtype='uint8')
print('imgBlank.shape=', imgBlank.shape)
print('imgBlank.data=', imgBlank.data)

plt.figure(num='Original Image & their color components')
plt.subplot(221); plt.imshow(img)      # 입력받은 대로 출력
plt.title('Original(color)')
plt.axis('off')             # plt.xticks([]), plt.yticks([])

ii=0
for color in ['Red', 'Green', 'Blue']:
    plt.waitforbuttonpress()        # 키 혹은 버튼 입력을 기다린다.
    imgShow = imgBlank.copy()
    imgShow[:,:,ii] = img[:,:,ii]
    plt.subplot(220+ii+2)
    plt.imshow(imgShow)
    plt.axis('off')             # plt.xticks([]), plt.yticks([])
    plt.title(color)
    ii += 1

#plt.show()                 # interactive mode에서는 필요없음.
plt.waitforbuttonpress()        # 키 혹은 버튼 입력을 기다린다.
exit(0)
"""


# ========================================================================================================
# 실습 3 : 칼라 영상을 모노 영상 변환하여 이를 다양한 칼라맵을 사용하여 출력하여 본다.
# Choosing Colormaps in Matplotlib
#   https://matplotlib.org/tutorials/colors/colormaps.html?highlight=cmap
# ========================================================================================================

imgM = cv.cvtColor(image, cv.COLOR_BGR2GRAY)    # 3채널 영상을 1채널 gray로 변환
cv.imshow('gray image, imgM', imgM)
print('imgM.shape = ', imgM.shape)

plt.figure(num='images')
plt.subplot(221); plt.imshow(image); plt.title("Color")
plt.subplot(222); plt.imshow(imgM); plt.title("gray-default")   # pseudo color를 사용하여 모노 영상을 칼라링한다.
plt.subplot(223); plt.imshow(imgM, cmap='gray'); plt.title("cmap-gray") # 흑백 gray map을 사용하여 출력. cv 결과와 같다.
plt.subplot(224); plt.imshow(imgM, cmap='jet'); plt.title("cmap-jet")   # NASA의 jet engine 분사구의 온도를 pseudo color를 사용하여 표현
#plt.subplot(224); plt.imshow(imgM, cmap='ocean'); plt.title("ocean")

plt.show()
exit(0)
#=============================================================================================



#===============================================================================
# 미션 과제
# 실습 3의 그림 1(title=Color)  칼라 영상은 올바른 칼라가 표현되지 않는다.
#   OpenCV가 출력한 원본 영상(color in 3 channels)와 비교해 보시오...
# 이를 바로 잡도록 실습 3을 수정하시오.
#   힌트 - 이를 교정하기 위해서는 BGR 배열을 RGB 배열로 바꾸어야 한다.
#          이 작업을 함수를 설계하여 완성하시오.
#===============================================================================












