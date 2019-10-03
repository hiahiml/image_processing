"""
1. 개요
    가우시안 함수를 만들고 이를 그려 보인다.
        실습 1) 1차원 가우시안 함수를 2차원 평면에 그린다.
        실습 2) 2차원 가우시안 함수를 3차원 평면에 그린다.

2. 목표 - 숙지할 사항
    실습 1에서는 pyplot을 이용한 함수의 drawing 기술에 대해 유념해야 한다.

3. 미션 - 소스 하단 부에 기술하였음.
    1) kx1 크기의 1차원 가우시간 커널을 반환하는 함수를 설계하시오
    2) kxk 크기의 2차원 가우시간 커널을 설계하시오.

"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

"""
# ======================================================================================================================
# 실습 1: Draw 1D Gaussian functions on 2D space
# 1차원 가우시안 함수의 데이터를 반환하는 함수를 정의하고
# 이를 이용하여 다양한 시그마(표준편차, sigma)에 대한 함수 곡선을 색상을 바꾸어가며 그린다.
# ======================================================================================================================

r = np.arange(-31,31,0.1,np.float32)

def gaussian(r, sigma): # 가우시안 함수를 정의함.
    return np.exp(-r**2/(2*sigma**2))

# curve_list =[ (시그마 값, 색상_스트링, 레전드_스트링), (...) , ...]
curve_list = [(1, 'b', r'$\sigma=1$'), (3, 'r', r'$\sigma=3$'), (5, 'c', r'$\sigma=5$'), (7, 'g', r'$\sigma=7$'), (9, 'm', r'$\sigma=9$')]
curve_list = [(1, 'b', r'$\sigma=1$'), (3, 'r', r'$\sigma$=3'), (5, 'c', r'$\sigma$=5'), (7, 'g', r'$\sigma$=7'), (9, 'm', r'$\sigma$=9')]
# 주의!!! 칼라 값을 아래와 같이 숫자로 지정하면 legend가 2배의 개수로  나타남.  이유 불명!!
#curve_list = [(1, 1, r'$\sigma=1$'), (3, 2, r'$\sigma=3$'), (5, 3, r'$\sigma=5$'), (7, 4, r'$\sigma=7$'), (9, 5, r'$\sigma=9$')]
for sigma, color, lbl in curve_list:
    plt.plot(r, gaussian(r, sigma), color, label=lbl)

#plt.ylim(top=1, bottom=0)       # 주의!!! 칼라 값을 숫자로 지정하면 y값의 범위가 늘어남. 이유 불명!!
plt.legend()
plt.grid(True)
plt.title('Gaussian functions with various sigma')
plt.show()
exit(0)
"""

# ======================================================================================================================
# 실습 2: Draw 2D Gaussian functions on 3D space
# 2차원 가우시안 함수의 데이터를 반환하는 함수를 정의하고
# 이를 이용하여 다양한 시그마=2인 2차원 가우시안 함수를 3D 평면에 도시하시오. 높이가 크기가 됨.
# 2차원 Gaussian 함수의 3D 표현
# ======================================================================================================================

from mpl_toolkits.mplot3d import Axes3D
X = np.arange(-6, 6, 0.25)
Y = np.arange(-6, 6, 0.25)
XX, YY = np.meshgrid(X, Y)

def gaussian2D(x,y, sigma):
    return(np.exp(-(x**2 + y**2)/(2*sigma**2)))

#sigma =3; ZZ = gaussian2D(XX,YY, sigma)
sigma =2; ZZ = gaussian2D(XX,YY, sigma)

fig = plt.figure(num='2D Gaussian function in 3D space')
ax = Axes3D(fig)
#ax.set_title("Gaussian: sigma=" + str(sigma))
ax.set_title("Gaussian: $\sigma$=" + str(sigma))
ax.plot_surface(XX, YY, ZZ, rstride=1, cstride=1, cmap='jet')
plt.show()


# 미션 1 --------------------------------------------------------------------------
# 위 소스를 참조로 하여 kx1 크기의 1차원 가우시간 커널을 반환하는 함수를 설계하시오
#       - 즉, getGaussianKernel() 함수를 설계하시오.
# 이를 기반으로 sepFilter2D() 함수를 사용하여 블러링을 행하시오.
# --------------------------------------------------------------------------------



# 미션 2 --------------------------------------------------------------------------
# 위 소스를 참조로 하여 kxk 크기의 2차원 가우시간 커널을 설계하시오.
# 위 소스를 참조로 하여 kxk 크기의 2차원 가우시간 커널의 3D 그래프를 출력하시오.
# kxk 2차원 커널을 이용하여 filter2D() 함수를 이용하여 영상의 블러링을 시행하시오.
# --------------------------------------------------------------------------------
