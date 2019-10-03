"""

1. 개요
    plt 함수로 OpenCV와 유사한 환경을 만들어 내었다. => plt를 interactive mode로 작동하게 한다.

2. 점검 포인트
    1) interactive mode로 설정하여 imshow() 없이 imshow()만으로 출력된다.
    2) 마우스 버튼으로 다음 과정으로 진행하게 하였다. 키보드 입력을 받지 않음.
    3) 창 번호를 지정하여 해당 창에 대해 영상처리를 할 수 있다.
    4) subplot 함수를 이용하여 창을 지정한 매트릭스로 나누어 원하는 서브 창에 출력한다.
    5) figure()로 새로운 창을 여는 방법이 달라졌다.
    6) x, y축의 라벨을 다르게 지정해 보았다.
    7) 지정하는 창을 닫도록 설계하였다.

"""


import numpy as np
import cv2 as cv
# 만약 matplotlib 모듈이 없다면 윈도 컴맨드 창에서 "pip install matplotlib" 명령을 수행한다. 
from matplotlib import pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------
# 단계 1:  영상이 존재하는 폴더와 파일 이름을 지정하고 읽어내기
# ----------------------------------------------------------------------------------------------------------------------
# 다음 사례를 활용하여 영상 파일이 있는 폴더를 적절히 지정하시오.
#Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
Path = 'd:/work/@@DIP/LectureMaterials/Images/'
Name = 'lenna.bmp'
#Name = 'monarch.bmp'
FullName = Path + Name

img = cv.imread(FullName)
print('type(img)= ', type(img),'img.dtype=', img.dtype)

# assert condition, message  : condition이 false이면  message 출력하면서 AssertError 발생.
assert img is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.


# ----------------------------------------------------------------------------------------------------------------------
# 단계 2 - interactive mode로 설정한다.
# 인터랙티브 모드에서는 plt.show() 함수의 수행없이 plt.imshow()만으로 화면의 내용이 출력된 후 사용자의 입력을 기다린다.
# 다음 과정으로 넘어가고자 할 때는 활성창에 마우스 버튼을 지정하고 클릭한다.
# 이때는 해당 창이 소거된다.
# ----------------------------------------------------------------------------------------------------------------------
plt.ion()


# ----------------------------------------------------------------------------------------------------------------------
# 단계 3 - 창 생성 하기
# 새로운 창을 생성하여 영상을 출력한다.
# 창의 이름을 지정하면 그 이름으로 창이 생성되면 번호는 생성 순서에 따라 부여받는다.
# 여기서는 처음 창을 열기 때문에 Figure 1의 이름으로 생성된다.
# 창의 이름을 지정하지 않으면 디폴트 창 번호가 1번으로 시작한다.
# ----------------------------------------------------------------------------------------------------------------------
#plt.figure()               # Figure 1 이름으로 창이 생성된다.
plt.figure(num='window1')   # 출력할 윈도 이름 지정하기하여 새로 열기
plt.imshow(img)
plt.title('step 3: BGR data from OpenCV')   # 지정된 sub 창에 그림 제목을 출력한다.

# x축, y축에 라벨링에 변화를 주었다.
# 축의 라벨링을 삭제하고 싶으면 plt.axis('off') 명령을 수행한다.
plt.xticks(np.arange(0, img.shape[1], step=100))    # 100 픽셀 단위의 가로 축 눈금
plt.yticks(np.arange(0, img.shape[0], step=50))     # 50 픽셀 단위의 가로 축 눈금
#locs, labels = plt.xticks(); print(locs); print(labels)


# ----------------------------------------------------------------------------------------------------------------------
# 단계 4 - BGR to RGB 배열 바꿔 출력하기
# OpenCV 함수를 이용해 BGR 배열을 RGB 배열로 바꾼 후,
# 새로운 창을 하나 더 만들어서 재 배열된 영상을 출력한다.
# ----------------------------------------------------------------------------------------------------------------------
b, g, r = cv.split(img)     # img파일을 b,g,r로 분리
img2 = cv.merge([r,g,b])    #  b, r을 바꿔서 Merge

plt.figure(num='window2')   # 출력할 윈도 이름 지정하기하여 새로 열기
plt.title('step4: RGB data re-arranged')   # 지정된 sub 창에 그림 제목을 출력한다.
plt.imshow(img2)

# 마우스 버튼을 기다린다.
# This will return True is a key was pressed,
# False if a mouse button was pressed
# and None if timeout was reached without either being pressed.
plt.waitforbuttonpress()        # window2에서 버튼 입력을 기다린다.
# 현재의 창에서 마우스 버튼을 입력하면 현재의 창이 닫히고 다음 루틴으로 진입한다.

# ----------------------------------------------------------------------------------------------------------------------
# 단계 5 - 창의 이름 혹은 창 번호를 지정하여 영상 출력하기
# 창번호 1에 가서 그 내용을 바꾸어 놓는다.
# ----------------------------------------------------------------------------------------------------------------------
plt.figure(num='window1')   # = plt.figure(1) 창의 이름 혹은 창 번호를 지정해도 동작은 같다.
plt.axis('off')
plt.imshow(img2)
plt.title('step 5: Tell me two differences')

plt.waitforbuttonpress()        # window1에서 버튼 입력을 기다린다.


# ----------------------------------------------------------------------------------------------------------------------
# 단계 6 - 역상처리
# matplotlib.pyplot는 데이터 범위에 유연성이 있다.
# ----------------------------------------------------------------------------------------------------------------------

# a) 'window2'에 역상을 출력한다.
plt.figure('window2')
plt.imshow(255-img2)        # OpenCV에서는 이것만 역상처리가 된다.
plt.title('step 6a: plt.imshow(255-img2)')
plt.waitforbuttonpress()        # 'window2'에서 버튼 입력을 기다린다.

# b) 'window1'에 역상을 출력한다.
plt.figure(1)               # window 1
plt.imshow(-img2)          # 255-img2와 -img2는 같은 값이다.
plt.title('step 6b: plt.imshow(-img2)')
plt.waitforbuttonpress()    # 'window2'에서 버튼 입력을 기다린다.
plt.close(1)                # 1번창만 닫는다.


# ----------------------------------------------------------------------------------------------------------------------
# 단계 7
# 여러 화면으로 구성된 창을 생성한다.
# subplot(NMK)가 의미하는 것 : 화면을 rowXcolumn(NxM)개의 sub 창으로 나누고 K 번째 서브창을 지정한다.
# 이후 imshow() 함수는 지정된 sub 창에 출력한다.
# ----------------------------------------------------------------------------------------------------------------------
plt.figure('subplot')       # 새창을 하나 더 연다.
plt.subplot(121),plt.imshow(img),plt.title('step 7a: BGR data')  # 1x2 서브 화면에서 1 번을 지정.
#plt.xticks([]), plt.yticks([])      # x축, y축에 label을 출력하지 않는다.
plt.axis('off')
plt.subplot(122),plt.imshow(img2),plt.title('step 7b: RGB data') # 1x2 서브 화면에서 2 번을 지정.
plt.axis('off')
plt.waitforbuttonpress()        # 'subplot'에서 버튼 입력을 기다린다.

# 이후 프로그램이 종료되므로 모든 창이 닫힌다.
