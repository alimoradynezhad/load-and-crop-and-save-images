import os
import matplotlib
import cv2
import matplotlib.pyplot as plt

dir = os.listdir(r"C:\Users\moradi\Desktop\New folder (2)")
print(dir)
os.mkdir(r'C:\Users\moradi\PycharmProjects\plt\out')
for a in dir:
    img = cv2.imread(fr"C:\Users\moradi\Desktop\New folder (2)\{a}")
    plt.imshow(img[1262:, :])
    cropimg = img[1262:, :]
    #cv2.imshow(f'{a}', cropimg)
    cv2.imwrite(f'{a}.jpg', cropimg)
    cv2.waitKey(0)
