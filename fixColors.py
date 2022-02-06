import cv2

for i in range(66):
    file_name = "bb8_sample{}.png".format(i)
    cv_image = cv2.imread(file_name)
    fixed_color = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    cv2.imwrite(file_name, fixed_color)
    print(file_name + " has been coverted!")
    i += 1