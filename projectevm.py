import cv2
import os
import face_recognition as fr


import numpy as np

def load_registered_data():
    registered_data = {}
    # Your code to load registered voter data from files or database
    return registered_data

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

    # Release the webcam
    cap.release()

    # Save the captured frame as an image file
    folder_path = "my_images"
    filename = f"{first_name}_{last_name}_{voter_id}.jpg"
    file_path = os.path.join(folder_path, filename)
    cv2.imwrite(file_path, frame)
    print(f"Image saved successfully: {file_path}")

    return file_path

voted_voters = set()  # Set to store the IDs of voters who have already voted

# Function for the voting system
def voting_system(first_name, last_name, voter_id):
    registered_data = load_registered_data()

    # Check if the voter ID exists in the registered data
    if voter_id not in registered_data:
        print("Error: Voter ID not found.")
        return

    # Check if the voter has already voted
    if voter_id in voted_voters:
        print("Error: You have already voted.")
        return

    # Capture the voter's image
    image_path = capture_image(first_name, last_name, voter_id)
    if image_path is None:
        return

    # Perform face recognition
    # Your face recognition code goes here using the captured image

    # Once face recognition is successful, proceed with voting
    print(f"Welcome {first_name} {last_name} (Voter ID: {voter_id})")
    # Mark the voter as voted
    voted_voters.add(voter_id)
    # Proceed with the voting process
    while True:
        candidate_selected = input("Enter the candidate number (1, 2, or 3): ")
        if candidate_selected in ["1", "2", "3"]:
            candidate_name = f"Candidate{candidate_selected}"
            # Vote for the selected candidate
            # Your voting code goes here
            print(f"Thank you for voting!{first_name} {last_name}")
            break

if __name__ == "__main__":
    registered_voters = load_registered_data()
    vote_counts = {"Candidate1": 0, "Candidate2": 0, "Candidate3": 0}

    while True:
        # Your voting system initialization here...
        first_name = input("Enter your first name (or 'Q' to quit): ")
        if first_name.upper() == 'Q':
            break  # Quit the program if 'Q' is entered
        
        last_name = input("Enter your last name (or 'Q' to quit): ")
        if last_name.upper() == 'Q':
            break  # Quit the program if 'Q' is entered
        
        voter_id = input("Enter your voter's card ID (or 'Q' to quit): ")
        if voter_id.upper() == 'Q':
            break  # Quit the program if 'Q' is entered
        
        # Check if the input is 'Q' before validating the voter's ID
        if voter_id.upper() != 'Q':
            voting_system(first_name, last_name, voter_id)
        
        # Check if the voter has voted and break the loop if they have
        if voter_id in registered_voters and registered_voters[voter_id]['voted']:
            break