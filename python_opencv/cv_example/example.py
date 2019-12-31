from cv2 import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


# show picture on frame
def show_pic(pos, title, aim):
    plt.subplot(1, 4, pos)
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    plt.imshow(aim)


# 读取灰度图
img = cv.imread("1.jpg", cv.IMREAD_GRAYSCALE)
show_pic(1, "gray", img)

# 灰度转换
gray = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
show_pic(2, "convert", gray)

# 二值化处理
ret, thresh = cv.threshold(gray, 170, 255, cv.THRESH_TRUNC)
show_pic(3, "threshold", thresh)

# 腐蚀操作
kernel = np.ones((30, 30), np.uint8)
res = cv.erode(thresh, kernel, iterations=5)
show_pic(4, "erode", res)

plt.savefig("out.png", dpi=300, bbox_inches='tight')
plt.show()
