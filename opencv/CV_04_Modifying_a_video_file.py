"""
1. 개요
    지정한 비디오 파일의 속성을 변경한다. 입력 해당 영상이 천천히 혹은 빠르게 재생되도록 fps를 바꾸어 저장한다.
    이 프로그램을 수행하기 위해서는 data 폴더 밑에 지정된 동영상이 있어야 한다.
    이 프로그램을 수행하면 test.avi 이름의 동영상이 현재의 폴더에 생성된다.

2. 동작
    단계 1 : 읽기용의 비디오 객체를 생성한다.
    단계 2 : 읽을 비디오 파일의 속성을 출력한다.
    단계 3 : 저장할 비디오 파일 코덱을 지정한다.
    단계 4 : 쓰기용의 비디오 객체를 생성한다.
    단계 5 : 첫 번째 프레임을 읽어보고 영상의 속성을 출력한다.
    단계 6 : 직전의 읽기 동작이 성공하였다면 화면에 영상 데이터를 출력하면서 저장한다.

3. 함수
    cv.VideoCapture(): 비디오 객체(읽기용)를 생성한다.
    cv.VideoCapture.get(): 읽을 비디오 파일(비디오 객체)의 속성을 출력한다.
    cv.VideoWriter_fourcc(): 쓰기 용의 비디오 영상 코덱을 지정한다.
    cv.VideoWriter(): 쓰기용의 비디오 객체를 생성한다.
    videoCapture.read(): 한 프레임의 영상을 반환한다.

4. 질문
    단계 6에서 저장할 영상의 데이터형은 무엇이라고 판단되는가?

5. 미션
    1. fourcc('X','2','6','4') 코덱을 사용하여 저장하시오.
    2. 영상의 좌측 반쪽을 역상으로 만들어 저장하시오.
    3. 영상을 2.5배 밝게 만들어 저장하기 위해 필요한 수정사항을 제시하시오.

"""

import cv2 as cv

# numpy.ndarray 데이터의 상세 내용을 출력하는 함수
# 데이터 변수를 문자열로 입력한다.
def printImgAtt (string):
    print("\n" + string)
    data = eval(string)
    print(' type :', type(data))           # imge type =  <class 'numpy.ndarray'>
    print(' shape = ', data.shape)      # 영상 어레이의 크기 알아내기. image shape =  (512, 768, 3). (행, 열, 채널)
    print(' data type = ', data.dtype) # 어레이 요소의 데이터 타입 알아내기. uint8 = unsigned 8비트.
    if len(data.shape) >= 2:
        print(' row = ', data.shape[0])  # shape는 tuple이다. 원소는 []로 지정. 리스트도 []로 지정한다.
        print(' column = ', data.shape[1])  # 열의 수.
        if len(data.shape) == 3:
            print(' channel = ', data.shape[2])  # 채널의 수. 칼라 영상이면 3. 모도 영상이면 1.


#----------  영상이 존재하는 폴더와 파일 이름을 지정하기
#Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = 'd:/StudyImages/Images/'        # 사용가능
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
Path = 'd:/Work/StudyImages/Images/'
Path = 'data/'
Name = 'the_return_of_the_king.avi'
#Name = 'Bullet Time and The Matrix.mp4'

FullName = Path + Name
#FullName = 'test.avi'           # 테스트용
FullName = 'CamVid.avi'

# ========================================================================================================
# 단계 1 : 읽기용의 비디오 객체를 생성한다. 파일 혹은 캠카메라에서 읽을 수 있다.
#         비디오 카메라는 파일명 대신 카메라 번호를 지정하면 된다. 예) cv.VideoCapture(0)
#   Class for video capturing from video files, image sequences or cameras.
#       https://docs.opencv.org/4.1.1/d8/dfe/classcv_1_1VideoCapture.html
# ========================================================================================================
videoCapture = cv.VideoCapture(FullName)


# ========================================================================================================
# 단계 2 : 읽을 비디오 영상 파일의 속성을 출력한다.
# 	retval	=	cv.VideoCapture.get(propId)
#       propId = VideoCapture generic properties identifier.
#       https://docs.opencv.org/4.1.1/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
# ========================================================================================================
fps = videoCapture.get(cv.CAP_PROP_FPS)
print ('fps=', fps)

size = (int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
    int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
print ('size=', size)

fourcc = videoCapture.get(cv.CAP_PROP_FOURCC)
print ('CAP_PROP_FOURCC =', int(fourcc))     # 4-character code of codec. 압축 코텍 4글자
# see VideoWriter::fourcc
#     https://docs.opencv.org/4.0.0/dd/d9e/classcv_1_1VideoWriter.html#afec93f94dc6c0b3e28f4dd153bc5a7f0

number_of_total_frames = videoCapture.get(cv.CAP_PROP_FRAME_COUNT)
print ('CAP_PROP_FRAME_COUNT=', int(number_of_total_frames))


# ========================================================================================================
# 단계 3 : 저장할 비디오 영상 코덱을 지정한다.
# FourCC(Four Character Code)
#   그대로 "4글자 코드"라는 뜻이며, 4 바이트로 된 문자열은 데이터 형식을 구분하는 고유 글자가 된다.
#   FourCC는 주로 AVI 파일의 영상 코덱을 구분할 때 사용된다
# 참조 URL:   http://www.fourcc.org/
# ========================================================================================================
#CODEC = -1      # 윈도에서 지원하는 코덱의 다이얼박스 목록에서 선택한다. Intel YUV=70MB. MS RLE 80=실패.
#CODEC = cv.VideoWriter_fourcc('D','I','V','X')
#CODEC = cv.VideoWriter_fourcc('I','4','2','0')         # 파일 용량 큼
CODEC = cv.VideoWriter_fourcc('F','M','P','4')          # 파일 용량 적음

# 아래 코덱은 저장할 때 다음 오류를 유발하므로 미리 다운 받아야 함.
#Failed to load OpenH264 library: openh264-1.7.0-win64.dll
# https://github.com/cisco/openh264/releases
# 주의사항: 오류 메시지에서 제시된 버전(1.7.0)을 다운 받아야함. 이 버전은 파이썬 설치 버전에 따라 달라질 수 있음.
# dll 파일을 본 프로그램의 폴더에 복사해 넣거나 PATH=C:\Python\Scripts\;C:\Python\ 등으로 제시된 path 폴더 중의 하나에 넣어도 됨.
#CODEC = cv.VideoWriter_fourcc('X','2','6','4')

print('CODEC=', CODEC); print('type(CODEC)=', type(CODEC))


# ========================================================================================================
# 단계 4 : 쓰기용의 비디오 객체를 생성한다.
# ========================================================================================================
new_fps = int(fps/3)        # 3배 저속으로 출력하도록 fps를 낮춘다.
videoWriter = cv.VideoWriter(
    #'backup.avi', CODEC, fps, size)
    'test.avi', CODEC, new_fps, size)
#exit(0)



# ========================================================================================================
# 단계 5 : 첫 번째 프레임을 읽어보고 영상의 속성을 출력한다.
# ========================================================================================================
success, frame = videoCapture.read()
printImgAtt('frame')



# ========================================================================================================
# 단계 6 : 직전의 읽기 동작이 성공하였다면 화면에 영상 데이터를 출력하면서 저장한다.
# 질문 : 2.5배 밝게하여 저장하고자 하는 코드가 오류가 발생하는 이유(오류 1, 2)를 설명하시오.
# 미션 : 영상을 2.5배 밝게 만들어 저장하는 코드를 작성하시오.
# ========================================================================================================

scale =1            # play time will be decreased by this amount.
count = 0
while success: # Loop until there are no more frames.
    count += 1
    cv.imshow(Name, frame)
    videoWriter.write(frame)               # 정상 작동
    #videoWriter.write(2.5 * frame)                  # 오류 1- 수행 오류
    #videoWriter.write((2.5 * frame).astype(dtype='uint8'))  # 오류 2- 영상 잡음
    success, frame = videoCapture.read()
    cv.waitKey(int(1000/(fps*scale)))
    print("\rCount = ", count, end=' ')
print('Total Count = ', count)

