import urllib.request as req
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from bs4 import BeautifulSoup
import os

Corona_url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='

def _day():
    code = req.urlopen(Corona_url)
    soup= BeautifulSoup(code, "html.parser")
    info_day = soup.select("#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(1) > dl > dd")
    day_result = info_day[0].string
    return day_result       # 일일 확진자수 결과를 return

def _avg():
    code_avg = req.urlopen(Corona_url)
    soup = BeautifulSoup(code_avg, "html.parser")
    info_avg = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(9)')
    return info_avg.string      # 7일 평균 확진자수 결과를 return

token = os.environ.get('token',"5322770624:AAGDUuFm7k50OHxwzfif3SqJuWv3dAN7GVc")    # 토큰 넣기
id = 5316579447                   # chat_id
bot = telegram.Bot(token)

info_message = '* 생활 정보 알림이에 오신 것을 환영합니다.\n'\
               '* 필요한 정보를 입력해주세요.\n'\
               '* 코로나  : 일일 코로나 확진자 수 * \n' \
                '* 평균확진자  : 7일 평균 확진자 수 *'


bot.sendMessage(chat_id=id, text=info_message)      # 봇이 시작될 때 출력

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text # 사용자가 보낸 메세지를 user_text 변수에 저장
    if (user_text == "코로나"):        #일일 확진자수 '코로나'를 입력시 웹크롤링
        covid_num = _day()
        bot.send_message(chat_id=id, text="오늘 확진자 수 : {} 명".format(covid_num))

    elif (user_text == "평균확진자"):    #평균 확진자수 '평균확진자'를 입력시 웹크롤링
        covid_avg = _avg()
        bot.send_message(chat_id=id, text = "7일 평균 확진자 수 : {} 명".format(covid_avg))


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
