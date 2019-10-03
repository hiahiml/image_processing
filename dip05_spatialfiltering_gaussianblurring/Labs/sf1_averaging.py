"""
1. 개요
    코릴레이션에 의한 영상의 Averaging 처리
    내부 계수가 모두 같은 정방형의 커널로 영상에 대해 공간 필터링(spatial filtering) 동작을 행한다.

2. 동작
    평균화 처리를 처리하는 5x5, 15x15 커널을 만들어 이것으로 입력영상에 대해 코릴레이션 동작을 수행한 결과를 출력하시오.

3. 주요 함수
    correlation 을 행하는 함수, filter2D
    dst	= cv.filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
        src: source image
        dst: returned image.
        ddepth: desired depth of the destination image, see combinations
                When ddepth=-1, the output image will have the same depth as the source.=> dst.shape=src.shape.
                => When ddepth=-1, dst.dtype=src.dtype.
        kernel: convolution kernel (or rather a correlation kernel), a single-channel floating point matrix;
        anchor: anchor of the kernel that indicates the relative position of a filtered point within the kernel;
                the anchor should lie within the kernel; default value (-1,-1) means that the anchor is at the kernel center.
        delta: optional value added to the filtered pixels before storing them in dst.
        borderType:	pixel extrapolation method,

4. 미션
    소스의 맨 아랫 부분의 2개 미션을 수행하는 코드를 작성하시오.

5. 참조
    OpenCv-Python smoothing 부분
        https://docs.opencv.org/3.4.3/d4/d13/tutorial_py_filtering.html
    OpenCv-Python 한글 매뉴얼 - 기초 영상 처리
        https://opencv-python.readthedocs.io/en/latest/doc/01.imageStart/imageStart.html


"""

import numpy as np
import cv2 as cv
# 만약 matplotlib 모듈이 없다면 윈도 컴맨드 창에서 "pip install matplotlib" 명령을 수행한다.
from matplotlib import pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------
# 공통 섹션:  영상이 존재하는 폴더와 파일 이름을 지정하고 읽어내기
# ----------------------------------------------------------------------------------------------------------------------
# 다음 사례를 활용하여 영상 파일이 있는 폴더를 적절히 지정하시오.
#Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = './data/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/StudyImages/images/'
Name = 'lenna.tif'
#Name = 'monarch.bmp'
#Name = "Resolution chart.tiff"

FullName = Path + Name

img = cv.imread(FullName)

# assert condition, message  : condition이 false이면  message 출력하면서 AssertError 발생.
assert img is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

"""
# ======================================================================================================================
# 실습 1: OpenCV 기반의 간략형 실험 - averaging kernel을 사용한 filtering
# ======================================================================================================================

cv.imshow('img', img)

N = 5
kernel = np.ones((N, N),np.float32)/(N * N)         # N*N으로 나누어 정규화한다.
print(np.sum(kernel))           # 커널의 모든 원소의 값을 합하면 1이 된다.

# img 영상을 kernel로 필터링(코릴레이션 연산)하여 결과 dst를 반환한다.
# 출력 영상, dst는 shape가 입력 영상과 같다. => dst.shape=src.shape.
# -1은 출력 영상의 depth가 입력 영상과 같음을 의미한다. => dst.dtype=src.dtype.
dst = cv.filter2D(img, -1, kernel)
print('type(dst)=', type(dst), ' | dst.shape=', dst.shape, ' | dst.dtype=', dst.dtype )
cv.imshow('dst', dst)
cv.waitKey()
exit(0)
"""

# ======================================================================================================================
# 실습 2: matplotlib, OpenCV 기반의 실험 - averaging kernel을 사용한 filtering
# 영상 처리는 OpenCV 함수를 이용.
# 영상 출력은 matplotlib를 이용
# ======================================================================================================================


# ----------------------------------------------------------------------------------------------------------------------
# 단계 1 - BGR to RGB 배열을 바꾼다.
# matplotlib를 이용해 화면에 영상을 출력하려면 영상 평면을 바꾸어야 한다.
# OpenCV 함수를 이용해 BGR 배열을 RGB 배열로 바꾼다.
# ----------------------------------------------------------------------------------------------------------------------

b, g, r = cv.split(img)   # img파일을 b,g,r로 분리
img = cv.merge([r, g, b]) # b, r을 바꿔서 Merge

#plt.ion()      # interactive mode로 설정한다. plt.show() 없이 plt.imshow()만으로 출력된다.


# ----------------------------------------------------------------------------------------------------------------------
# 단계 2 - Average filter의 Kernel을 선언한다.
# 내부 요소가 1로만 이루어진 NxN 형태의 커널을 만든다.
# 커널의 계수합이 1이 되도록 정규화 해야 한다.
# ----------------------------------------------------------------------------------------------------------------------
N = 19

# 1) 커널 정의 방법 1
#kernel = np.ones((N, N), np.float32) / (N * N)      # N*N으로 나누어 커널의 합이 1이 되도록 정규화한다.

# 2) 커널 정의 방법 2
kernel = np.ones((N, N), np.float32)
kernel /= np.sum(kernel)   # 커널의 합으로 나누어 커널의 합이 1이 되도록 정규화한다.


np.set_printoptions(precision=2)    # 소수 이하 2자리까지 출력. 이하 0이면 출력 안한다.
#print('kernel=\n', kernel)          # 커널의 원소 값을 출력
print('np.sum(kernel)=', np.sum(kernel))    # 커널의 총합을 확인.

# ----------------------------------------------------------------------------------------------------------------------
# 단계 3 - correlation 연산을 행한다.
# 위의 커널으로 영상에 대해 correlation 연산을 수행한다.
# 이런 동작을 spatial filtering(공간 필터링)이라고 말한다.
# filter2D - 2차원 코릴레이션 연산을 행하는 함수
# python shell에서 help(cv.filter2D) 명령어를 입력하면 여러가지 정보를 얻을 수 있다.
# The function(filter2D) does actually compute correlation, not the convolution
# ----------------------------------------------------------------------------------------------------------------------
#dst = cv.filter2D(img, -1, kernel, borderType = cv.BORDER_DEFAULT)        # 2차원 콘벌루션 연산
dst = cv.filter2D(img, -1, kernel, borderType = cv.BORDER_ISOLATED )      # 경계처리 안함.
#dst = cv.filter2D(img, -1, kernel, borderType = cv.BORDER_REPLICATE )     # 맨 바깥 화소의 값이 중복된 것으로 간주.
print('type(img)=', type(img), ' | img.shape=', img.shape, ' | img.dtype=', img.dtype )
print('type(dst)=', type(dst), ' | dst.shape=', dst.shape, ' | dst.dtype=', dst.dtype )

# 단계 3 --------------------------------------
# 서브화면에 원본과 처리 결과를 출력한다. 이후 마우스를 입력할 때까지 기다린다.
# subplot(NMK)가 의미하는 것 : 화면을 rowXcolumn(NxM)개의 sub 창으로 나누고 K 번째 서브창을 지정한다.
# 이후 imshow() 함수는 지정된 sub 창에 출력한다.
plt.subplot(121)        # 1x2 서브 화면에서 1 번을 지정.
plt.imshow(img)
plt.title('Original')   # 지정된 sub 창에 그림 제목을 출력한다.
plt.xticks([]), plt.yticks([])      # x축, y축에 label을 출력하지 않는다.

plt.subplot(122),plt.imshow(dst),plt.title('Averaging: N='+ str(N)) # 1x2 서브 화면에서 2 번을 지정.
plt.axis('off')                     # x축, y축에 label을 출력하지 않는다.

# 마우스 버튼을 기다린다.  interactive mode 일 때 활성화 시키기 바람
#plt.waitforbuttonpress()   # 현 화면에서 버튼 입력을 기다린다.


plt.show()      # interactive mode 일 때는 필요 없음
# 이후 프로그램이 종료되므로 모든 창이 닫힌다.
exit(0)


# ======================================================================================================================
# 실습 3: matplotlib 기반의 실험 - averaging kernel을 사용한 filtering
# 영상 출력은 matplotlib를 이용. non-interactive mode
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
# 단계 1 - BGR to RGB 배열을 바꾼다.
# matplotlib를 이용해 화면에 영상을 출력하려면 영상 평면을 바꾸어야 한다.
# OpenCV 함수를 이용해 BGR 배열을 RGB 배열로 바꾼다.
# ----------------------------------------------------------------------------------------------------------------------
b, g, r = cv.split(img)   # img파일을 b,g,r로 분리
img = cv.merge([r, g, b]) # b, r을 바꿔서 Merge

# ----------------------------------------------------------------------------------------------------------------------
# 단계 2 - Average filter의 Kernel을 선언한다.
# 내부 요소가 1로만 이루어진 NxN 형태의 커널을 만든다.
# 커널의 계수합이 1이 되도록 정규화 해야 한다.
# ----------------------------------------------------------------------------------------------------------------------
N = 11

kernel_list =[]         # 다수의 커널로 list 자료로 기록한다.
# 1) 1xN 커널 정의
kernel = np.ones((1, N), np.float32) / (N)      # 주의!!! N으로 나누어 커널의 합이 1이 되도록 정규화한다.
print('np.sum(kernel)=', np.sum(kernel))    # 커널의 총합을 확인.
kernel_list.append(kernel)

# 2) Nx1 커널 정의
kernel = np.ones((N, 1), np.float32)
kernel /= np.sum(kernel)   # 커널의 합으로 나누어 커널의 합이 1이 되도록 정규화한다.
print('np.sum(kernel)=', np.sum(kernel))    # 커널의 총합을 확인.
kernel_list.append(kernel)

print(type(kernel_list))

#np.set_printoptions(precision=2)    # 소수 이하 2자리까지 출력. 이하 0이면 출력 안한다.
#print('kernel=\n', kernel)          # 커널의 원소 값을 출력


# ----------------------------------------------------------------------------------------------------------------------
# 단계 3 - correlation 연산을 행하고 그 결과를 pyplot 결과창에 출력한다.
# 위의 커널 list로 영상에 대해 correlation 연산을 수행한다.
# ----------------------------------------------------------------------------------------------------------------------

plt.figure(num='average filtering')
plt.subplot(131)    # 1x3 창의 첫번째 창 선택
plt.imshow(img)     # 원본 영상
plt.axis('off')
plt.title('Original')

i = 0   # kernel index
for knl in kernel_list:
    print(type(knl), knl.shape)
    dst = cv.filter2D(img, -1, knl, borderType=cv.BORDER_DEFAULT)
    plt.subplot(130 + (i+2))      # 1x3 창의  (i+2)번째 창 선택
    plt.imshow(dst)     # filtering 결과 영상
    plt.axis('off')
    plt.title('Kernel=' + str(knl.shape))
    i += 1

plt.show()      # interactive mode 일 때는 필요 없음
# 이후 프로그램이 종료되므로 모든 창이 닫힌다.
exit(0)




# ======================================================================================================================
# 미션 1: 실습 2를 interactive mode로 작동시켜보시오.
# ======================================================================================================================

# ======================================================================================================================
# 미션 3: 커널의 크기가 5x5, 15x15, 31x31의 average filtering 결과를 원본 영상과 함께 2x2 화면에 출력하시오
# ======================================================================================================================
