import cv2
import pyttsx3

faceCascade = cv2.CascadeClassifier("cascade.xml")
frameWidth = 640
frameHeight = 480

video_capture = cv2.VideoCapture('bank_robbey_video.mp4')

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    frames = cv2.resize(frames, (frameWidth, frameHeight))
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Video", frames)
        if (x != 0):
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 200)
            engine.say("Thief Detected")
            engine.runAndWait()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

