"""
작업의 내용: cv로 영상을 읽어 plt함수로 출력한다.
- 이 작업의 문제점: 1) cv로 읽은 영상데이터는 BGR 순서로 칼라 평면이 구성되어 있는데
                  plt는 영상 평면이 RGB로 배열된 것을 전제로 한다.
                  2) plt.show() 함수가 없으면 화면의 내용을 볼 수 없다.
- 점검 포인트
    1) BGR 배열을 RGB 배열로 바꾼다.
    2) figure()로 새로운 창을 연다.
    3) x, y축의 라벨을 삭제할 수도 있다.
    4) Non-interactive mode이다; 종료할 때는 각각의 창을 모두 닫아야 한다.
"""

import numpy as np
import cv2 as cv
# 만약 matplotlib 모듈이 없다면 윈도 컴맨드 창에서 "pip install matplotlib" 명령을 수행한다. 
from matplotlib import pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------
# 단계 1 :  영상이 존재하는 폴더와 파일 이름을 지정하고 영상 파일 읽기
# 다음 사례를 활용하여 영상 파일이 있는 폴더를 적절히 지정하시오.
# ----------------------------------------------------------------------------------------------------------------------

#Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
Path = 'd:/work/@@DIP/LectureMaterials/Images/'
Name = 'lenna.bmp'
#Name = 'monarch.bmp'
FullName = Path + Name

img = cv.imread(FullName)
# assert condition, message  : condition이 false이면  message 출력하면서 AssertError 발생.
assert img is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.


# ----------------------------------------------------------------------------------------------------------------------
# 단계 2 :  읽어 들인 영상을 matplotlib를 이용에 화면에 출력하기
# OpenCV로 읽어들인 영상을 matplotlib의 pyplot.imshow함수로 화면에 출력한다.
# plt.imshow() 함수에서 화면에 출력되는 것은 아니다. 실제로는 plt.show()에서 화면에 출력된 것이 보임.
# ----------------------------------------------------------------------------------------------------------------------

# 1) BGR 순설로 배열된 영상을 matplotlib로 화면에 출력해 본다.
# matplotlib는 RGB 배열을 전제로 하기 때문에 올바른 색상이 출력되지는 않는다.
plt.imshow(img)         # 영상의 3채널 평면은 BGR 순으로 배열되어 있다.
plt.title('BGR data from OpenCV')   # 지정된 sub 창에 그림 제목을 출력한다.

# 2) OpenCV 함수를 이용해 BGR 배열을 RGB 배열로 바꾸어 화면에 출력한다.
b, g, r = cv.split(img)   # img파일을 b,g,r로 분리
img2 = cv.merge([r,g,b]) # b, r을 바꿔서 Merge

# 새로운 창을 하나 더 만들어서 재 배열된 영상을 출력한다.
plt.figure()        # plt.figure(num='BGR to RGB')
plt.title('RGB data re-arranged')   # 지정된 sub 창에 그림 제목을 출력한다.
plt.imshow(img2)
plt.xticks([]), plt.yticks([])      # x축, y축에 label을 출력하지 않는다.

# In non-interactive mode: plt.ioff()  <- 현재 이 모드로 설정되어 있음.
#   show() display all figures and block until the figures have been closed;
# In interactive mode: plt.ion()
#   show() displays the figures but does not block.
#   show() has no effect unless figures were created
#   prior to a change from non-interactive to interactive mode (not recommended).
plt.show()      # 이 부분이 누락되면 출력된 내용을 볼 수 없다.
# 종료할 때는 각각의 창을 모두 닫아야 한다.

