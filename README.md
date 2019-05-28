## SUMMER

## 2019년 캡스톤 디자인 17조


---------------------------------------

### 1. 프로젝트 소개


TED와 같은 영어 강연에서 전문적이고 긴 내용을 사람들이 한번에 이해하기는 어렵다. 이러한 강연은 길이가 길어서 집중하는데 한계가 있고 중요한 부분을 놓치게 된다. 따라서 강연을 다시 보거나 음성을 녹음하는 등의 방법으로 내용을 다시 이해하려 한다. 이러한 과정에서 착안하여 음성 데이터를 텍스트로 변환한 후 중요 문장 단위로 추출하여 제공해주는 프로젝트를 계획하였다.  
(TED는 기술, 오락, 디자인 등과 관련된 강연회이다.)


이 프로젝트의 전체적인 구조 및 개발 내용은 크게 3가지로 나뉜다.  
  
-  음성인식을 위해 외부 API(Google Speech-to-Text API)를 사용하여 음성데이터를 텍스트로 변환한 후 그 데이터를 서버에 저장한다.  

-  서버에 저장된 텍스트 데이터를 요약 알고리즘을 적용하여 핵심 문장으로만 요약되도록 데이터를 가공한다.

-  가공된 데이터를 다시 가져와서 사용자에게 제공한다.


### Abstract

It is difficult for people to understand the professional and long contents of English lectures like TED* at once. These lectures are long, so people have a limited concentration and miss the important part. Therefore, they try to understand the content again, such as re-viewing the lecture or recording a voice. In this process, we have planned a project that converts voice data into text and extracts it in units of import agreements.

The overall structure and development of this project are divided into three main categories.

-  For voice recognition, we use external API (Google Speech-to-Text API) to convert voice data to text and store the data in server.

-  Apply the summarization algorithm to the text data stored on the server to process the data so that it is summarized as a core sentence only.


-  Bring the processed data back to the user.



---------------------------------------

### 2. 시연 영상

[![Video Label](https://img.youtube.com/vi/hhs1IOTSo3Y/0.jpg)](https://youtu.be/hhs1IOTSo3Y)

---------------------------------------

### 3. 팀 소개


#### Professor : **박수현 교수님**


#### 1. 팀장 : 김기성

- 학번 : 20133193

- 역할 : TF-IDF 와 TextRank 알고리즘을 이용한 텍스트 요약 기능을 구현.

- E-mail : kimgisuo@gmail.com


#### 2. 팀원 : 김윤성

- 학번 : 20133210

- 역할 : TF-IDF 와 TextRank 알고리즘을 이용한 텍스트 요약 기능을 구현.

- E-mail : msmf3@naver.com


#### 3. 팀원 : 양성호

- 학번 : 20133235

- 역할 : UI설계 및 구현, Google Speech API 호출 및 Time Stamp 와 Hash Tag 기능을 구현. Django와 MongoDB를 이용해 서버를 구축하고 데이터를 관리.

- E-mail : ysh827@kookmin.ac.kr 


#### 4. 팀원 : 정경진

- 학번 : 20153225

- 역할 : UI설계 및 구현, Google Speech API 호출 및 Time Stamp 와 Hash Tag 기능을 구현. Django와 MongoDB를 이용해 서버를 구축하고 데이터를 관리.

- E-mail : okyungjin@gmail.com


#### 5. 팀원 : 정예원

- 학번 : 20165161

- 역할 : UI설계 및 구현, Google Speech API 호출 및 Time Stamp 와 Hash Tag 기능을 구현. Django와 MongoDB를 이용해 서버를 구축하고 데이터를 관리.

- E-mail : yes3427@gmail.com


---------------------------------------

### 4. 사용자 메뉴얼

<img src="https://github.com/kookmin-sw/2019-cap1-2019_17/blob/master/img/사용자매뉴얼.png" width="100%"></img>




