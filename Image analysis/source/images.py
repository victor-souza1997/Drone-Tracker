import numpy as np
from PIL import Image
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os, sys

class Image():
    def getImgVector(self, face_set, img):
        ##"""Return a raster of integers from a PGM as a list of lists."""
        path ='C:/Users/victo/OneDrive/Documentos/Codigos/Drone Tracker/Image analysis/utils/conteudo/s'+str(face_set)+'/'+str(img)+'.pgm'
        pgmf = open(path, 'rb')
        header = pgmf.readline()
        assert header[:2] == b'P5'
        (width, height) = [int(i) for i in pgmf.readline().split()]
        depth = int(pgmf.readline())
        assert depth <= 255
        print(str(width) +" "+ str(height)+" "+str(width*height))
        M = np.fromfile(pgmf, dtype = np.uint8)
        pgmf.close()
        return M[0:width*height:4]
        vetorimg = read_pgm(2)
        print(vetorimg)

    def addVectorImg(self, face_set,img):
        #f=open("C:/Users/victo/OneDrive/Documentos/Codigos/Drone Tracker/Image analysis/utils/imagens/faces/face1.txt", "a+")
        with open("C:/Users/victo/OneDrive/Documentos/Codigos/Drone Tracker/Image analysis/utils/imagens/faces/face"+str(face_set)+".txt", "a") as myfile:
            np.savetxt(myfile,img)
        myfile.close()
    def readImage(self, face_set, n, length):
        #with open("C:/Users/victo/OneDrive/Documentos/Codigos/Drone Tracker/Image analysis/utils/imagens/faces/face1.txt", "r") as myfile:
        return np.loadtxt("C:/Users/victo/OneDrive/Documentos/Codigos/Drone Tracker/Image analysis/utils/imagens/faces/face"+str(face_set)+".txt",delimiter="\n")[(n-1)*length:length*n]
    def showImage(self, img, length, width):
        im = img.reshape(length, width)
        plt.gray()
        plt.imshow(im)
        plt.show()

#width = 92 and length = 112 in all the imagens
#n = 10
width = 23
length = 112
img = Image()
face_set = 1
#for i in range(1,11):#
    #M = img.getImgVector(face_set,i)
    #print(M.shape)#
    #img.addVectorImg(face_set, M)
x = img.readImage(face_set, 1,  width*length).T
img.showImage(x,  length, width)

#def reScaleImage(self, M, resize):
