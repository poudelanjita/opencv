import cv2 
cam_port = 0
cam = cv2.VideoCapture(cam_port)
# reading the input using the camera
while(1):
        project = input('Enter person name:')
        while(1):
                result,image = cam.read()
                cv2.imshow(project, image)
                if cv2.waitKey(1) == ord('q'): 
                 cv2.imwrite(project+".png", image)
                print("image taken")
                break
              