"""
개요
    영상 파일을 읽어들여 화면에 출력하고 저장한다.

동작
    1. 이미지를 읽어 영상을 화면에 출력한다.
    2. 영상 데이터를 저장한다.
    3. 저장한 영상을 다시 읽어들여 확인한다.

함수
    1. 영상 파일("abc.jpg") 읽어 영상 어레이(img)에 반환하기: img=imread("abc.jpg", 열기_모드)
    2. 영상 어레이(img)를 지정된 이름("win")의 타이틀에 출력하기: imshow("win", img)
    3. 영상 어레이(img)를 지정된 파일 이름("abc.jpg")으로 저장하기: imwrite("abc.jpg", img)
    4. 키입력을 무한 혹은 500[ms]동안 기다리기: waitKey()=waitKey(0) or waitKey(500)
    5. 타이틀 이름("abc")을 지정하여 창 닫기: destroyWindow("abc")
    6. 모든 창을 닫기 : destroyAllWindows()

질문
    1. JPEG 파일로 저장할 때 화질을 지정하여 저장하는 방법은?
    2. 영상 파일을 읽을 때 칼라 파일을 1채널의 모노 파일로 읽어 들이는 방법은?
    3. 1채널의 모노 영상을 3채널의 칼라 데이터로 읽어 들이는 방법은?

"""

import cv2 as cv

"""
# ----------------------------------------------------------------------------------------------------------------------
# 사전 실험 : 가장 단순한 예제
# 1) 영상 파일을 읽어, 2) 화면에 출력 출력하고, 3) 다른 이름(형식)의 파일로 저장하기
# ----------------------------------------------------------------------------------------------------------------------
a = cv.imread('./data/lenna.tif')         # 1) 영상읽기. 'data/lenna.tif'=영상의 폴더 및 이름. a에 영상 객체가 들어가 있음.
print(f'type(a)={type(a)}, a.shape={a.shape}, a.dtype={a.dtype}')
#print('type(a)={}, a.shape={}, a.dtype={}'.format(type(a), a.shape, a.dtype))
cv.imshow('test', a)                    # 2) 영상 보이기. test=창의 이름
cv.waitKey()
cv.imwrite('./data/tmp.jpg', a)                # 3) 영상 저장. tmp.jpg=저장된 영상
exit(0)
"""

# ----------------------------------------------------------------------------------------------------------------------
# 섹션 1 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
# ----------------------------------------------------------------------------------------------------------------------
Path = './data/'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = './data/'
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/@@DIP/Images/'
Name_no = 'RGBColors.JPG'
Name1= 'colorbar_chart.jpg'
Name2 = 'lenna.bmp'
Name3 = 'monarch.bmp'
FullName1 = Path + Name1
FullName2 = Path + Name2
FullName3 = Path + Name3
FullName_no = Path + Name_no


# ----------------------------------------------------------------------------------------------------------------------
# 섹션 2: numpy.ndarray 데이터의 상세 내용을 출력하는 함수
# 데이터 변수 객체를 문자열로 입력한다.
# 섹션 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
# ----------------------------------------------------------------------------------------------------------------------
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



# ----------------------------------------------------------------------------------------------------------------------
# 단계 1: 영상 파일의 영상 읽기. 다음 함수를 통해 지정된 영상을 읽어내어 영상 데이터를 numpy.ndarray 객체로 반환한다.
# https://docs.opencv.org/4.1.1/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
# retval = cv.imread(filename[, flags]	)
#   filename = 영상 파일의 이름. 거의 모든 파일 양식(bmp. tif, jpg, png 등)을 지원. path도 함께 지정가능.
#   flags = 읽어 내는 모드. 다음 3가지 중 하나.
#       IMREAD_COLOR = 1            default. 칼라영상을 row x column x channel의 3차원 ndarrary로 읽어 반환한다.
#                                   칼라 채널 배열 순서는 B, G, R 순이다.
#                                   모노 영상도 3채널(BGR) 영상으로 확장하여 읽는다. 이 경우 각 채널에는 같은 값이 들어 있다.
#       IMREAD_GRAYSCALE = 0        1채널 mono gray 영상으로 읽어 반환한다. 칼라 영상을 모노로 변환하여 연다. 1채널 영상이 됨.
#       IMREAD_UNCHANGED = -1       있는 그대로 열기.
#   retval = numpy.ndarray 타입의 영상 데이터 객체.
# ----------------------------------------------------------------------------------------------------------------------

flags = cv.IMREAD_COLOR                    # BGR 3채널로 읽는다. default.
image = cv.imread(FullName3, flags)         # OpenCV에서는 BGR 배열임

# assert condition, message  : condition이 false이면  message 출력하면서 AssertError 발생.
assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

imageM = cv.imread(FullName3, 0)      # IMREAD_GRAYSCALE = 0. Read in mono.

printImgAtt('image')
# image
#  type : <class 'numpy.ndarray'>
#  shape =  (512, 768, 3)
#  data type =  uint8
#  row =  512
#  column =  768
#  channel =  3

printImgAtt('imageM')
# imageM
#  type : <class 'numpy.ndarray'>
#  shape =  (512, 768)
#  data type =  uint8
#  row =  512
#  column =  768



# ----------------------------------------------------------------------------------------------------------------------
# 단계 2: 영상 데이터 화면에 출력하기. 아래 함수들은 cv.waitKey() 함수가 있어야 화면에 내용물을 출력한다.
# None = cv.imshow(winname, array)              # array 영상을 winname 창에 출력한다.
#   열려져 있는 winname 창이 없으면 생성한 후 영상을 출력한다.
#   winname = Name of window
#   array = Image to be shown
# None = cv.namedWindow(winname[, flags])       # winname 창을 생성하여 화면에 보인다. 아직 내용물(영상)은 안보임.
#   winname = Name of window
#
# ----------------------------------------------------------------------------------------------------------------------

winname_image ='image : ImReadMode=' + str(cv.IMREAD_COLOR)     # =1. default. BGR color. 3 channel.
cv.imshow(winname_image, image)
cv.waitKey()       # 이곳에서 키보드 입력을 기다린다.
cv.destroyWindow(winname_image)     # 지정한 이름의 창을 닫는다.

winname_imageM = 'imageM : ImReadMode=' + str(cv.IMREAD_GRAYSCALE)  # =0. mono gray. 1 channel.
cv.namedWindow(winname_imageM)
cv.waitKey(0)       # 이곳에서 키보드 입력을 기다린다.

cv.imshow(winname_imageM, imageM)
cv.waitKey(0)       # 이곳에서 키보드 입력을 기다린다.

cv.destroyWindow(winname_imageM)

# ----------------------------------------------------------------------------------------------------------------------
# 단계 3: 영상을 다른 이름과 형식으로 저장한다.
# jpg와 png 형식의 파일로 저장한다. => 파일 이름의 확장자로 지정 가능하다.
# 압축을 사용하는 파일 형식은 영상 품질로 압축률을 통제한다.
# ----------------------------------------------------------------------------------------------------------------------

fname = FullName3[0:-4]      # 파일 이름에서 확장자(.bmp, .jpg, .png 등)를 제거한다.

# 1) 모노 그레이 영상을 저장한다.
filename_mono = fname + '_mono'+'.jpg'
cv.imwrite(filename_mono, imageM)

# 2) 압축 품질을 지정하여 jpeg으로 저장한다.
quality =80              # quality : 1 to 100. The higher is the better.
#filename_jpg = fname + '_q='+str(quality)+'.jpg'              # 저장할 파일의 이름
filename_jpg = fname + '_q=%02d'%quality+'.jpg'              # 저장할 파일의 이름
cv.imwrite(filename_jpg, image, (cv.IMWRITE_JPEG_QUALITY, quality))       # mono 영상을 저장해 본다. quality is 95 default.
# 여러 개의 파라미터를 제어할 때는 아래와 같이 파라미터 이름과 값을 나열하면 된다. 이들 파라미터는 리스트 혹은  튜플로서 한대의 파라미터로 입력된다.
q_chroma = 1; q_luma = 10
filename_jpg2 = fname + '_qChro=%02d'%q_chroma + '_qLuma=%02d'%q_luma + '.jpg'              # 저장할 파일의 이름
cv.imwrite(filename_jpg2, image, (cv.IMWRITE_JPEG_CHROMA_QUALITY, q_chroma, cv.IMWRITE_JPEG_LUMA_QUALITY, q_luma))


# 3) 압축 품질을 지정하여 png로 저장한다.
quality =9              # png 파일의 품질. 0~9로 지정. 높은 값(9)이 압축이 심함. default=1
#filename_png = fname + '_q='+str(quality)+'.png'
filename_png = fname + '_' \
                       'q=%02d'%quality+'.png'
cv.imwrite(filename_png, image, (cv.IMWRITE_PNG_COMPRESSION, quality) )

# ----------------------------------------------------------------------------------------------------------------------
# 단계 4: 확인 차원에서 저장한 영상을 읽어 화면에 출력한다.
# ----------------------------------------------------------------------------------------------------------------------

image_mono = cv.imread(filename_mono)
cv.imshow('1) ' + filename_mono, image_mono)
cv.waitKey()
cv.destroyWindow('1)'+filename_mono)
printImgAtt('image_mono')
# image_mono
#  type : <class 'numpy.ndarray'>
#  shape =  (512, 768, 3)
#  data type =  uint8
#  row =  512
#  column =  768
#  channel =  3                             # 왜 3채널로 변했을까???

image_jpg = cv.imread(filename_jpg)
cv.imshow('2) ' + filename_jpg, image_jpg)
printImgAtt('image_jpg')
# image_jpg
#  type : <class 'numpy.ndarray'>
#  shape =  (512, 768, 3)
#  data type =  uint8
#  row =  512
#  column =  768
#  channel =  3


image_jpg2 = cv.imread(filename_jpg2)
cv.imshow('3) ' + filename_jpg2, image_jpg2)
printImgAtt('image_jpg2')
# image_jpg2
#  type : <class 'numpy.ndarray'>
#  shape =  (512, 768, 3)
#  data type =  uint8
#  row =  512
#  column =  768
#  channel =  3

image_png = cv.imread(filename_png)
cv.imshow('4) ' + filename_png, image_png)
printImgAtt('image_png')
# image_png
#  type : <class 'numpy.ndarray'>
#  shape =  (512, 768, 3)
#  data type =  uint8
#  row =  512
#  column =  768
#  channel =  3

cv.waitKey(0)


cv.destroyAllWindows()     # This does not work in 2.7. Fine in 3.7

exit(0)


#====================================================================================================================
# 미션 과제(1)
# 파일의 이름과 영상 품질을 키보드로 입력 받아 저장하는 프로그램을 작성하시오.
# 이때 파일 확장자는 jpg를 가정하며 이는 입력받지 않는다.
# 활용 예: lenna.tif를 입력받아 quality=20인 abc.jpg로 변환하여 저장하한다.
#   input file:lenna.tif
#   out file:abc
#   quality:20
#====================================================================================================================


#====================================================================================================================
# 미션 과제(2)
# 파일의 이름과 영상 품질을 키보드로 입력 받아 저장하는 프로그램을 작성하시오.
# 사용 예: python lenna.bmp out.jpg 20         # lenna.bmp 영상을 입력 받아 out.jpg로 저장.
#====================================================================================================================
