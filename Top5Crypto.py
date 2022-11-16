from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

url = 'https://www.investing.com/crypto/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
table_rows = soup.findAll("tr")

for row in table_rows[1:6]:
    cells = row.findAll("td")
    name = (cells[2].text.strip())
    symbol = (cells[3].text.strip())
    current_price = (cells[4].text)
    daily_change = (cells[8].text.strip())
    current_price2 = float(cells[4].text.replace(",",""))
    daily_change2 = float(cells[8].text.replace("+","").replace("%","")) / 100
    changed_price = round((current_price2+(current_price2 * daily_change2)),4)

    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Current Price: ${current_price}")
    print(f"24 Hour Price Change (%): {daily_change}")
    print(f"Daily Adjusted Price: ${changed_price}")
    print()
    print()
    input()

#Text Message Section
import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+18087551629"
myCellPhone = "+9495420598"

for row in table_rows[1:6]:
    td = row.findAll("td")
    name = (td[2].text.strip())
    current_price2 = float(td[4].text.replace(",",""))
    if name == "Bitcoin" and current_price2 < 40000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="BTC is below $40,000")

    if name == "Ethereum" and current_price2 < 3000:
        textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body="ETH is below $3,000")



