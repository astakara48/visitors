### 코로나 확산 방지를 위한 비대면 무인 방역 시스템

##### [활용 기술]

- Language : Python, HTML
  - Operating System : Window 10
  - FrameWork
    - TensorFlow 1.15.0  // Keras 2.2.4 // Django 2.1.5 // Opencv 4.2.0.34 // Qrcode 6.1 ...
  - Tool : Jupyter Notebook, Visual Studio Code
  - 담당한 부분 : 마스크 판독 모델 개발, 안면 인식 시스템 구축, Web 개발



#### 1. 프로젝트 개요

- COVID-19로 인한 많은 업소 특히 코인 노래방, PC방 등에서 많은 피해 발생

- 이러한 업소는 수기로 출입 명부를 작성하여 허위 정보 기재의 염려가 있고, 시설 관리자가 직접관리를 하여 접촉 불가피 등의 문제가 존재

- 이를 해결하기 위해 웹 서버를 활용한 비대면 무인 방역 서비스로 감염 노출 방지 효과 기대



#### 2. 프로젝트 주요 내용

- 전자 출입 명부
  - 카메라 기본 어플을 이용 QR 코드 인식
  - 개인 인적사항 등록
  - 개인 QR 코드 발급
- 마스크 착용 여부 판독
  - 마스크 미착용 데이터 10,986장, 마스크 착용 2,222장, 마스크 착용 불량 90장,  아예 사람이 없는 배경 사진 35장
  - 4개의 category에 ImageDataGenerator로 이미지 증식을 하여 Data로 활용
  - Block 1개는 (Conv2D + Batch_Normalization + MaxPooling2D + Dropout) 구성
  - 4개의 Block + (Flatten + Dense + Batch_Normalization + Dense(Softmax))이 모델이 됨
- 안면 인식 시스템
  - QR코드로 로그인 후 촬영 일정 범위에 맞춰서 촬영
  - 그 결과는 화면에 표시되는 Text와 스피커를 통한 Voice로 알려줌



#### 3. 프로젝트 결과

##### 1. 처음 web 화면

![1](https://user-images.githubusercontent.com/58538112/87533463-9d6e4180-c6cf-11ea-9631-00de1e701762.png)

- 해당 page에서 회원가입이 되어있을 경우 왼쪽은 발급 받은 QR코드를 인식하는 부분
- 회원가입이 안되어 있을 경우 오른쪽 QR 코드를 카메라로 인식하여 회원가입 페이지로 넘어간다.



##### 2. 모바일 회원가입 화면

![2](https://user-images.githubusercontent.com/58538112/87533465-9f380500-c6cf-11ea-9c74-02543323764d.png)

- 모바일로 회원가입을 하면 발급된 순서가 PK가 되며 해당 PK에 대한 QR코드를 생성



##### 3. 마스크 판독 화면

![4](https://user-images.githubusercontent.com/58538112/87533469-9fd09b80-c6cf-11ea-9d31-4b1667480141.png)
![5](https://user-images.githubusercontent.com/58538112/87533471-a0693200-c6cf-11ea-8b35-5e6b7b0cd444.png)

- 화면에서 녹색 박스에 얼굴을 맞춘 후 아래 버튼을 클릭하면 판독 시작



#### 4. Code 설명

##### 1) Model 생성

- MaskCheckModel_Ver*.ipynb 파일들은 모델만들고 테스트 했던 파일
- 