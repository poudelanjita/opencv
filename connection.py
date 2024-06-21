import serial
import cv2
import os

# Setup serial connection (adjust 'COM3' and baud rate as necessary)
arduino = serial.Serial('COM3', 9600, timeout=1)

def is_voter_id_valid(voter_id):
    # Your existing validation function

def capture_image(first_name, last_name, voter_id):
    # Your existing image capture function

def listen_for_voters():
    while True:
        data = arduino.readline().decode().strip()
        if data == 'v':  # Voter ready signal received
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            voter_id = input("Enter your voter's card ID: ")
            if capture_image(first_name, last_name, voter_id):
                arduino.write(b'y')  # Send validation success signal
            else:
                arduino.write(b'n')  # Send validation failure signal

if __name__ == "__main__":
    listen_for_voters()