# Jetson_Nano_project

<h2>###NVIDA jetson-nano 를 다루며 진행했던 project repository###</h2>

<h3>1. geture-classification</h3>
- get_img.py : jetson-nano camera를 이용해 0,1,2의 이미지 캡쳐(image dataset 만들기)<br>
- div_img.py : 캡쳐한 이미지를 train,test dataset으로 나누기<br>
- classification.py : Pytorch를 활용해 이미지 분류 model 생성
- model_gesture.pth : 0,1,2의 gesture를 분류해주는 model(Conv layer가 아닌 Linear layer를 통해 분류) 
