import cv2
import datetime
from pathlib import Path

PIC_FOLDER_CAMERA = 'pic_folder_camera'
Path(PIC_FOLDER_CAMERA).mkdir(parents=True, exist_ok=True)
PIC_FOLDER_CAMERA = Path(PIC_FOLDER_CAMERA)


def capture(camera_number: int):
    # Open a connection to the webcam (0 is typically the default camera)
    cap = cv2.VideoCapture(camera_number)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Cannot open webcam")
        exit()

    # Capture a single frame
    ret, frame = cap.read()

    # If the frame is captured successfully, save it
    if ret:
        time_now = datetime.datetime.now().strftime('%d_%m_%Y__%H_%M_%S.%f')
        filename = f"{time_now}.jpg"
        file_path = PIC_FOLDER_CAMERA / filename
        cv2.imwrite(file_path, frame)

        return file_path, filename

    # Release the camera
    cap.release()

    return None, None
