# - Life_Alert_Bot
## 코로나, 날씨, 최신 뉴스 정보를 웹크롤링으로 데이터를 추출하여 출력하게하는 텔레그램 챗봇
### Life_Alert_Bot 텔레그램 봇 기능
1. Covid-19 기능 : 코로나 19 일일, 평균, 누적 확진자 수를 출력
2. 나의 위치 날씨, 전국의 날씨 기능 : 자신의 위치를 기반으로 날씨 출력, 전국 날씨 링크 연결
3. 최신 뉴스 기능 : 최신 뉴스를 랜덤으로 불러옴

## 챗봇을 실행하기 위한 환경 설정

token = os.environ.get('token',"이곳에 토큰을 넣어주세요") 

id = 'chat_id'  

![챗봇과 연결하기](https://user-images.githubusercontent.com/102271635/169682805-a162964a-2064-4ec5-964c-ea21a9f8a51c.png)


## 개발할 때 참고한 사이트
[코로나 일일, 평균 확진자](http://ncov.mohw.go.kr/bdBoardList_Real.dobrdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=)

[코로나 누적 확진자](http://ncov.mohw.go.kr/bdBoardList_Real.dobrdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=)

[날씨 정보](https://search.naver.com/search.naverwhere=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8)
