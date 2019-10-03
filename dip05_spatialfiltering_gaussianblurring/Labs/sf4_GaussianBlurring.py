"""
1. 개요
    코릴레이션에 의한 영상의 Gaussain Blurring 처리
    2차원 가우시안 함수로 만들어진 커널을 이용해 영상에 대해 공간 필터링(spatial filtering) 동작을 행한다.

2. 목표
    1) 가우시안 블러링이 적용되는 원리를 이해한다.
    2) 블러링을 OpenCV에서 지원하는 함수를 이용하여 구현하는 방법을 이해한다.
        실습 1) GaussianBlur() 함수를 사용하는 방법 - 원 영상에 2차원 가우시안 블러링을 행하는 함수
                출력 결과는 OpenCV로 보인다.
        실습 2) OpenCV의 1차원 가우시안 커널을 구하는 함수와 1차원 커널기반의 코릴레이션 함수, sepFilter2D의 사용법을 익힌다.
                이를 이용해 가로, 세로 각각 1회 필터링을 행한다.
                getGaussianKernel - 1차원 가우시안 커널 구하기
                sepFilter2D - 1차원 커널 2개로 총 2회의 필터링을 행하기
                출력 결과를 pyplot로 보인다.
        실습 3) 2차원 가우시안 커널을 구하고 filter2D 함수로 1회의 필터링 연산을 행하는 방법
        - 작성하지 않았음.
3. 미션
    1. 실습 1의 예제를 pyplot으로 원본과 블러링 된 영상 2개(시그마=3, 시그마=15) 를 한 화면에 출력하시오.
    2. 원영상과 시그마(= 2, 5, 15)에 따른 다양한 출력 결과를 subplot을 이용하여 한꺼번에 출력하시오.
        조건 :
            시그마=2는 1차원 가우시안 커널로 가로 방향만 filter2D() 함수로 블러링. 필터는 가우시안 연산식을 통해 직접 정의할 것.
            시그마=5는 1차원 가우시안 커널로 세로 방향만 GaussianBlur() 함수로 블러링.
            시그마=15는 2차원 가우시안 커널로 양방향으로 filter2D() 함수로 블러링. getGaussianKernel을 기반으로 2차원 필터를 정의할 것.

4. 참고
    OpenCv-Python smoothing 부분
        https://docs.opencv.org/3.4.3/d4/d13/tutorial_py_filtering.html
    OpenCv-Python 한글 매뉴얼 - 기초 영상 처리
        https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html



"""


import numpy as np
import cv2 as cv
# 만약 matplotlib 모듈이 없다면 윈도 컴맨드 창에서 "pip install matplotlib" 명령을 수행한다. 
from matplotlib import pyplot as plt



#----------  영상이 존재하는 폴더와 파일 이름을 지정하기.
# 다음 사례를 활용하여 영상 파일이 있는 폴더를 적절히 지정하시오.
#Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = './data/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/@@DIP/LectureMaterials/Images/'
#Path = 'd:/work/StudyImages/images/'
#Name = 'lenna.tif'
#Name = 'monarch.bmp'
Name = 'Resolution chart.tiff'
FullName = Path + Name

img = cv.imread(FullName)
# assert condition, message  : condition이 false이면  message 출력하면서 AssertError 발생.
assert img is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

"""
# ======================================================================================================================
# 실습 1 : GaussianBlur() 함수를 사용하는 방법
# ======================================================================================================================
#       미션 - 원영상과 파라미터에 따른 다양한 출력 결과를 subplot을 이용하여 한꺼번에 출력하시오.
#       질문 - 시그마 값에 비해 지나치게 작은 크기의 커널은 평균 필터와 같다. 이유를 설명하시오.
# 함수를 사용해 가장 편리한 방법으로 블러링한다.

# 활용 1) 시그마를 제시하고 적절한 커널 크기를 자동 산정하게 하는 방안. 추천방안. 양방향 블러링
# ksize=(0, 0)-> 시그마로부터 계산. (가로, 세로)로 표기됨에 유의할 것. 대략; 커널 사이즈 = 6*sigma +1
#blur = cv.GaussianBlur(img, (0, 0), 9)     # 시그마=9의 값으로 양방향으로 블러링.
#blur = cv.GaussianBlur(src=img, ksize=(0, 0), sigmaX=9)     # 키워드를 제시하는 방식. 양방향으로 블러링.
#blur = cv.GaussianBlur(src=img, ksize=(0, 0), sigmaX=9, sigmaY=0 )     # 양방향으로 블러링.

# 활용 2) 시그마를 제시하고 적절한 커널 크기를 자동 산정하게 하는 방안. 추천방안. 한 쪽 방향 블러링
# sigmaX, sigmaY 값의 지정으로 X축 혹은 Y축 블러링을 선택적으로 시행할 수 있다.
#blur = cv.GaussianBlur(src=img, ksize=(0, 0), sigmaX=9, sigmaY=0.1 )   # 가로축으로 블러링.
#blur = cv.GaussianBlur(src=img,ksize=(0,0),sigmaX=0.1, sigmaY=9 )      # 세로축으로 블러링.


# 활용 3) 커널 사이즈를 제시하고 그에 따라 자체적으로 적당한 시그마를 계산하는 방안
#blur = cv.GaussianBlur(img, (21, 21), 0)    # ksize로 부터 시그마를 계산.
#blur = cv.GaussianBlur(img, (1, 21), 0)     # ksize로 부터 시그마를 계산. 세로 방향의 블러링
#blur = cv.GaussianBlur(img, (21, 1), 0)     # ksize로 부터 시그마를 계산. 가로 방향의 블러링

# 활용 4) 주의 사례: 오류는 아니지만 바람직하지 않은 파라미터
blur = cv.GaussianBlur(src=img, ksize=(51,51), sigmaX=1)    # 시그마에 비해 커널의 크기가 크다. => 연산낭비.
#blur = cv.GaussianBlur(img, (5,5), 15)  # 시그마 값에 비해 지나치게 작은 크기의 커널을 사용한다. => 부정확 처리

cv.imshow('Gaussian Blur', blur)
cv.waitKey()
exit(0)
"""

# ======================================================================================================================
# 실습 2: OpenCV의 1차원 가우시안 커널을 구하는 함수와 1차원 커널기반의 코릴레이션 함수, sepFilter2D의 사용법을 익힌다.
#       getGaussianKernel - 1차원 가우시안 커널 구하기
#       sepFilter2D - 1차원 커널 2개로 이를 이용해 가로, 세로 각각 1회 총 2회의 필터링을 행한다.
# ======================================================================================================================

# -----------------------------------------------------------------------------------------------
# 1단계 : 평상 평면을 BGR -> RGB 순으로 재배열한다.
# matplotlib를 이용해 화면에 영상을 출력하려면 영상 평면 배열을 RGB로 바꾸어야 한다.
# OpenCV 함수를 이용해 BGR 평면 배열을 RGB 평면 배열로 바꾼다.
# -----------------------------------------------------------------------------------------------
b, g, r = cv.split(img)   # img 파일을 b,g,r로 분리
img = cv.merge([r, g, b]) # b, r을 바꿔서 Merge


# -----------------------------------------------------------------------------------------------
# 2단계 : 1차원 커널을 구하고 가로, 세로 각각 1회 필터링을 행하는 방법
# -----------------------------------------------------------------------------------------------

# 세부 단계 2a --------------------------------------
# 함수를 호출하여 가우시안 커널을 구한다.
# retval = cv.getGaussianKernel(ksize, sigma[, ktype] )
# The function computes and returns the ksize×1 matrix of Gaussian filter coefficients
# ktype	Type of filter coefficients. It can be CV_32F or CV_64F
k=11; s=2; t = cv.CV_32F;
k_1D = cv.getGaussianKernel(ksize=k, sigma=s, ktype=t)
np.set_printoptions(precision=2)    # 소수 이하 2자리까지 출력. 이하 0이면 출력 안한다.
print('type(k_1D)=', type(k_1D), '| k_1D.shape=', k_1D.shape, '\nk_1D.T=\n', k_1D.T)


# 세부 단계 2b --------------------------------------
# 1차원 커널을 X축, Y축에 각각 1회씩 적용하여 2차원 correlation 연산을 수행한다.
# dst	=	cv.sepFilter2D(	src, ddepth, kernelX, kernelY[, dst[, anchor[, delta[, borderType]]]]	)
# The function applies a separable linear filter to the image.
# That is, first, every row of src is filtered with the 1D kernel kernelX.
# Then, every column of the result is filtered with the 1D kernel kernelY.
# The final result shifted by delta is stored in dst.

dst = cv.sepFilter2D(src=img, ddepth=-1, kernelX=k_1D, kernelY=k_1D.T)
#--->>>연산량감소,
# 단계 3 --------------------------------------
# 서브화면에 원본과 처리 결과를 출력한다. 이후 마우스를 입력할 때까지 기다린다.
# subplot(NMK)가 의미하는 것 : 화면을 rowXcolumn(NxM)개의 sub 창으로 나누고 K 번째 서브창을 지정한다.
# 이후 imshow() 함수는 지정된 sub 창에 출력한다.
plt.subplot(121)        # 1x2 서브 화면에서 1 번을 지정.
plt.imshow(img)
plt.title('Original')   # 지정된 sub 창에 그림 제목을 출력한다.
plt.xticks([]), plt.yticks([])      # x축, y축에 label을 출력하지 않는다. 검은 테두리는 출력한다.

plt.subplot(122), plt.imshow(dst),plt.title('Gaussain Blurring: sigma=' + str(s) ) # 1x2 서브 화면에서 2 번을 지정.
plt.xticks([]), plt.yticks([])      # x축, y축에 label을 출력하지 않는다. 검은 테두리는 출력한다.
#plt.axis('off')        # 라벨과 테두리 모두 없앤다.


# 이후 프로그램이 종료되므로 모든 창이 닫힌다.
plt.show()