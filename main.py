import cv2

cap = cv2.VideoCapture(0)
width =320
height = 240
cap.set(3, width)
cap.set(4, height)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('Capture', frame)

    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    cv2.imshow('Gaussian Blurring', blur)

    #filter = cv2.Laplacian(frame, cv2.CV_64F)
    filter = cv2.Canny(frame, 100, 100)
    cv2.imshow('Laplacian Filter', filter)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
