# Life_Alert_Bot
## : 생활 정보 알림이. 코로나, 날씨, 뉴스와 같은 생활 정보들에 관한 데이터를 웹크롤링을 통해 추출한 후 출력하는 텔레그램 챗봇
### 텔레그램을 통해 봇이 제공하는 기능
1. Covid-19 기능 : 코로나 바이러스 일일/평균/누적/도시별 확진자 수를 출력 + 코로나 방역 지침 출력
2. 날씨 기능 : 전국의 날씨를 볼 수 있는 링크 연결, 사용자의 위치를 추적하여 날씨 출력
3. 기온에 따라 추천하는 옷차림을 출력하는 기능
4. 뉴스 기능 : 실시간으로 업데이트되는 뉴스 중 가장 최신의 뉴스를 확인 가능

### 챗봇을 실행하기 위한 환경 설정

token = os.environ.get('token',"이곳에 토큰을 넣어주세요") 

id = 'chat_id'  

![챗봇과 연결하기](https://user-images.githubusercontent.com/102271635/169682805-a162964a-2064-4ec5-964c-ea21a9f8a51c.png)

### 실행화면
- 대화 리스트에 뜨는 챗봇

![화면](https://user-images.githubusercontent.com/102271914/169698491-1a24550d-9601-4759-aaad-e51341aab67b.PNG)

- 성공적인 실행시 자동으로 보내지는 메세지 

![main](https://user-images.githubusercontent.com/102271914/169798289-5e154982-57b0-46b1-9a96-27438d02d6c4.PNG)

- 주어지는 기능이 아닌 다른 명령을 입력했을 때 나오는 화면

![error](https://user-images.githubusercontent.com/102271914/169706574-365d3c39-0730-484c-b90a-ba4506c1d08f.PNG)

※아래 링크를 클릭해서 기능별 더 자세한 실행화면을 확인하세요.

[Covid-19 기능 실행화면](https://github.com/jingyeong27/Life_Alert_Bot/wiki/covid-19)

[날씨 기능 실행화면](https://github.com/jingyeong27/Life_Alert_Bot/wiki/weather)

[추천 옷차림 실행화면](https://github.com/jingyeong27/Life_Alert_Bot/wiki/clothes)

[뉴스 기능 실행화면](https://github.com/jingyeong27/Life_Alert_Bot/wiki/news)

### 개발할 때 참고한 사이트

●[코로나 일일, 평균 확진자](http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=)

●[코로나 누적 확진자](http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=)

●[날씨 정보](https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8)

●[뉴스 정보](https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%89%B4%EC%8A%A4)
