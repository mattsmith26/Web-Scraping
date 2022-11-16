import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://ebible.org/asv/JHN'
random_chapter = random.randint(1,21)
if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)
webpage = webpage + random_chapter + '.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

page_verses = soup.findAll('div', class_='main')

for verse in page_verses:
    verse_list = verse.text.split('.')

myverse = random.choice(verse_list[:-5])

message = "Chapter:" + random_chapter + " Verse:" + myverse

print(message)

import keys2
from twilio.rest import CLient
client = Client(keys2.AccountSID, keys2.authToken)

TwilioNumber = "+18087551629"

myCellPhone = "+9495420598"

textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber,
                    body= "you just got an email professor Bhojwani")

print(textmessage.status)