"""
개요
    OpenCV에서 제공하는 다양한 2d primitive의 사용법을 제시한다.
    본 프로그램은 모든 실험 내용이 한 화면에 한꺼번에 실행된다.
    랜덤함수를 사용하여 출력 결과가 수행할 때마다 달라질 수 있다.

2. 주요 함수에 대한 소개 - Drawing Functions
    https://docs.opencv.org/4.0.1/d6/d6e/group__imgproc__draw.html#ga7078a9fae8c7e7d13d24dac2520ae4a2
    OpenCV에서 제공하는 다양한 도형 그리기 함수를 소개한다.

3. 참고 사항 - 아래 예제를 다시 씀.
    1장- 06 Drawing 2d primitives_ markers, lines, ellipses, rectangles and text.py

"""

#import cv2
#import cv2 as cv           # 위와 같이 나누어서 import 할 수 있음.
import numpy as np, random, cv2, cv2 as cv      # 모든 모듈을 1줄로 임포트 가능.

#import numpy as np  #, random
#import random

#---------------------------------------------------------------------------------------------------------------
# 섹션 0:  영상이 존재하는 폴더와 파일 이름을 지정하기.
#---------------------------------------------------------------------------------------------------------------
Path = 'd:\Work\StudyImages\Images\\'       # \\ 오류 발생 방지. \만 쓰면 오류.
Path = 'd:/Work/StudyImages/Images/'       # \\ 오류 발생 방지. \만 쓰면 오류.
#Path = '../../Images/'               # 현재 상위 폴더의 상위 폴더 아래에 있는 Images 폴더.
#Path = 'data/'
Name = 'RGBColors.JPG'
Name= 'colorbar_chart.jpg'
Name = 'lenna.bmp'
Name = 'monarch.bmp'
FullName = Path + Name

#---------------------------------------------------------------------------------------------------------------
# 섹션 1: 영상 파일 열기
#---------------------------------------------------------------------------------------------------------------
# ImreadMode: 영상 데이터의 반환 모드를 결정
#   IMREAD_COLOR = 1            # default. 모노 영상도 3채널(RGB) 영상이 된다.
#   IMREAD_GRAYSCALE = 0        # 칼라 영상도 모노로 변환하여 연다. 1채널 영상이 됨.
#   IMREAD_UNCHANGED = -1       # 있는 그대로 열기.
image = cv2.imread(FullName, -1)
assert image is not None, 'No image file....!'  # 입력 영상을 제대로 읽어오지 못하여 NULL을 반환.
w, h = image.shape[1], image.shape[0]
print('image.shape=', image.shape)

#---------------------------------------------------------------------------------------------------------------
# 섹션 2: 전역변수 w, h의 범위에 있는 2개의 정수 값을 반환하는 함수.
# 영상(x, h)의 가로 x 세로 영역 안에 있는 랜덤 (x,y) 좌표로 활용예정
#---------------------------------------------------------------------------------------------------------------

# import random
# random.randrange(5)       # 0~4까지의 임의의 정수를 반환.
# random.randrange(1, 7)    # 1~6까지의 임의의 정수를 반환.
# random()                  # 0부터 1 사이의 임의의 float

def rand_pt(mult=1.0):
    return (random.randrange(int(w*mult)),
            random.randrange(int(h*mult)))


#---------------------------------------------------------------------------------------------------------------
# 실습 1: circle 그리기
# https://docs.opencv.org/4.1.1/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670
# void cv::circle (InputOutputArray 	img,
#   Point center,           // Center of the circle.
#   int radius,             // Radius of the circle.
#   const Scalar & color,   // Circle color.
#   int thickness = 1,      // Thickness of the circle outline, if positive.
#                           // Negative values, like FILLED, mean that a filled circle is to be drawn.
#   int lineType = LINE_8,  // Type of the circle boundary. See LineTypes
#                           // LINE_4: 4-connected line, LINE_8: 8-connected line
#   int shift = 0)          // Number of fractional bits in the coordinates of the center and in the radius value.
#---------------------------------------------------------------------------------------------------------------

center = rand_pt(); radius=180; color = (255, 0, 0)     # Blue, thickness=1
print(f'1a: center={center}, radius={radius}, color={color}')

cv2.circle(image,               # InputOutputArray
           center,           # Point	center
           radius,                  # int 	radius
           color)         # const Scalar & 	color

center = rand_pt(); radius=10; color = (0, 0, 255)      # Red. filled.
print(f'1b: center={center}, radius={radius}, color={color}')
cv2.circle(image, center, radius, color,
           cv2.FILLED)          # =-1. Negative values, like FILLED, mean that a filled circle is to be drawn.

center = rand_pt(); radius=40; color = (0, 255, 0); thickness = 2
print(f'1c: center={center}, radius={radius}, color={color}, thickness={thickness}')
cv2.circle(image, center, radius, color, thickness)

center = rand_pt(); radius=40; color = (0, 0, 255); thickness = 3
print(f'1d: center={center}, radius={radius}, color={color}, thickness={thickness}')
cv2.circle(image, center, radius, color, thickness,
           cv2.LINE_AA)     # antialiased line.


#---------------------------------------------------------------------------------------------------------------
# 실습 2: 선 그리기
# void cv::line	( InputOutputArray 	img,
#   Point pt1,              // First point of the line segment.
#   Point pt2,              // Second point of the line segment.
#   const Scalar & 	color,  // Line color.
#   int thickness = 1,      // Line thickness.
#   int lineType = LINE_8,
#   int shift = 0)
#---------------------------------------------------------------------------------------------------------------

cv2.line(image, rand_pt(), rand_pt(), (0, 255, 0), 3)           # Green
cv2.line(image, rand_pt(), rand_pt(), (255, 255, 255), 4)       # white
cv2.line(image, rand_pt(), rand_pt(), (170, 255, 170), 4, cv2.LINE_AA)      #  antialiased line.


#---------------------------------------------------------------------------------------------------------------
# 실습 3: 화살표 선 그리기
# void cv::arrowedLine	(	InputOutputArray 	img,
#   Point pt1,              // First point of the line segment.
#   Point pt2,              // Second point of the line segment.
#   const Scalar & 	color,  // Line color.
#   int thickness = 1,      // Line thickness.
#   int lineType = LINE_8,
#   int shift = 0,
#   double 	tipLength = 0.1)    // The length of the arrow tip in relation to the arrow length

cv2.arrowedLine(image, rand_pt(), rand_pt(), (0, 0, 255), 3, cv2.LINE_AA)


#---------------------------------------------------------------------------------------------------------------
# 실습 4: 사각형 그리기
# void cv::rectangle	(	InputOutputArray 	img,
#   Point 	pt1,            // Vertex of the rectangle.
#   Point 	pt2,            // Vertex of the rectangle opposite to pt1 .
#   const Scalar & 	color,  // Rectangle color or brightness (grayscale image).
#   int thickness = 1,      // Thickness of the circle outline, if positive.
#                           // Negative values, like FILLED, mean that a filled circle is to be drawn.
#   int lineType = LINE_8,  // Type of the circle boundary. See LineTypes
#                           // LINE_4: 4-connected line, LINE_8: 8-connected line
#   int shift = 0)          // Number of fractional bits in the coordinates of the center and in the radius value.
cv2.rectangle(image, rand_pt(), rand_pt(), (255, 255, 0), 3)        # cyan


#---------------------------------------------------------------------------------------------------------------
# 실습 5: 타원형 그리기
# https://docs.opencv.org/4.1.1/d6/d6e/group__imgproc__draw.html#ga28b2267d35786f5f890ca167236cbc69
# void cv::ellipse(	InputOutputArray 	img,
#   Point center,               // Center of the ellipse.
#   Size 	axes,               // Half of the size of the ellipse main axes. (width, height)
#   double 	angle,              // Ellipse rotation angle in degrees.
#   double 	startAngle,         // Starting angle of the elliptic arc in degrees.
#   double 	endAngle,           // Ending angle of the elliptic arc in degrees.
#   const Scalar & 	color,      // Ellipse color.
#   int thickness = 1,      // Thickness of the circle outline, if positive.
#                           // Negative values, like FILLED, mean that a filled circle is to be drawn.
#   int lineType = LINE_8,  // Type of the circle boundary. See LineTypes
#                           // LINE_4: 4-connected line, LINE_8: 8-connected line
#   int shift = 0)          // Number of fractional bits in the coordinates of the center and in the radius value.
#cv2.ellipse(image, rand_pt(), rand_pt(0.3), random.randrange(360), 0, 360, (255, 255, 255), 3)
cv2.ellipse(image, rand_pt(), (100, 50), random.randrange(360), 0, 360, (255, 255, 255), 3)


#---------------------------------------------------------------------------------------------------------------
# 실습 6: 글씨 넣기
# void cv::putText(	InputOutputArray 	img,
#   const String & 	text,               // Text string to be drawn.
#   Point org,                          // Bottom-left corner of the text string in the image.
#   int fontFace,                       // Font type, see HersheyFonts.
#   double fontScale,                   // Font scale factor that is multiplied by the font-specific base size.
#   Scalar color,                       // Text color.
#   int thickness = 1,                  // Thickness of the lines used to draw a text.
#   int lineType = LINE_8,              // Line type. See LineTypes
#   bool bottomLeftOrigin = false)      // When true, the image data origin is at the bottom-left corner.
#                                           Otherwise, it is at the top-left corner.
cv2.putText(image, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)


cv2.imshow("result", image)
key = cv2.waitKey(0)