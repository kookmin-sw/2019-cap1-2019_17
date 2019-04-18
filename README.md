## SUMMER

## 2019년 캡스톤 디자인 17조


---------------------------------------

### 1. 프로젝트 소개


연설이나 발표, 공표 등 음성을 통한 많고 긴 내용을 사람들이 모두 흡수하고 이해하기에는 무리가 있다. 중대하거나 중요한 내용이지만 그만큼 내용의 양도 많아지고 길어 지기 때문에 사람이 집중하는 시간에는 한계가 있어서 중요한 부분을 놓칠 수도 있다. 그러하기 때문에 방송을 통해 다시 보기를 하거나, 영상을 녹화하거나, 음성을 녹음하는 등 다양한 방법으로 내용을 백업하여 나중에 다시 활용하고 있다. 이 부분에 착안하여 사용 용도에 따라 음성 데이터를 텍스트로 변환한 후 그 텍스트로 변환된 문장을 중요 문장 단위로 추출하여 제공해주는 프로젝트를 계획하였다.

이 프로젝트의 전체적인 구조 및 개발 내용은 크게 3가지로 나뉜다.

-  음성인식을 위해 외부 API(Google Speech API)를 사용하여 음성데이터를 텍스트로 변환한 후 그 데이터를 서버에 저장한다.

-  서버에 저장된 텍스트 데이터를 요약 알고리즘을 적용하여 핵심 문장으로만 요약되도록 데이터를 가공한다.

-  가공된 데이터를 다시 가져와서 사용자에게 제공한다.


### Abstract

It is difficult for people to absorb and understand many long and long contents through speeches, speeches, announcements, etc. It is important or important, but because the amount of content is getting longer and longer, there is a limit to the amount of time people concentrate on, which can miss important parts. Because of this, the contents are backed up in various ways, such as viewing again via broadcast, recording video, recording audio, etc., and reuse it later. We focused on this part and planned a project that converts voice data to text according to the use purpose and extracts the sentence converted into the text by important sentence unit.



---------------------------------------

### 2. 소개 영상

[![Video Label](https://img.youtube.com/vi/UIbcKwdViQM/0.jpg)](https://youtu.be/UIbcKwdViQM)

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

- 역할 : Google Speech API 호출 및 Time Stamp와 Hash Tag 기능을 구현. Django와 MongoDB를 이용해 서버를 구축하고 데이터를 관리.

- E-mail : ysh827@kookmin.ac.kr 


#### 4. 팀원 : 정경진

- 학번 : 20153225

- 역할 : Google Speech API 호출 및 Time Stamp와 Hash Tag 기능을 구현.

- E-mail : okyungjin@gmail.com


#### 5. 팀원 : 정예원

- 학번 : 20165161

- 역할 : 사용자 인터페이스 설계. Django 와 MongoDB 를 이용해 서버를 구축하고 데이터를 관리.

- E-mail : yes3427@gmail.com


---------------------------------------

### 4. 사용법


소스코드 제출 시 업로드 예정.


---------------------------------------

### 5. 기타

