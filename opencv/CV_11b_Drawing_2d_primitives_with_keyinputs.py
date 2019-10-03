"""
아래 예제를 기반으로 수정함.
    1장- 06 Drawing 2d primitives_ markers, lines, ellipses, rectangles and text.py

    p, l, r, e, t 문자를 입력하면 활성화된 영상 화면에 해당 그리기 혹은 문자 출력을 수행한다.
    이때 사용되는 파라미터는 랜덤값에 의존하기 때문에 같은 동작이라도 반복하면 가능하다.
    이때 c는 화면을 지우는 용도로 사용하고 종료 할 때는 esc 키를 사용한다.
"""

import cv2
import cv2 as cv
import numpy as np, random

#===============================================================================
# 단계 0 :  영상이 존재하는 폴더와 파일 이름을 지정하기.
#===============================================================================
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
# 단계 1 : 영상 파일을 열기
# ========================================================================================================
# ImreadMode: 영상 데이터의 반환 모드를 결정
#   IMREAD_COLOR = 1            # default. 모노 영상도 3채널(RGB) 영상이 된다.
#   IMREAD_GRAYSCALE = 0        # 칼라 영상도 모노로 변환하여 연다. 1채널 영상이 됨.
#   IMREAD_UNCHANGED = -1       # 있는 그대로 열기.
image = cv.imread(FullName, -1)
assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.

image_to_show = np.copy(image)
w, h = image.shape[1], image.shape[0]

# ========================================================================================================
# 함수 정의: 전역변수 w, h의 범위에 있는 2개의 정수 값을 반환하는 함수.
# 영상(x, h)의 가로 x 세로 영역 안에 있는 랜덤 (x,y) 좌표로 활용예정
# ========================================================================================================
def rand_pt(mult=1.0):
    return (random.randrange(int(w*mult)),
            random.randrange(int(h*mult)))

# ========================================================================================================
# 메인루틴: 키보드 문자를 입력하여 해당 동작 수행하기
# p : circle 함수를 이용하여 10개의 파란 색 점(반지름 3)을 그린다.
# l : line 함수를 이용하여 초록 색 선을 1개 그린다.
# r : rectangle() 함수를 이용하여 붉은 색 사각형을 그린다.
# e : ellipse() 함수를 이용하여 남색 타원형을 그린다.
# ========================================================================================================
finish = False
while not finish:
    cv2.imshow("result", image_to_show)
    key = cv2.waitKey(0)
    if key == ord('p'):
        for pt in [rand_pt() for _ in range(10)]:
            cv2.circle(image_to_show, pt, 3, (255, 0, 0), -1)
    elif key == ord('l'):
        cv2.line(image_to_show, rand_pt(), rand_pt(), (0, 255, 0), 3)
    elif key == ord('r'):
        cv2.rectangle(image_to_show, rand_pt(), rand_pt(), (0, 0, 255), 3)
    elif key == ord('e'):
        #cv2.ellipse(image_to_show, rand_pt(), rand_pt(0.3), random.randrange(360), 0, 360, (255, 255, 0), 3)
        cv2.ellipse(image_to_show, rand_pt(), (100, 50), random.randrange(360), 0, 360, (255, 255, 0), 3)
    elif key == ord('t'):
        cv2.putText(image_to_show, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (random.randrange(255), random.randrange(255), random.randrange(255)), 3)
    elif key == ocrd('c'):
        image_to_show = np.copy(image)
    elif key == 27:
        finish = True
