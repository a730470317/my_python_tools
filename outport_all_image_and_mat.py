import numpy as np
import matplotlib as mlt
import cv2
import glob,os
import scipy.io as sio
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
                    file_list.append(full_path)
    return file_list;

def process_all_mat(image_files_list):
    mat_file_list=[];
    for file in image_files_list:
        spl = str.split(file, '/');
        mat_name=''
        for i in range(1,len(spl)-2):
        # mat_name = mat_name + spl[i];
            mat_name += (spl[i]);
            mat_name += '/';
        mat_name+='seg.mat'
        print mat_name
        mat_file_list.append(mat_name);
    return mat_file_list;

def convert_mat_to_img(mat_file):
    mat = sio.loadmat(mat_file);
    image = mat['seglabel'];
    return image;

dir_name = '../all_data';
txt_file = open('train.txt','w+');
image_files_list = list_all_image_files_in_dir("./", ".jpg");
mat_file_list = process_all_mat(image_files_list);
if  False == os.path.exists(dir_name):
    os.mkdir(dir_name);
for i in range(1,len(image_files_list)):
    image_file = image_files_list[i];
    mat_file = mat_file_list[i];
    print(image_file);
    print(mat_file);
    # I = cv2.imread(image_file);
    # cv2.imshow('img',I);
    # cv2.waitKey(1);
    spl = str.split(image_file,'/');
    prefix = spl[len(spl)-3];
    mat_img = convert_mat_to_img(mat_file);
    ############save file##########
    out_raw_image_name = dir_name + '/' +prefix + '.jpg';
    out_seg_image_name = dir_name + '/' + prefix + '_seg.jpg';
    out_mat_file_name = dir_name + '/' + prefix + '.mat';
    txt_file.write(out_raw_image_name+' '+out_seg_image_name+'\n');
    copyfile(image_file, out_raw_image_name);
    # copyfile(mat_file, out_mat_file_name);
    cv2.imwrite(out_seg_image_name , mat_img);
txt_file.close();