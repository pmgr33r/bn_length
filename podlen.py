from pyPodcastParser.Podcast import Podcast
import requests
from datetime import datetime

def ConvertSectoDay(n): 
  
    day = n // (24 * 3600) 
  
    n = n % (24 * 3600) 
    hour = n // 3600
  
    n %= 3600
    minutes = n // 60
  
    n %= 60
    seconds = n 
      
    print(day,"days", hour, "hours",  
          minutes, "minutes", 
          seconds, "seconds\n") 

totalTime = 0
response = requests.get('https://feeds.megaphone.fm/thesession')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items: 
    sumSession += int(x.itunes_duration)
print("The Session: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

totalTime += sumSession

response = requests.get('https://feeds.megaphone.fm/sourhour')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items: 
    sumSession += int(x.itunes_duration)
print("The Sour Hour: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

totalTime += sumSession

response = requests.get('https://feeds.megaphone.fm/drhomebrew')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items: 
    sumSession += int(x.itunes_duration)
print("Dr. Homebrew: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

totalTime += sumSession

response = requests.get('https://feeds.megaphone.fm/brewstrong')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items: 
    sumSession += int(x.itunes_duration)
print("Brew Strong: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

totalTime += sumSession

response = requests.get('https://feeds.megaphone.fm/jamilshow')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items: 
    sumSession += int(x.itunes_duration)
print("Jamil Show: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

totalTime += sumSession

response = requests.get('http://thebrewingnetwork.com/homebrewedchef.xml')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items:
    try:
        h, m, s = x.itunes_duration.split(':')
        totalSeconds = int(h)*3600 + int(m) * 60 + int(s)
        sumSession += totalSeconds
    except ValueError:
        print("Oops")
print("Homebrew Chef: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

totalTime += sumSession

response = requests.get('http://thebrewingnetwork.com/lunchmeet.xml')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items:
    try:
        h, m, s = x.itunes_duration.split(':')
        totalSeconds = int(h)*3600 + int(m) * 60 + int(s)
        sumSession += totalSeconds
    except ValueError:
        try:
            m, s = x.itunes_duration.split(':')
            totalSeconds = int(m) * 60 + int(s)
            sumSession += totalSeconds
        except ValueError:
            print("Oops")
print("LUNCH MEET!!!!: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

totalTime += sumSession

response = requests.get('https://feeds.megaphone.fm/headsandtails')
podcast = Podcast(response.content)
sumSession = 0
for x in podcast.items:
    sumSession += int(x.itunes_duration)
print("Heads + Talis: " + str(sumSession) + " Seconds or ") 
ConvertSectoDay(sumSession)

print("Total Shows: " + str(totalTime) + " Seconds or ") 
ConvertSectoDay(totalTime)