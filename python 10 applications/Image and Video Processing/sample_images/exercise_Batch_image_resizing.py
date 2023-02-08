import cv2
import glob

imgs = glob.glob("*.jpg")

print(imgs)

for i in imgs:
    img = cv2.imread(i,0)
    resized_image = cv2.resize(img,(100,100))
    cv2.imwrite("revised_"+ i,resized_image)
