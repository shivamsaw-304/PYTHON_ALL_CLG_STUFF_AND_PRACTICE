import cv2



# Step 1: Create camera object
camerObject = cv2.VideoCapture(0)



# Step 2: Continuously capture frames
while True:

     ret, frame = camerObject.read()

     if not ret:
        print("Camera not accessible")
        break
    
    # Display captured frame
     cv2.imshow("My First Cawerwe", frame)

    # Exit when Q is pressed
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camerObject.release()

# Step 4: Close all OpenCV windows
cv2.destroyAllWindows()