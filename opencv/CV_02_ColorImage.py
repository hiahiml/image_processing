
"""
개요
    0으로 초기화된 빈 영상 어레이를 선언한다.
    이곳에 특정 영상의 칼라 채널을 복사해서 해당 색상으로 그 채널 영상을 보인다.

동작

함수

질문
    각 단계에서의 질문에 답하시오
"""
import cv2  as cv
import numpy as np


#===============================================================================
# 단계 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
# 질문 1: 영상 데이터의 여러 속성을 제시하고 그 의미를 설명하시오.
# 질문 2: eval() 함수의 용법에 대하여 설명하시오.
# 질문 3: printImgAtt('image') 표현식에서 'image'을 스트링으로 처리해야 하는 이유를 설명하시오.
#===============================================================================
Path = './data/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/@@DIP/Images/'
Name = 'RGBColors.JPG'
Name= 'colorbar_chart.jpg'
#Name = 'lenna.bmp'
#Name = 'monarch.bmp'
FullName = Path + Name

def printImgAtt (string):
    print("\n" + string)
    data = eval(string)
    print(' type :', type(data))           # imge type =  <class 'numpy.ndarray'>
    print(' shape = ', data.shape)      # 영상 어레이의 크기 알아내기. image shape =  (512, 768, 3). (행, 열, 채널)
    print(' data type = ', data.dtype) # 어레이 요소의 데이터 타입 알아내기. uint8 = unsigned 8비트.
    if len(data.shape) >=2:
        print(' row = ', data.shape[0])  # shape는 tuple이다. 원소는 []로 지정. 리스트도 []로 지정한다.
        print(' column = ', data.shape[1])  # 열의 수.
        if len(data.shape) ==3:
            print(' channel = ', data.shape[2])  # 채널의 수. 칼라 영상이면 3. 모도 영상이면 1.


# ========================================================================================================
print("\n단계 1 : 영상 파일을 열어 화면에 출력하기")
# ========================================================================================================
# ImreadMode: 영상 데이터의 반환 모드를 결정
#   IMREAD_COLOR = 1            # default. 모노 영상도 3채널(RGB) 영상이 된다.
#   IMREAD_GRAYSCALE = 0        # 칼라 영상도 모노로 변환하여 연다. 1채널 영상이 됨.
#   IMREAD_UNCHANGED = -1       # 있는 그대로 열기.
image = cv.imread(FullName)     # read as 3 channel. default.
if image is None:               # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.
    print('No image file....!')
    exit(0)     # 종료
#assert img is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.
cv.imshow('color in 3 channels', image)
cv.waitKey()
cv.destroyWindow('color in 3 channels')

# ========================================================================================================
print("\n단계 2 : BGR 칼라채널을 출력한다")
# Yellow = Green + Red
# Magenta = Red + Blue
# Cyan = Blue + Green
# 질문 1: 아래 문장이 의미하는 바를 설명하시오.
#           img = np.zeros(image.shape, dtype=np.uint8)
#           img[:,:,0] = image[:,:,0]
#           img[:,:,2] = 0
# 질문 2: 아래 방법 3)이 불가한 이유를 설명하시오. 이를 copy()를 활용하여 해결하시오.
# ========================================================================================================

# 입력 영상과 같은 크기의 모든 요소의 값이 0으로 초기화된 영상 어레이 img를 선언한다.
#img = np.zeros(image.shape, dtype='uint8')     # 방법 1) 이것도 됨.
img = np.zeros(image.shape, dtype=np.uint8)     # 방법 2) 이것도 됨.
#img = image; img[:,:,:]=0                      # 방법 3) 이것은 안되는 이유가 우엇인가?

printImgAtt('image')
printImgAtt('img')
img[:,:,0] = image[:,:,0]       # copy B channel
cv.imshow('B', img)
img[:,:,0] = 0                  # clear B channel

img[:,:,1] = image[:,:,1]       # copy G channel
cv.imshow('G', img)
img[:,:,1] = 0                  # clear G channel

img[:,:,2] = image[:,:,2]       # copy R channel
cv.imshow('R', img)
img[:,:,2] = 0                  # clear R channel

cv.imshow('BGR', image)

cv.waitKey()

cv.destroyAllWindows()     # This does not work in 2.7. Fine in 3.7
#exit(0)



#===============================================================================
# 질문 1: 아래 동작이 copy를 실행하는지 혹은 단지 포인터만 일치시키는 추정하고 그 근거를 제시하시오.
# img[:,:,0] = image[:,:,0]
# 이 질문은 취소합니다.. 답: 명백히 copy합니다.
#===============================================================================



