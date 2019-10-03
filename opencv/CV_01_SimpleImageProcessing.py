"""
개요
    영상 파일을 읽어들여 간단한 밝기 변화와 영상 조작을 행하고 이를 화면에 출력한다.

동작
    단계 1 : 영상 파일을 읽어 들여 화면에 출력하기
    단계 2 : 간단한 영상 처리
    단계 3: 영상 데이터를 0~1 범위의 부동소수로 만들어 출력하기
    단계 4 : 0~1의 부동소수 데이터를 uint8형으로 바꾸어서 출력하기
        1) astype() 메소드를 사용하여 바꾸기
        2) threshold() 함수를 사용하여 255보다 큰 값은 모두 255로 표현하는 truncation을 시행하기
        3) numpy.clip() 함수를 이용한 값의 범위 지정

함수
    1. numpy.amax, numpy.amin: ndarray의 최대/최소 값을 반환.
    2. ndarray.astype(dtype='uint8'): ndarray를 uint8형으로 바꾼다.
    3. threshold(): 영상 데이터의 임계치에 따라 값을 변환
    4. numpy.clip(): 값의 범위(min, max)를 지정하여 범위를 넘는 값은 min 혹은 max의 값을 갖게 clipping하기
    5. numpy.array_equal(a, b): 어레이 a, b가 같은가 비교한다.

질문
    1. 각 단계의 설명부에 제시된 질문에 답하시오.
    2. 영상을 밝게(곱하기) 혹은 어둡게(나누기) 표현하기 위해 처리된 데이터는 출력을 위해 어떻게 가공되어야 하는지 설명하시오.
        a) 표현할 데이터가 부동소수일 경우
        b) 표현할 데이터가 uint8형일 경우

"""
import cv2  as cv
import numpy as np

# ========================================================================================================
# 단계 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
# ========================================================================================================
Path = './data/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = 'd:/CV/Images/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/@@DIP/Images/'
Path = './data/'
Name = 'RGBColors.JPG'
Name2= 'colorbar_chart.jpg'
Name1 = 'lenna.tif'
Name = 'monarch.bmp'
FullName = Path + Name
FullName2 = Path + Name2

# ========================================================================================================
# 단계 1 : 영상 파일을 읽어 들여 화면에 출력하기
# ========================================================================================================
# ImreadMode: 영상 데이터의 반환 모드를 결정
#   IMREAD_COLOR = 1            # default. 모노 영상도 3채널(RGB) 영상이 된다.
#   IMREAD_GRAYSCALE = 0        # 칼라 영상도 모노로 변환하여 연다. 1채널 영상이 됨.
#   IMREAD_UNCHANGED = -1       # 있는 그대로 열기.
image = cv.imread(FullName, cv.IMREAD_UNCHANGED)      # IMREAD_COLOR라면 생략가능
assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.
winname = '1. image : ImReadMode=' + str(cv.IMREAD_UNCHANGED)
cv.imshow(winname, image)
cv.waitKey(0)
cv.destroyWindow(winname)

# ========================================================================================================
# 단계 2 : 간단한 영상 처리
# 질문 1: 파일에서 읽은 영상 어레이이 1.5을 곱하면 데이터 형은 어떻게 변하는가?
# 질문 2: 부동소수 영상을 imshow() 함수를 통해 화면에 출력하기 위한 조건은?
# ========================================================================================================
print('\nStep 2')

# 1) 역상(반전) 영상 출력하기
imageR = 255-image
print('1) image.dtype = ', image.dtype)  # 어레이 요소의 데이터 타입 알아내기.
# 1) image.dtype =  uint8

print('1) imageR.dtype = ', imageR.dtype)
# 1) imageR.dtype =  uint8

cv.imshow('2a. reverse_image, imageR', imageR)
cv.waitKey(0)
cv.destroyWindow('2a. reverse_image, imageR')

# 2) 영상의 명암을 밝게 혹은 어둡게 처리하고자 한다. - 오류 상황
image1 = image * 1.5
image2 = image / 1.5
cv.imshow('2b. Brighter', image1)
cv.imshow('2c. Darker', image2)
print('2) imag1.dtype = ', image1.dtype)
# 2) imag1.dtype =  float64

print('2) imag2.dtype = ', image2.dtype)
# 2) imag2.dtype =  float64

print('Error!! Why the blank screens?')        # 질문? : 힌트 - 영상 데이터 어레이의 데이터 형(dtype) 관찰.
cv.waitKey(0)
cv.destroyWindow('2b. Brighter')
cv.destroyWindow('2c. Darker')


# ========================================================================================================
# 단계 3: 영상 데이터를 0~1 범위의 부동소수로 만들어 출력하기
# imshow()는 uint8 데이터 혹은 0~1 범위의 부동소수만을 올바르게 출력한다.
# 부동소수 데이터가 1보다 큰 데이터는 1인 것으로 간주하여 출력한다.
# 질문 1: 부동소수 영상 데이터가 25이다. imshow() 함수는 이를 어떻게 표현하는가?
# 질문 2: 영상어레이의 최소 혹은 최대 값을 구하는 함수는?
# 질문 3: min, max 함수로 영상어레이의 최소 혹은 최대 값을 알아내는 방법은?
# ========================================================================================================
print('\nStep 3')
# 1) 영상을 부동소수로 만들어 역상 영상을 출력한다.
imageF = image/255
print('1) imagF.dtype = ', imageF.dtype)
# 1) imagF.dtype =  float64

imageR = 1-imageF
cv.imshow('3a. reversed image, imageR',imageR)
cv.waitKey(0)
cv.destroyWindow('3a. reversed image, imageR')


# 2) 부동 소수 데이터에 대해 명암 변환 처리를 시행한다.
# 이 경우 1의 보다 큰 영상 데이터는 1인 것으로 간주되어 출력된다.
image1 = imageF * 1.5
image2 = imageF / 1.5
cv.imshow('3b. Brighter', image1)
cv.imshow('3c. Darker', image2)
print('2) imag1.dtype = ', image1.dtype)
# 2) imag1.dtype =  float64

print('2) imag2.dtype = ', image2.dtype)
# 2) imag2.dtype =  float64

# 3) 영상 어레이의 값의 범위를 확인하기 위해 데이터 중에서 화소 값의 최대, 최소를 출력한다.
print("3) np.amax(image1)=", np.amax(image1))  # numpy.amax: numpy 배열의 원소 중의 최대 값
# 3) np.amax(image1)= 1.488235294117647

print("3) np.amin(image1)=", np.amin(image1))  # numpy.amin: numpy 배열의 원소 중의 최소 값
# 3) np.amin(image1)= 0.0

print("3) image1.max()=", image1.max())  # 객체의 메소스들 사용한 최대 값
# 3) image1.max()= 1.488235294117647

print("3) image1.min()=", image1.min())  # 객체의 메소스들 사용한 최소 값
# 3) image1.min()= 0.0

# 파이썬에 내장된 min/max 함수는 사용이 불편하다. 아래 예제 참고 바람.
# a=[ [1, 2], [3,4]]
# min(min(a))           # 1
# max(max(a))           # 4

cv.waitKey(0)
cv.destroyWindow('3b. Brighter')
cv.destroyWindow('3c. Darker')


# ========================================================================================================
# 단계 4 : 0~1의 부동소수 데이터를 uint8형으로 바꾸어서 출력하기
# 질문 1: 단계 4의 1)에서 영상에 오류가 발생한 원인을 설명하시오.
# 질문 2: threshold() 함수의 truncation 동작을 그림과 함께 상세히 설명하시오.
# ========================================================================================================

print('\nStep 4')
# 1) astype() 메소드를 사용하여 바꾸기
# 단계 3에서 넘어온 image1 어레이는 1보타 큰 값을 내포하고 있는 부동소수로 이루어진 배열이다.
# 여기에 255를 곱한 수에 대한 uint8 정수형 변환을 행한다.
# 255를 넘는 수는 255가 되는 것이 아니라 그 수에 대한 정수형의 하위 8비트를 취하는 동작을 수행한다.
# 본 예제의 최하단 참고 예제를 관찰하기 바람.

dst1 = (255*image1).astype(dtype='uint8')           # 주의: 괄호를 써야함. (255*image1)
#dst1 = (255*image1).astype(dtype=np.uint8)         # 위와 같은 표현임.

cv.imshow("4a. astype(dtype='uint8')", dst1)

cv.waitKey(0)
cv.destroyWindow("4a. astype(dtype='uint8')")


# 2) threshold() 함수를 사용하여 255보다 큰 값은 모두 255로 표현하는 truncation을 시행하기
# threshold() 함수의 용법
#retval, dst = cv.threshold(src, thresh, maxval, type[, dst])
thresh = 1.0         # 경계치. 이보다 큰 값은 truncation된다.

# maxval 파라미터는 현재는 활용하지 않음.
# THRESH_BINARY, THRESH_BINARY_INV에서 사용. 경계치를 넘으면 이 값을 사용한다.
maxval = 0

# threshold 함수 : retval, dst =	cv.threshold(src, thresh, maxval, type[, dst])
# 여기는 threshold() 함수는 입력 영상에 대해 임계값을 정하여 그 보다 크면
# 최대값으로 clipping하는 동작을 수행하는 용도로 사용하였다.
#   src	- input array (multiple-channel, 8-bit or 32-bit floating point).
#   dst - output array of the same size and type and the same number of channels as src.
#   thresh - threshold value.
#   maxval - maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
#   type - thresholding type (see ThresholdTypes).

# cv.THRESH_TRUNC : thresh를 넘는 값들은 모두 thresh 값으로 치환한다.
# 단계 3에서 넘어온 image1 어레이는 1보타 큰 값을 내포하고 있는 부동소수로 이루어진 배열이다.
retval, dst	= cv.threshold(image1, thresh, maxval, type=cv.THRESH_TRUNC)


print("2) retval=", retval)     # 오쯔 알고리즘을 쓰지 않는한 반환 값은 의미를 해석할 필요가 없다.
# 2) retval= 1.0

dst2=(255*dst).astype(dtype='uint8')                # 주의: 괄호를 써야함. (255*dst)
print("2) Max2 pixel value=", np.amax(dst2))
# 2) Max2 pixel value= 255

print("2) Min2 pixel value=", np.amin(dst2))
# 2) Min2 pixel value= 0

cv.imshow('4b. threshold UINT8 image(THRESH_TRUNC)', dst2)
cv.waitKey(0)
cv.destroyWindow('4b. threshold UINT8 image(THRESH_TRUNC)')


# 3) numpy.clip() 함수를 이용한 값의 범위 지정
# 단계 3에서 넘어온 image1 어레이는 1보타 큰 값을 내포하고 있는 부동소수로 이루어진 배열이다.
clip_img = np.clip(image1, 0, 1)        # 0~1의 범위 값은 그대로 두고 나머지 범위는 잘라내기.=> 0보다 작으면 0, 1보다 크면 1.
clip_img = (255*clip_img).astype(dtype='uint8')
print('2) ', np.array_equal(clip_img, dst2))    # 두 영상이 같은지 진위 여부를 출력
# 2) True

cv.imshow('5. clip image', clip_img)

cv.waitKey(0)
cv.destroyAllWindows()     # This does not work in 2.7. Fine in 3.7
exit(0)





#--------------------------------------------------------------------------
# 참고 예제 - astype()으로 자료형 바꾸기
# 0~255를 넘어서는 범위의 부동 소수형 데이터에 대해 uint8형으로 자료형을 바꾸면
# 255이상의 수는 255로 clipping되지 않고 부동 소수를 32비트로 정수로 바꾼 다음에 하위 8비트만 취한다.
#--------------------------------------------------------------------------
a = np.random.uniform(0, 5.0, size=(4,3))   # 0~5.0의 분포를 가진 4x3 어레이 생성
print('\na=\n', a)
# a=
#  [[3.9269126  4.90935897 0.81033026]
#  [1.78459042 3.32592098 2.79407259]
#  [1.21676514 1.89058453 3.84862031]
#  [1.79393754 4.62214923 2.65264582]]

b = 255*a
print('\nb=\n', b)
# b=
#  [[1001.36271424 1251.88653788  206.63421521]
#  [ 455.07055696  848.10985002  712.48851111]
#  [ 310.27511192  482.09905517  981.39817844]
#  [ 457.45407315 1178.64805416  676.42468284]]

c = b.astype(dtype=np.uint8)                # uint8 타입으로 변경하기
print('\nc=\n', c)
# c=
#  [[233 227 206]
#  [199  80 200]
#  [ 54 226 213]
#  [201 154 164]]

bb = b.astype(np.uint32)
print('\nbb=\n', bb)
# bb=
#  [[ 119 1073 1103]
#  [1094   66  386]
#  [ 256  822  233]
#  [ 161  765  897]]

bb1 = bb & 0xff                 # bb1은 c어레이와 같은 값을 가진다.
print('\nbb1=\n', bb1)
# bb1=
#  [[119  49  79]
#  [ 70  66 130]
#  [  0  54 233]
#  [161 253 129]]


exit(0)