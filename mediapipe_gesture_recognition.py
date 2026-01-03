import cv2 as cv
import mediapipe as mp
import time
import numpy as np
import head_pose as hp
import pygame
import pygame_directions
from pygame_directions import playsound
pygame.mixer.init()
NOSE_TIP = 1
OUTER_LEFT_EYE = 33
OUTER_RIGHT_EYE = 263
MOUTH_LEFT = 61
MOUTH_RIGHT = 291
NOSE_BRIDGE = 199
HEAD_POSE= {NOSE_TIP: {"2d": [],
                       "3d": []
                      },
            OUTER_LEFT_EYE: {"2d": [],
                             "3d": []
                            },
            OUTER_RIGHT_EYE: {"2d": [],
                              "3d": []
                             }, 
            MOUTH_LEFT: {"2d": [],
                         "3d": []
                        },
            MOUTH_RIGHT: {"2d": [],
                          "3d": []
                         }, 
            NOSE_BRIDGE: {"2d": [],
                        "3d": []
                        }}


def main():
    capture = cv.VideoCapture(0)
    capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    pTime= 0

    mpDraw = mp.solutions.drawing_utils
    mpFaceMesh = mp.solutions.face_mesh
    mpDrawingStyles = mp.solutions.drawing_styles
    drawSpecs = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
    mpFaceMeshConnections = mp.solutions.face_mesh_connections

    faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
    while True:
        #start with fresh lists for every image
        face_3d = []
        face_2d = [] 
        sucess, img = capture.read()
        img_h, img_w, _ = img.shape
        #Flip used for fixing the left-right orientation.
        img = cv.flip(img, 1)
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        #Used to improve performance 
        imgRGB.flags.writeable = False
        #faceMesh is detecting and getting each facial landmark. 
        results = faceMesh.process(imgRGB)
        #check if there is any face in the frame. 
        if results.multi_face_landmarks:
            #get landmarks of each individual face out of all the faces. 
            for faceLms in results.multi_face_landmarks:
                #getting the index and the corresponding landmark coordinates.
                for idx, landmark in enumerate(faceLms.landmark):
                    #Filtering out the specific landmarks that are in HEAD_POSE
                    if idx in HEAD_POSE:
                        x,y,z = landmark.x * img_w, landmark.y * img_h, landmark.z
                        HEAD_POSE[idx]["3d"] = [x, y, z]                
                        HEAD_POSE[idx]["2d"] = [x, y]
                        
                head_3d = np.array([HEAD_POSE[NOSE_TIP]["3d"], HEAD_POSE[NOSE_BRIDGE]["3d"], 
                                    HEAD_POSE[OUTER_LEFT_EYE]["3d"], HEAD_POSE[OUTER_RIGHT_EYE]["3d"],
                                    HEAD_POSE[MOUTH_LEFT]["3d"], HEAD_POSE[MOUTH_RIGHT]["3d"]],
                                    dtype=np.float64)
                head_2d = np.array([HEAD_POSE[NOSE_TIP]["2d"], HEAD_POSE[NOSE_BRIDGE]["2d"], 
                                    HEAD_POSE[OUTER_LEFT_EYE]["2d"], HEAD_POSE[OUTER_RIGHT_EYE]["2d"],
                                    HEAD_POSE[MOUTH_LEFT]["2d"], HEAD_POSE[MOUTH_RIGHT]["2d"]],
                                    dtype=np.float64)
                pitch, yaw, roll = hp.get_head_angle(img_w, img_h, head_3d, head_2d)
                pitch = pitch * 360
                yaw = yaw * 360
                roll = roll * 360
                print(f"yaw: {str(np.round(yaw, 2))}, pitch: {str(np.round(pitch, 2))}, roll: {str(np.round(roll, 2))}")
                cv.putText(img, f"Pitch: {str(np.round(pitch, 2))}, Yaw: {str(np.round(yaw, 2))}, Roll: {str(np.round(roll, 2))}", (20,30), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), thickness=2)
                

                #pygame_directions.playsound(yaw, pitch, roll)
                pygame_directions.drum_sounds(yaw, pitch, roll)
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv.putText(img,f'FPS: {int(fps)}', (20,70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0 ,0), thickness=2)

            mpDraw.draw_landmarks(img, faceLms, mpFaceMeshConnections.FACEMESH_CONTOURS, drawSpecs, drawSpecs)
        cv.imshow("Grayscale Webcam Feed", img)
        key = cv.waitKey(1)
        
        if key == ord('r'):
            break

    capture.release()

    cv.destroyAllWindows()

if __name__=="__main__":
    main()


