import numpy as np
import matplotlib as mlt
import cv2
import glob,os
from shutil import copyfile
from os import listdir
from os.path import isfile, join
from os import walk

def list_all_image_files_in_dir(dir,target):
    file_list = []
    for root, dirs, files in os.walk(dir):
        if(root.endswith('image')):
            for file in files:
                if file.endswith(target):
                    full_path = os.path.join(root, file)
                    # print(full_path)
                    # print(file)
                    # print file_list
                    file_list.append(full_path)
    return file_list;


a = [1,2,3];
b = [2,3,4];
a = np.matmul(a,b);
file_list = list_all_image_files_in_dir("./kv1/",".jpg");
if  False == os.path.exists('all_image'):
    os.mkdir('all_image');
for file in file_list:
    print(file);
    # I = cv2.imread(file);
    # cv2.imshow('img',I);
    # cv2.waitKey(1);
    spl = str.split(file,'/');
    copyfile(file, './all_image/' +spl[len(spl)-1]);
exit(0)
I = cv2.imread('./kv1/NYUdata/NYU0001/image/NYU0001.jpg');
cv2.imshow('img',I);
cv2.waitKey();
print(a)
