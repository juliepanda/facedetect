import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

# set celeb and find 
celeb_img = cv2.imread('face.jpg')
celeb_gray = cv2.cvtColor(celeb_img, cv2.COLOR_BGR2GRAY)
celeb_faces = face_cascade.detectMultiScale(celeb_gray, 1.05, 5)

x, y, w, h = celeb_faces[0]

while(True):
    ret, img = cap.read()

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray_img, 1.05, 5)

    for (p,q,r,s) in faces:
        cv2.rectangle(img,(p,q),(p+r,q+s),(255,0,0),2)
        face_gray = gray_img[q:q+s, p:p+r] 
        face_color = img[q:q+s, p:p+r] 
        eyes = eye_cascade.detectMultiScale(face_gray) 
        for (ep,eq,er,es) in eyes:
           cv2.rectangle(face_color,(ep,eq),(ep+er,eq+es), (0,255,0),2)
    celeb_img = cv2.resize(celeb_img,(r,s))
    print celeb_img.shape

    img[q:q+s, p:p+r] = celeb_img[0:celeb_img.shape[0], 0:celeb_img.shape[1]]
    cv2.imshow("output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break


cap.release()
cv2.destroyAllWindows()
