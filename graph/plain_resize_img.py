import numpy as np 
import cv2 

src = cv2.imread('E:/dog.jpg')
src_h, src_w, _ = src.shape 

ratio_h = 2.0
ratio_w = 2.0 

dst = np.zeros((int(src_h * ratio_h), int(src_w * ratio_w), 3), dtype=np.uint8)
dst_h, dst_w, _ = dst.shape

print(src_h, src_w)
print(dst_h, dst_w)

scale_x = src_w / dst_w
scale_y = src_h / dst_h  


for dst_y in range(dst_h): 
    for dst_x in range(dst_w):
        # 目标在源上的坐标
        src_x = (dst_x + 0.5) * scale_x - 0.5
        src_y = (dst_y + 0.5) * scale_y - 0.5
        # 计算在源图上四个近邻点的位置
        src_x_0 = int(np.floor(src_x))
        src_y_0 = int(np.floor(src_y))
        src_x_1 = min(src_x_0 + 1, src_w - 1)
        src_y_1 = min(src_y_0 + 1, src_h - 1)

        #print(src_x_0, src_y_0, src_x_1, src_y_1)

        # 双线性插值
        value0 = (src_x_1 - src_x) * src[src_y_0, src_x_0, :] + (src_x - src_x_0) * src[src_y_0, src_x_1, :]
        value1 = (src_x_1 - src_x) * src[src_y_1, src_x_0, :] + (src_x - src_x_0) * src[src_y_1, src_x_1, :]

        tmp = (src_y_1 - src_y) * value0 + (src_y - src_y_0) * value1
        tmp = np.array(tmp, dtype=np.uint8)

        dst[dst_y, dst_x, :] = tmp 

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)#
cv2.imshow('dst', dst)

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.imshow('src', src)

cv2.waitKey(0)
cv2.destroyAllWindows()


