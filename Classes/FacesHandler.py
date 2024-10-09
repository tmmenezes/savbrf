import cv2
import face_recognition as fr
from cv2 import distanceTransform, waitKey
from face_recognition import face_locations, compare_faces
from numpy.core.defchararray import upper


class FacesHandler:
    """
        metodo construtor recebe argumentos do arquivo principal (alvo principal)
        main_file_path: caminho para a imagem principal, na qual se encontra o alvo
        imgages_dir_path: caminho do diretório onde se encontram as imagens para análise
    """
    def __init__(self, main_img_path):
        self.main_img_path = main_img_path
        self.main_img = fr.load_image_file(main_img_path)
        self.main_img = cv2.cvtColor(self.main_img, cv2.COLOR_BGR2RGB)
        self.face = self.find_faces(self.main_img)[0]
        self.encode = fr.face_encodings(self.main_img)[0]

    def find_faces(self, image):
        faces = face_locations(image)
        return faces

    def show_target_face(self, name):
        face = self.face
        cv2.rectangle(self.main_img, (face[3], face[0]), (face[1], face[2]), (0, 255, 0), 3)
        (w, h), _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 3)
        cv2.rectangle(self.main_img, (face[3], face[0] - h * 2), (face[3] + w, face[0]), (0, 255, 0), -2)
        cv2.putText(self.main_img, name, (face[3] + 1, face[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
        cv2.namedWindow(name, 0)
        cv2.imshow(name,self.main_img)

    def search_target(self, name, img_path):
        image = fr.load_image_file(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.compare_faces(name, image)

    def show_faces(self, image):
        faces = fr.face_locations(image)
        for face in faces:
            #compare_faces(face)
            cv2.rectangle(image, (face[3], face[0]), (face[1], face[2]), (0, 255, 0), 3)

        cv2.namedWindow('Test_faces', 0)
        cv2.imshow('Test_faces',image)

    def compare_faces(self, target_name, image):
        match = list()
        faces = fr.face_locations(image)
        face_encodings = fr.face_encodings(image, faces)
        #print(face_encodings)

        for face_encoding in face_encodings:
            match.append(fr.compare_faces([self.encode], face_encoding))

        print(match)

        i = 0
        f_count = 0

        for face in faces:
            name = 'Desconhecido ' + str(f_count)
            #print(match[i][0])

            if match[i][0]:
                name = target_name
            else:
                f_count += 1

            cv2.rectangle(image, (face[3], face[0]), (face[1], face[2]), (0, 255, 0), 3)
            (w, h), _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 3)
            cv2.rectangle(image, (face[3], face[0] - h * 2), (face[3] + w, face[0]), (0, 255, 0), -2)
            cv2.putText(image, name, (face[3] + 1, face[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 255, 255), 2)
            cv2.namedWindow('Image', 0)
            cv2.imshow('Image', image)
            i += 1
