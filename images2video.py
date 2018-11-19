import cv2
import numpy as np
import os
 
from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    #files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.cv.CV_FOURCC('i', 'Y', 'U', 'V'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
        #print(frame_array[i])
    out.release()
 
def main():
    pathIn= './frames_output_7/'
    pathOut = 'video.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)
 
if __name__=="__main__":
    main()