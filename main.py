import urllib.request as req
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from bs4 import BeautifulSoup
import os
import re

Corona_url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
Corona_url1= 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='
Wt = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'


def _manual():
    f = open("Corona_manual.txt", 'r')
    data = f.read()
    return data


token = os.environ.get('token',"5322770624:AAGDUuFm7k50OHxwzfif3SqJuWv3dAN7GVc")    # 토큰 넣기
id = 5316579447                  # chat_id
bot = telegram.Bot(token)

info_message = '* 생활 정보 알림이에 오신 것을 환영합니다.\n'\
               '* 필요한 정보를 입력해주세요.\n'\
               '* 메뉴 : 생활 정보 알림이 명령어 다시 보기 🙏 \n' \
               '* 코로나  : 일일 확진자, 7일 평균 확진자, 누적 확진자 수 ☠\n '\
                '* 코로나지침 : 최근 코로나 방역지침 📖 \n '\
                '* 나의날씨 : 자신의 현재위치를 기반으로한 날씨 정보 ☁  '

bot.sendMessage(chat_id=id, text=info_message)      # 봇이 시작될 때 출력

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장
    if (user_text == "코로나"):        #일일 확진자수 '코로나'를 입력시 웹크롤링
        code = req.urlopen(Corona_url)
        soup = BeautifulSoup(code, "html.parser")
        info_day = soup.select_one("#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(1) > dl > dd").string
        re.sub('<[^<]+?>', '', info_day)
        info_avg = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(9)').string
        re.sub('<[^<]+?>', '', info_avg)
        code1 = req.urlopen((Corona_url1))
        soup = BeautifulSoup(code1, "html.parser")
        info_total = soup.select_one('#mapAll > div > ul > li:nth-child(5) > div:nth-child(2) > span').string
        re.sub('<[^<]+?>', '', info_total)
        bot.send_message(chat_id=id, text="오늘 확진자 수 :"+ str(info_day) + " 명"+ "\n" + "7일 평균 확진자 수 : " + str(info_avg) + " 명"+ "\n"+ "현재 누적 확진자 수 :{} 명".format(info_total))

    elif (user_text == "코로나지침"):
        covid_man = _manual()
        bot.send_message(chat_id=id, text=covid_man)

    elif (user_text == "메뉴"):
        bot.sendMessage(chat_id=id, text=info_message)

    elif (user_text == "나의날씨"):
        code_mywt = req.urlopen(Wt)
        soup = BeautifulSoup(code_mywt, "html.parser")
        my_adr = soup.select_one("#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.top_wrap > div.title_area._area_panel > h2.title").string
        re.sub('<[^<]+?>', '', my_adr)
        my_tem = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong').text
        my_wea = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.weather_main > i > span').string
        re.sub('<[^<]+?>', '', my_wea)
        bot.send_message(chat_id = id, text = "현재 위치 : " + str(my_adr) + "\n" + str(my_tem) + "\n날씨 : " + str(my_wea))

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
