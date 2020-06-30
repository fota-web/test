import requests 
from bs4 import BeautifulSoup
import pandas as pd
 
url = 'https://news.google.com/search?q=%E9%9F%93%E5%9C%8B%E7%91%9C&hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
r = requests.get(url)
web_content = r.text
soup = BeautifulSoup(web_content,'lxml')

title = soup.find_all('div', class_='xrnccd')
# print(title)

titles = [t.find('span').text for t in title]
# print(titles)

newUrls = [requests.get(t.find('a')['href'].replace('.','https://news.google.com',1)).url for t in title]
# print(newUrls)

df = pd.DataFrame(
{
    'title': titles,
    'links': newUrls
})

# print(df)

