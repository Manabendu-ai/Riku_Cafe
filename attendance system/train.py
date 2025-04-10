import cv2 as cv
import os
import numpy as np
from PIL import Image

rec = cv.face.LBPHFaceRecognizer_create()
path = 'dataset/know_faces'
def trainData(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs = []

    for imagePath in imagePaths:
        img = Image.open(imagePath).convert('L')
        faceNp = np.array(img, 'uint8')
        id = int(os.path.split(imagePath) [-1].split(".")[1])
        faces.append(faceNp)
        IDs.append(id)
        cv.imshow('trainimgs',faceNp)
        cv.waitKey(100)

    return np.array(IDs), faces

ids, faces = trainData(path)
rec.train(faces, ids)
rec.save('trainingData.yml')

