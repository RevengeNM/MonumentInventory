import cv2
import webbrowser

cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        a = data
        cv2.destroyAllWindows()
        break

    cv2.imshow("scanner", img)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

print(str(a))
cv2.destroyAllWindows()