import cv2 as cv
import mediapipe as mp
import time

capture = cv.VideoCapture(0)
pTime= 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
mpDrawingStyles = mp.solutions.drawing_styles
drawSpecs = mpDraw.DrawingSpec(thickness=2, circle_radius=1)
mpFaceMeshConnections = mp.solutions.face_mesh_connections

faceMesh = mpFaceMesh.FaceMesh(max_num_faces=9)

while True:
    sucess, img = capture.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    results = faceMesh.process(imgRGB)

 
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            print(faceLms)
            mpDraw.draw_landmarks(img, faceLms, mpFaceMeshConnections.FACEMESH_CONTOURS, drawSpecs, drawSpecs)
            
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img,f'FPS: {int(fps)}', (20,70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0 ,0), thickness=2)   
    cv.imshow("Grayscale Webcam Feed", img)  
    key = cv.waitKey(1)

    if key == ord('r'):
        break

capture.release()

cv.destroyAllWindows()