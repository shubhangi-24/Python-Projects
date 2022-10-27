
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("News for today...Let's begin")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=7432d901e31347d0af154f20b1709174"
    news=requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])  
    arts= news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news..Listen carefully") 