import cv2
import face_recognition as fr
from face_recognition import face_locations


class PhotoHandler:
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.img = cv2.imread(file_path + '/' + file_name)

    def find_faces(self):
        faces = face_locations(self.img)
        return faces

    def show_faces(self, faces):
        for face in faces:
            cv2.rectangle(self.img, (face[3], face[0]), (face[1], face[2]), (0, 255, 0), 3)

        cv2.namedWindow('Faces', 0)
        cv2.imshow('Faces',self.img)

    def compare_faces(self):
        pass