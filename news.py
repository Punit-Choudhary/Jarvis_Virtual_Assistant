''' This module provide news headlines. '''

import requests
import json
import os
from dotenv import load_dotenv

import voice

load_dotenv()

api_key = os.getenv('NEWS_KEY')  # Add your News API key here

url = "http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=" + api_key
news = requests.get(url).text
news_dict = json.loads(news)

if news_dict['status'] == 'ok':
    articles = news_dict['articles']
    
    voice.speak("From source : The Times of India")
    voice.speak("Todays news Headlines are...")

    for index, article in enumerate(articles):
        voice.speak(article['title'])

        if index == len(articles) - 1:
            break
        voice.speak("Moving to the next news headline..")
    voice.speak("These were top news headlines from The Times of India..")
    voice.speak("Have a nice day sir!")
else:
    voice.speak("Sorry, i couldn't able to fetch news headlines.")
