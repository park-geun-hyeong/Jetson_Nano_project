import os
import cv2
import numpy as np
import glob 
import shutil


 print("0 image_file_number : {}".format(len(os.listdir("images/training/0"))))
 print("1 image_file_number : {}".format(len(os.listdir("images/training/1"))))
 print("2 image_file_number : {}".format(len(os.listdir("images/training/2"))))

for i in range(3):
    img_list = glob.glob("images/training/"+str(i)+"/*.png")
    print("img_num of number {}: {}".format(i, len(img_list)))

    idx_list = np.random.choice(len(img_list), 50, replace=False)
    idx_list = img_list[:50]
    print("idx_list of number {} : {}".format(i, idx_list))
    print("================================================")
    print()
   
    for idx in idx_list:
         src_path = idx
         dst_path = 'images/testing/'+str(i)+"/"+str((idx.split('/')[3]).split('.')[0])+".png"

        
         shutil.move(src_path, dst_path)



print(os.getcwd())

for i in range(3):
    test_img_list = sorted(os.listdir("/home/park/lec22/images/testing/"+str(i)))
    print("{} test img: {}".format(i, test_img_list))
    print(len(test_img_list))
    print("======================")



