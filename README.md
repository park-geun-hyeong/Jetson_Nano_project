# Jetson_Nano_project

<h2>###NVIDA jetson-nano 를 다루며 진행했던 project repository###</h2>

<h3>1. geture-classification</h3>
- get_img.py : jetson-nano camera를 이용해 0,1,2의 이미지 캡쳐(image dataset 만들기)<br>
- div_img.py : 캡쳐한 이미지를 train,test dataset으로 나누기<br>
- classification.py : Pytorch를 활용해 이미지 분류 model 생성
- model_gesture.pth : 0,1,2의 gesture를 분류해주는 model(Conv layer가 아닌 Linear layer를 통해 분류) <br>
![185img](https://user-images.githubusercontent.com/69515694/119270879-e240fe00-bc39-11eb-915d-70d570496fee.png)
![83img](https://user-images.githubusercontent.com/69515694/119270881-e3722b00-bc39-11eb-8d61-a2813e3fb507.png)
![266img](https://user-images.githubusercontent.com/69515694/119270884-e4a35800-bc39-11eb-9789-466974e49819.png)
