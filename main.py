import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#choose input type

c = input("'w' for webcam and 'v'for vidio : \t")
choose = c.lower()

if choose=='w':
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

elif choose == 'v':
        # choose your exist video
        p = input('enter the video path : \t')
        path = p.replace('"','')
        cap = cv2.VideoCapture(path)

else:
    print("Invalid Input!")
    exit()

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale (face detection works better in grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Face Detection tool by @darker_m_t', frame)

    # Exit the loop when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
