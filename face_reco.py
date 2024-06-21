import cv2
import os

def is_voter_id_valid(voter_id):
    # Check if voter ID already exists in the images directory
    image_files = os.listdir("my_images")
    for filename in image_files:
        if filename.endswith(".jpg"):
            existing_voter_id = filename.split("_")[1].split(".")[0]
            if existing_voter_id == voter_id:
                return False
    return True

def capture_image(first_name, last_name, voter_id):
    # Create directories to store images
    if not os.path.exists("my_images"):
        os.makedirs("my_images")

    # Check if voter ID is valid
    if not is_voter_id_valid(voter_id):
        print("Error: Voter ID already exists. Please choose a different one.")
        return

    # Load the pre-trained face and eye cascade classifiers
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # Open the webcam (the default webcam, usually index 0)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Couldn't open the webcam.")
        return

    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Couldn't capture a frame.")
        cap.release()
        return

    # Convert the frame to grayscale for face and eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Check if faces are detected
    if len(faces) == 0:
        print("Error: No face detected. Please show your face properly.")
        cap.release()
        return

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes in the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Check if eyes are detected
        if len(eyes) == 0:
            print("Error: No eyes detected. Please show your face properly.")
            cap.release()
            return

        # Draw rectangles around the detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Save the captured frame as an image file
        folder_path = "my_images"
        filename = f"{first_name}_{last_name}_{voter_id}.jpg"
        file_path = os.path.join(folder_path, filename)
        cv2.imwrite(file_path, frame)
        print(f"Image saved successfully: {file_path}")

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    voter_id = input("Enter your voter's card ID: ")
    capture_image(first_name, last_name, voter_id)