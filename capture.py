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
    if not os.path.exists("my_images"):
        os.makedirs("my_images")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Couldn't open the webcam.")
        return False

    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't capture a frame.")
        cap.release()
        return False

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) == 0:
        print("Error: No face detected. Please show your face properly.")
        cap.release()
        return False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            print("Error: No eyes detected. Please show your face properly.")
            cap.release()
            return False

    folder_path = "my_images"
    filename = f"{first_name}_{last_name}_{voter_id}.jpg"
    file_path = os.path.join(folder_path, filename)
    cv2.imwrite(file_path, frame)
    print(f"Image saved successfully: {file_path}")

    cap.release()
    return True

def register_voter():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    voter_id = input("Enter your voter's card ID: ")

    if is_voter_id_valid(voter_id):
        if capture_image(first_name, last_name, voter_id):
            print("Registration successful.")
        else:
            print("Registration failed during image capture.")
    else:
        print("Error: Voter ID already exists. Please choose a different one.")

if __name__ == "__main__":
    register_voter()