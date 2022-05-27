import os
import telebot
from newsapi.newsapi_client import NewsApiClient
import os
import datetime as dt
import pandas as pd
from keep_alive import keep_alive
import random

NEWS_API = os.getenv('NEWS_API_KEY')

news_api = NewsApiClient(api_key=NEWS_API)

#bot code
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet', 'greet', 'start'])
def greet(message):
    bot.send_message(message.chat.id, "Hey aspiring IAF Officer!")

@bot.message_handler(commands=['Help', 'help'])
def help(message):
    bot.send_message(message.chat.id, """
Type /help to get help.
Type /greet to display the welcome message.
Type /news to get the latest IAF news!
                     """)


@bot.message_handler(commands=['News', 'news'])
def news(message):
  data = news_api.get_everything(q="IAF", qintitle='Defence, air force', language='en', sort_by='relevancy', exclude_domains='archdaily.com')


  articles = data['articles']

  str = ""
  for i in range(1, 6):
    random_index = random.randint(0, len(articles)-1)

    str += (f"""
{i}. {articles[random_index]['title']}
            
Link: {articles[random_index]['url']}
        
        """)
  bot.send_message(message.chat.id, str)

keep_alive()
bot.polling()