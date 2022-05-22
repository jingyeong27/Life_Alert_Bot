import urllib.request as req

import requests
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from bs4 import BeautifulSoup
import os

Corona_url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
Corona_url1 = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='

def _day():
    code = req.urlopen(Corona_url)
    soup = BeautifulSoup(code, "html.parser")
    info_day = soup.select("#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(1) > dl > dd")
    day_result = info_day[0].string
    return day_result  # 일일 확진자수 결과를 return


def _avg():
    code_avg = req.urlopen(Corona_url)
    soup = BeautifulSoup(code_avg, "html.parser")
    info_avg = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(9)')
    return info_avg.string  # 7일 평균 확진자수 결과를 return


def _total():
    code_total = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_total, "html.parser")
    info_total = soup.select_one('.total > li:nth-child(5) > div:nth-child(2) > span:nth-child(1)')
    return info_total.string


def _seoul():
    code_seoul = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_seoul, "html.parser")
    info_seoul = soup.select_one('#main_maplayout > button:nth-child(1) > span:nth-child(2)')
    return info_seoul.string


def _daegu():
    code_daegu = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_daegu, "html.parser")
    info_daegu = soup.select_one('#main_maplayout > button:nth-child(3) > span:nth-child(2)')
    return info_daegu.string


def _busan():
    code_busan = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_busan, "html.parser")
    info_busan = soup.select_one('#main_maplayout > button:nth-child(2) > span:nth-child(2)')
    return info_busan.string


def _incheon():
    code_incheon = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_incheon, "html.parser")
    info_incheon = soup.select_one('#main_maplayout > button:nth-child(4) > span:nth-child(2)')
    return info_incheon.string


def _gwangju():
    code_gwangju = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_gwangju, "html.parser")
    info_gwangju = soup.select_one('#main_maplayout > button:nth-child(5) > span:nth-child(2)')
    return info_gwangju.string


def _ulsan():
    code_ulsan = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_ulsan, "html.parser")
    info_ulsan = soup.select_one('#main_maplayout > button:nth-child(7) > span:nth-child(2)')
    return info_ulsan.string


def _jeju():
    code_jeju = req.urlopen(Corona_url1)
    soup = BeautifulSoup(code_jeju, "html.parser")
    info_jeju = soup.select_one('#main_maplayout > button:nth-child(17) > span:nth-child(2)')
    return info_jeju.string

def _clothes():
    f = open('Clothes.txt', 'r')
    data = f.read()
    return data

old_link=[]
def _news(old_link=[]):
    News_url = 'https://search.naver.com/search.naver?where=news&query=%EB%89%B4%EC%8A%A4&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0'
    req = requests.get(News_url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    total_search = soup.select_one('section.sc_new:nth-child(7) > div:nth-child(1)')
    news_list = total_search.select('#sp_nws1 > div:nth-child(1) > div:nth-child(1) > a:nth-child(2)')

    links = []
    for news in news_list[:5]:
        link = news['href']
        links.append(link)
    new_links = []
    for link in links:
        if link not in old_link:
            new_links.append(link)
    return new_links

def _unknown():
    return('해당 명령은 존재하지 않습니다 😓')

city_comment="서울,대구,인천,부산,광주,울산,제주 중에서 \n알고 싶은 도시를 알려주세요"

token = os.environ.get('token', "5396200298:AAEhrqPUg_VX5UoRzuImCNoyhDE_i4nLgKQ")  # 토큰 넣기
id = 5054586086  # chat_id
bot = telegram.Bot(token)

info_message = '* 생활 정보 알림이에 오신 것을 환영합니다.\n' \
               '* 필요한 정보를 입력해주세요.\n' \
               '* 코로나  : 일일 코로나 확진자 수 \n' \
               '* 평균확진자  : 7일 평균 확진자 수 \n' \
               '* 누적확진자 : 현재까지의 누적 확진자 수 \n' \
               '* 도시별확진자 : 각 도시의 확진자 수 \n'\
               '* 기온별옷차림 : 기온별로 적당한 옷차림 추천 \n' \
               '* 전국날씨 : 각 지역의 날씨 정보 \n' \
               '* 최신뉴스 : 가장 최근에 올라온 뉴스 확인'

bot.sendMessage(chat_id=id, text=info_message)  # 봇이 시작될 때 출력

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장
    if (user_text == "코로나"):  # 일일 확진자수 '코로나'를 입력시 웹크롤링
        covid_num = _day()
        bot.send_message(chat_id=id, text="오늘 확진자 수 : {} 명".format(covid_num))

    elif (user_text == "평균확진자"):  # 평균 확진자수 '평균확진자'를 입력시 웹크롤링
        covid_avg = _avg()
        bot.send_message(chat_id=id, text="7일 평균 확진자 수 : {} 명".format(covid_avg))

    elif (user_text == "누적확진자"):
        covid_total = _total()
        bot.send_message(chat_id=id, text="현재까지의 누적 확진자 수 : {} 명".format(covid_total))

    elif (user_text == "도시별확진자"):
        bot.send_message(chat_id=id, text=city_comment)

    elif (user_text == "서울"):
        covid_seoul = _seoul()
        bot.send_message(chat_id=id, text="서울의 누적 확진자 수 : {} 명".format(covid_seoul))

    elif (user_text == "대구"):
        covid_daegu = _daegu()
        bot.send_message(chat_id=id, text="대구의 누적 확진자 수: {} 명".format(covid_daegu))

    elif (user_text == "부산"):
        covid_busan = _busan()
        bot.send_message(chat_id=id, text="부산의 누적 확진자 수: {} 명".format(covid_busan))

    elif (user_text == "인천"):
        covid_incheon = _incheon()
        bot.send_message(chat_id=id, text="인천의 누적 확진자 수: {} 명".format(covid_incheon))

    elif (user_text == "광주"):
        covid_gwangju = _gwangju()
        bot.send_message(chat_id=id, text="광주의 누적 확진자 수: {} 명".format(covid_gwangju))

    elif (user_text == "울산"):
        covid_ulsan = _ulsan()
        bot.send_message(chat_id=id, text="울산의 누적 확진자 수: {} 명".format(covid_ulsan))

    elif (user_text == "제주"):
        covid_jeju = _jeju()
        bot.send_message(chat_id=id, text="제주의 누적 확진자 수: {} 명".format(covid_jeju))

    elif (user_text == "기온별옷차림"):
        temp_clothes = _clothes()
        bot.send_message(chat_id=id, text=temp_clothes)

    elif (user_text == "전국날씨"):
        bot.send_message(chat_id=id, text = "[전국의 날씨 정보(√클릭)](https://www.weather.go.kr/w/weather/forecast/short-term.do)",parse_mode='Markdown')

    elif (user_text == "최신뉴스"):
        recent_news = _news()
        bot.send_message(chat_id=id, text=recent_news)

    else:
        unknown_command = _unknown()
        bot.send_message(chat_id=id, text=unknown_command)

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
