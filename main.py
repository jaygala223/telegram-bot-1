import os
import telebot
from newsapi.newsapi_client import NewsApiClient
import os
import datetime as dt
import pandas as pd
from keep_alive import keep_alive

NEWS_API = os.getenv('NEWS_API_KEY')

news_api = NewsApiClient(api_key=NEWS_API)

data = news_api.get_everything(q='(Indian Air Force) OR IAF',qintitle='Air Force', language='en')
print('hello')

articles = data['articles']

str = ""
cnt = 0
for x,y in enumerate(articles):
  if cnt == 6:
    break
  str += (f"""{x}    {y['title']}
Link: {y['url']}
        
        """)
  cnt += 1

print(str)


#bot code
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet', 'greet', 'start'])
def greet(message):
    bot.send_message(message.chat.id, "Hey aspiring IAF Officer!")

@bot.message_handler(commands=['Help', 'help'])
def help(message):
    bot.send_message(message.chat.id, """
Type /news to get the latest IAF news!
                     """)


@bot.message_handler(commands=['News', 'news'])
def news(message):
  data = news_api.get_everything(q="IAF", qintitle='Defence, air force', language='en', sort_by='relevancy', exclude_domains='archdaily.com')


  articles = data['articles']

  str = ""
  cnt = 0
  for x,y in enumerate(articles):
    if cnt == 5:
      break
    str += (f"""
{x+1}. {y['title']}
            
Link: {y['url']}
        
        """)
    cnt += 1

  #print(str)

  bot.send_message(message.chat.id, str)

keep_alive()
bot.polling()