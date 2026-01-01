import cv2 as cv
import numpy as np
def get_head_angle(width, height, head_3d, head_2d ):
    camera_matrix = np.array([[width, 0, height/2,], 
                              [0, width, width/2],
                              [0, 0, 1]])
    
    distortion_matrix = np.zeros((4,1), dtype=np.float64)
    _, rotation_vector, translation_vector = cv.solvePnP(head_3d, head_2d, camera_matrix, distortion_matrix,)


    rotation_matrix, _ = cv.Rodrigues(rotation_vector)

    angles, *_ = cv.RQDecomp3x3(rotation_matrix)
    #order of the pitch, yaw, roll is along their respective axis. 
    yaw, pitch, roll = angles
    
    return yaw, pitch, roll



    