import numpy as np
import matplotlib as mlt
import cv2
import glob,os
from os import listdir
from os.path import isfile, join
from os import walk

def list_all_image_files_in_dir(dir):
    for root, dirs, files in os.walk(dir):
        if(root.endswith('image')):
            for file in files:
                if file.endswith('.jpg'):
                    full_path = os.path.join(root, file)
                    print(full_path)
                    # print(file)
                    # print file_list
                    file_list.append(full_path)
    return file_list;

a = [1,2,3];
b = [2,3,4];
a = np.matmul(a,b);
file_list = list_all_image_files_in_dir("kv1/NYUdata/");
exit(0)
I = cv2.imread('./kv1/NYUdata/NYU0001/image/NYU0001.jpg');
cv2.imshow('img',I);
cv2.waitKey();
print(a)
