## SUMMER

## 2019년 캡스톤 디자인 17조


---------------------------------------

### 1. 프로잭트 소개


본 프로젝트는 대학 강의를 녹음하여 나중에 시험공부를 위해 활용하기 위해서는 그 녹음파일에 대한 필기 자료가 필요하다. 또는 누군가와의 인터뷰를 녹음하여 그에 관한 기사나 글을 작성하게 될 때 그에 대한 텍스트 데이터가 필요하다. 그래서 본 프로젝트는 사용용도에 따라 간편하게 녹음파일만을 이용하여 텍스트로 변환된 자료를 제공하고 더 나아가 그 자료를 요약하여 필기 노트 형식으로 제공해주는 프로젝트를 계획하였다.

이 프로젝트의 전체적인 구조 및 개발 내용은 크게 3가지로 나뉜다.

-  음성인식을 위해 외부 API(Google Speech API)를 사용하여 음성데이터를 텍스트로 변환한 후 그 데이터를 서버에 저장한다.

-  서버에 저장된 텍스트 데이터를 요약 알고리즘을 적용하여 핵심 문장으로만 요약되도록 데이터를 가공한다.

-  가공된 데이터를 다시 가져와서 사용자에게 제공한다.


### Abstract

It is difficult for people to absorb and understand many long and long contents through speeches, presentations, official announcements, etc. Because the amount of content is getting longer and larger, there is a limit to the amount of time people concentrate on, which can miss important parts. But, It is significant or important. Because of this, the contents are backed up in various ways, such as viewing again via broadcast, recording video, recording audio, etc., and reuse it later. We focused on this part and planned a project that converts voice data to text according to the use purpose and extracts the sentence converted into the text by important sentence unit.

The overall structure and development of this project are divided into three main categories.

-  For voice recognition, we use external API (Google Speech API) to convert voice data to text and store the data in server.

-  Apply the summarization algorithm to the text data stored on the server to process the data so that it is summarized as a core sentence only.


-  Bring the processed data back to the user.


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
1) 사용자는 음성파일(flac포맷)을 업로드 버튼 클릭 또는 파일 드래그 & 드랍을 하여서 불러온다.
2) 파일이 불러와진다면 바로 요약 작업이 시작되고 완료될때까지 로딩창이 나타나는데 다음창으로 넘어갈때까지 기다린다.
3) 로딩창이 끝나고 다음 창으로 넘어가서 요약된 문장을 modal view형태로 보여주고 점선 버튼을 누르면 전체 텍스트 내용을 확인할 수 있다.
4) 특정 단어를 search bar에 타이핑한다면 어느 파일에 어느 시간대에 그 단어가 등장했는지에 대한 정보를 확인할 수 있다.
5) 파일 리스트 우측에 키워드태깅을 통해 그 파일에 대한 내용이 무슨내용인지 대략적으로 파악할 수 있다.


---------------------------------------

### 5. 기타

