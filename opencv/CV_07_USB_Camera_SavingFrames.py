"""
1. 개요
    USB 캠카메라의 영상을 정해진 시간(run_time)만큼 촬영하여 이를 파일(CamVid.avi)로 저장한다.
    과정 중 해상도와 FPS(Frame Per Second)를 바꾸고 제대로 반영되었는지 확인한다.
    1) 사용한 USB CAM : oCam - 5MP USB 3.0 Color Camera
        https://github.com/withrobot/oCam/tree/master/Products/oCam-5CRO-U-M
    2) 과거 사용했던 USB CAM " 라이프캠 HD-3000. USB 2.0
        https://www.microsoft.com/accessories/ko-kr/products/webcams/lifecam-hd-3000/t3h-00014
2. 동작
    단계 1: 비디오 객체(읽기용)를 생성한다.
    단계 2: 읽을 비디오 카메라(비디오 객체)의 속성을 출력한다.
    단계 3: fps를 변경하고 설정한 대로 변경되었는지 확인한다.
    단계 4: 카메라의 해상도를 다시 설정하고 설정한 대로 변경되었는지 확인한다.
    단계 5: 비디오 객체(쓰기용)을 생성한다.
    단계 6: 메인 루틴 - 카메라에서 읽어서 비디오 파일에 저장한다.

3. 사용된 함수
    cv.VideoCapture(): 비디오 객체(읽기용)를 생성한다.
    cv.videoCapture.read(): 한 프레임의 영상을 반환한다.
    cv.VideoCapture.get(): 비디오 카메라(비디오 객체)의 속성을 출력한다.
    cv.VideoCapture.set(): 비디오 카메라(비디오 객체)의 속성을 지정한다.
    cv.VideoWriter_fourcc(): 쓰기 용의 비디오 영상 코덱을 지정한다.
    cv.VideoWriter(): 쓰기용의 비디오 객체를 생성한다.
    cv.VideoWriter.write(): 쓰기용의 비디오 객체에 쓰기 동작을 수행한다.

4. 미션
    하단부의 미션 프로그램을 작성하시오.


"""


import cv2

# ========================================================================================================
# 단계 0: 비디오 객체(읽기용)를 생성한다.
# 장치 설정에 따라 카메라 번호를 바꾸어야할 때도 있다.
# ========================================================================================================
cameraCapture = cv2.VideoCapture(0)


# ========================================================================================================
# 단계 1: 읽을 비디오 카메라(비디오 객체)의 속성을 출력한다.
# ========================================================================================================
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('\n1. Default Setting:')
print('resolution : WIDTH*HEIGHT=', size)

fps_cam = cameraCapture.get(cv2.CAP_PROP_FPS)
print('fps=', fps_cam)



# ========================================================================================================
# 단계 2: 카메라의 해상도를 다시 설정하고 설정한 대로 변경되었는지 확인한다.
# 저급 카메라는 고해상도 설정에 실패한다.
# ========================================================================================================
#N_width = 1280; N_height = 720         # 저급 카메라는 안됨.
#N_width = 1920; N_height = 1080         # OK. @30, 15, 7.5 fps for oCam
#N_width = 1920; N_height = 1080         # OK. @30, 15, 7.5 fps for oCam
N_width = 1280; N_height = 720          # @60, 30, 15 fps for oCam
N_width = 320; N_height = 240           # 대다수 작동.
cameraCapture.set(cv2.CAP_PROP_FRAME_WIDTH, N_width)
cameraCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, N_height)
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('\n2. Resolution Change:')
print('resolution : WIDTH*HEIGHT=', size)
#print('current fps=', fps_cam)



# ========================================================================================================
# 단계 3: fps를 변경하고 설정한 대로 변경되었는지 확인한다.
# 실험에 의하면 설정이 바꾸지 않는 경우가 많음.
# 저장할 때 FPS를 바꾸면 되기 때문에 심각한 문제는 아니라고 판단됨.
# ========================================================================================================
print('\n3. FPS Change:')
fps = 30         # 희망하는 FPS(Frame Per Second)
print('setting fps =', fps)
cameraCapture.set(cv2.CAP_PROP_FPS, fps)   # MS Camera HD-3000 설정 실패. 설정이 되는 것을 본 적이 없음.
fps = cameraCapture.get(cv2.CAP_PROP_FPS)
print('fps after change=', fps)            # 따라서 설정한대로 읽히지 않을 수도 있음.


# ========================================================================================================
# 단계 4: 비디오 객체(쓰기용)을 생성한다.
# ========================================================================================================
print('\n4. Create a video object...')
#fps = 60         # 카메라의 fps보다 파일의 fps가 낮으면 time lapse 동영상이 만들어질 수 있다.
videoWriter = cv2.VideoWriter(
#    'CamVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
    'CamVid.avi', cv2.VideoWriter_fourcc('F', 'M', 'P', '4'), fps, size)


# ========================================================================================================
# 단계 5: 메인 루틴 - 카메라에서 읽어서 비디오 파일에 저장한다.
# ========================================================================================================
print('\n5. Writing into file...', end='')
run_time = 4;       # 녹화시간[초]
numFramesRemaining = run_time * fps             # 촬영할 프레임의 갯수

success = True
while success and numFramesRemaining > 0:
    success, frame = cameraCapture.read()
    cv2.imshow('CAM', frame)
    videoWriter.write(frame)
    cv2.waitKey(1)
    # fps에 따라 촬영 지연시간을 삽입. 저장시간이 추가되기 때문에 정확하지 않을 수 있음.
    #cv2.waitKey(int(1000/fps))
    numFramesRemaining -= 1
cameraCapture.release()
print('END')


# ========================================================================================================
# 미션 : 320x240의 영상을 촬영하여 그 영상과 그 영상의 모노의 영상을 가로로 이어 붙이고
# 이를 파일로 저장하시오.
# ========================================================================================================
