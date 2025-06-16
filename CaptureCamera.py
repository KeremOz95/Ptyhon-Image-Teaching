import cv2
import os

def main(Path):

    if not os.path.exists(Path):
        os.makedirs(Path)
    cap = cv2.VideoCapture(0)
    i = 0

    if "Compare_Image" in Path:
        while True:
            _, frame = cap.read()
            cv2.imshow("Camera", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                cv2.imwrite(f"{Path}image_1.jpg", frame)
                break
    else:
        while True:
            _, frame = cap.read()
            cv2.imshow("Camera", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                i += 1
                cv2.imwrite(f"{Path}image_{i}.jpg", frame)
                print(f"Image {i} captured and saved as image_{i}.jpg")
            elif key == ord('v'):
                break
    cap.release()
    cv2.destroyAllWindows()
    return i