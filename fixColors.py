import cv2
from PIL import Image

for i in range(66):
    file_name = "bb8_sample{}.png".format(i)
    cv_image = cv2.imread(file_name)
    bgr2rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    real_image = Image.fromarray(bgr2rgb)
    real_image.save(file_name)
    print(file_name + " has been coverted!")
    i += 1