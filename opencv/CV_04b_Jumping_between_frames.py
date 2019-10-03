"""
1. 개요
    입력 영상 파일의 특정 프레임(0, 1, 중간)의 정지 영상을 화면에 출력한다.

2. 함수
    cv.VideoCapture.get(): 읽을 비디오 파일의 속성을 출력한다.
    cv.VideoCapture.set(): 비디오 파일의 속성을 지정한다.

"""

import cv2

# 단계 1: 비디오 파일을 읽고 총 프레임수를 알아낸다.
capture = cv2.VideoCapture('data/the_return_of_the_king.avi')
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame count:', frame_count)

# 단계 2: 현재의 프레임 번호를 알아낸다. 맨 처음은 0을 가리킨다.
print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame 0', frame)

# 단계 3: 현재의 프레임 번호를 알아낸다. 한번 읽었기 때문에 1을 가리킨다.
print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame 1', frame)

# 단계 4: 프레임 번호를 지정하여 읽어 낸다. 중간 지점을 읽기로 한다.
mid = int(frame_count/2)
capture.set(cv2.CAP_PROP_POS_FRAMES, mid)
print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame #' + str(mid), frame)

cv2.waitKey()
cv2.destroyAllWindows()