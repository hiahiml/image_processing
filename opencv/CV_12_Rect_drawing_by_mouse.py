"""
1. 동작의 개요
    영상에 마우스 드래그 동작으로 화면에서 관심 영역을 선택한다.
    드래그하는 동안 선택된 사각형은 노란 색으로 표현된다.
    선택이 완료된 후에는 문자 c 혹은 r을 입력받는다. esc는 프로그램을 종료한다.
    c인 경우
        선택된 영역을 2배로 확대해서 화면에 출력한다.
        선택된 영역을 파일 crop.jpg에 저장한다.
    s인 경우
        선택한 영역의 크기로 영상을 줄여 출력한다. 일단 영역을 줄여 표현하면 복원되지 않는다.

2. 미션
    r을 입력하면 원본 영상의 크기로 복원하는 기능을 추가하시오.

3. 참조
    1장 08 Making your app interactive via handling user input from mouse.py를 개선하였다.
    위 소스의 마우스 드래그 동작을 더 이상 하지 않고 c만 누르면 계속 영상이 작아지는 문제를 해결하였다.
    - drawing_needed 변수가 True일 때만 선택된 영역의 크기 대로 영상의 크기를 조절한다.

"""
import cv2
import cv2 as cv
import numpy as np, random



# ========================================================================================================
# 단계 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
# ========================================================================================================
Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = 'd:/Work/StudyImages/Images/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'd:/work/@@DIP/Images/'
Name = 'RGBColors.JPG'
Name2= 'colorbar_chart.jpg'
Name = 'lenna.bmp'
Name = 'monarch.bmp'
FullName = Path + Name
FullName2 = Path + Name2

# ========================================================================================================
# 단계 1 : 영상 파일 열기
# ========================================================================================================
# ImreadMode: 영상 데이터의 반환 모드를 결정
#   IMREAD_COLOR = 1            # default. 모노 영상도 3채널(RGB) 영상이 된다.
#   IMREAD_GRAYSCALE = 0        # 칼라 영상도 모노로 변환하여 연다. 1채널 영상이 됨.
#   IMREAD_UNCHANGED = -1       # 있는 그대로 열기.
image = cv.imread(FullName, -1)
assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

# ========================================================================================================
# call back 함수 정의
# ========================================================================================================

def mouse_callback(event, x, y, flags, param):
    global image_to_show, s_x, s_y, e_x, e_y, mouse_pressed, drawing_needed

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x, y             # 선택 시작 좌표 기록
        #image_to_show = np.copy(image)     # 불 필요. 삭제함.

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동중이다...
        if mouse_pressed:               # 누른 상태에서...
            image_to_show = np.copy(image)      # 녹색 사각형을 지워야 함.
            cv2.rectangle(image_to_show, (s_x, s_y),
                          (x, y), (0, 255, 0), 1)       # 녹색 사각형으로 선택 영역 보이기

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        e_x, e_y = x, y             # 선택 종료 좌표 기록
        drawing_needed = True



# ========================================================================================================
# 단계 2 - 메인 루틴
# 마우스 드랙으로 화면에서 영역을 선택한다.
# 문자 c를 누르면 선택한 영역을 파일(crop.jpg)로 저장한다.
#   또한 영상을 2배로 확대하여 화면에 출력한다.
# 문자 s를 누르면 선택한 영역으로 영상을 줄여 출력한다.
# esc 키를 누르면 종료한다.
# ========================================================================================================

image_to_show = np.copy(image)

mouse_pressed = False

#s_ : start position, e_ : ending position
s_x = s_y = e_x = e_y = -1

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

modified = False
while True:
    cv2.imshow('image', image_to_show)
    k = cv2.waitKey(100)


    if k == ord('c') and drawing_needed == True:     # 마우스 드랙으로 크기를 바꾸지 않고 c만 계속 눌러도 사이즈를 줄이는 문제를 해결하였다.
        if s_y > e_y:           # y축상의 시작점과 끝점이 바뀌었으면 두 좌표를 바꾼다.
            s_y, e_y = e_y, s_y
        if s_x > e_x:           # x축상의 시작점과 끝점이 바뀌었으면 두 좌표를 바꾼다.
            s_x, e_x = e_x, s_x

        if e_y - s_y > 1 and e_x - s_x > 0:
            img_crop = image[s_y:e_y, s_x:e_x]
            img_crop2 = cv2.resize(img_crop, (img_crop.shape[1]*2, img_crop.shape[0]*2))
            cv2.imshow('crop', img_crop2)
            cv2.imwrite('crop.jpg', img_crop)
            drawing_needed = False                  # 사이즈 조절했으므로 더 이상 조절이 필요없다.



    if k == ord('s') and drawing_needed == True:     # 마우스 드랙으로 크기를 바꾸지 않고 c만 계속 눌러도 사이즈를 줄이는 문제를 해결하였다.
        if s_y > e_y:           # y축상의 시작점과 끝점이 바뀌었으면 두 좌표를 바꾼다.
            s_y, e_y = e_y, s_y
        if s_x > e_x:           # x축상의 시작점과 끝점이 바뀌었으면 두 좌표를 바꾼다.
            s_x, e_x = e_x, s_x

        if e_y - s_y > 1 and e_x - s_x > 0:
            image = image[s_y:e_y, s_x:e_x]
            image_to_show = np.copy(image)
            drawing_needed = False                  # 사이즈 조절했으므로 더 이상 조절이 필요없다.

    elif k == 27:
        break

cv2.destroyAllWindows()




