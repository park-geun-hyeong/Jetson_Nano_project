import numpy as np
import glob
import os
import cv2

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.init as init

train_path = '/home/park/lec22/images/training/'
test_path = '/home/park/lec22/images/testing/'

train_img = []
test_img = []




for i in range(3):
   # print(len(os.listdir(train_path+str(i)))) 
   # print(len(os.listdir(test_path+str(i))))
    
    tr_list_num = glob.glob("images/training/"+str(i)+"/*.png")
    train_img += tr_list_num
    
    te_list_num = glob.glob("images/testing/" +str(i)+ "/*.png")
    test_img += te_list_num

print(len(train_img), len(test_img))


imgs_vec = []

for i in range(len(train_img)):
    img = cv2.imread(train_img[i], cv2.IMREAD_GRAYSCALE)
    img_resize = cv2.resize(img, dsize=(48,27))

    img_vec = np.reshape(img_resize, 48*27)
    imgs_vec.append(img_vec)


x = np.array(imgs_vec)
imgs_vec.clear()
print("img_vec_shpae : {}".format(x.shape))
print(type(x))

target_list=[]

for i in range(3):
    tr_list_num = glob.glob("images/training/"+str(i)+"/*.png")
    target_list += len(tr_list_num)*[i]

y = np.array(target_list)
target_list.clear()
print("target shpae:{}".format(y.shape))

x_tensor = torch.tensor(x).float()
y_tensor = torch.tensor(y.astype(np.int64))

model = nn.Sequential(
        
        nn.Linear(48*27, 512),
        nn.ReLU(),

        nn.Linear(512,256),
        nn.ReLU(),

        nn.Linear(256,128),
        nn.ReLU(),

        nn.Linear(128, 32),
        nn.ReLU(),

        nn.Linear(32, 8),
        nn.ReLU(),

        nn.Linear(8,3)
    
        )


loss_fn=nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(100):
    optimizer.zero_grad()

    cost = model(x_tensor)
    loss = loss_fn(cost, y_tensor)

    loss.backward()
    optimizer.step()

    if epoch%10==0:
        print("epoch:{}, loss:{:.4f}".format(epoch, loss.item()))


output = model(x_tensor)

pred = torch.argmax(output, dim=1)
pred_np = pred.detach().numpy()

acc = np.mean(pred_np==y)
print("acc:{:.4f}".format(acc))

torch.save(model, "model_gesture.pth")









