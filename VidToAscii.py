import cv2
import os
import time
characters = " .:-=+*#%@"

def map_brightness_to_character(brightness):
    index = int((brightness / 255) * (len(characters) - 1))
    return characters[index]

video_path = 'Bad Apple.mkv'
cap = cv2.VideoCapture(video_path) # change video_path to 0 for webcam feed
time.sleep(5)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    disp_frame = cv2.resize(frame, (640, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

    cv2.imshow('frame', disp_frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    resized_frame = cv2.resize(gray_frame, (160, 80))

    ascii_art = ""
    for row in resized_frame:
        for brightness in row:
            ascii_art += map_brightness_to_character(brightness)
        ascii_art += "\n"

    time.sleep(0.1)
    os.system('cls')
    print(ascii_art)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
