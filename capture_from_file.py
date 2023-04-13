import cv2 as cv
import main_functions as mf

cap = cv.VideoCapture('C:\\Users\Administrator\\Desktop\\data_test\\popitka_kraji_ugona.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    img1 = gray
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
mf.show_image(img1)
