import mediapipe as mp
import cv2 
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection=0.2, static_image_mode=True, max_num_faces=3, refine_landamrks=True)


def analyze_image(frame):
    result = face_mesh.process(frame)
    