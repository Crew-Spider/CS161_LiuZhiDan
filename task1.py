#发现链接地址和新闻标题都存在于c-title的这种<h3>里
#再进一步看，链接地址存在于<a>的href属性里，标题存在于text里
#新闻事件存在于c-author的这种<p>的text里
from bs4 import BeautifulSoup
#from urllib.request import urlopen
import requests
base_url="http://news.baidu.com/ns?cl=2&rn=20&tn=news&word=%E4%B8%8A%E6%B5%B7%E6%B5%B7%E4%BA%8B%E5%A4%A7%E5%AD%A6"
html=requests.get(base_url).text
soup=BeautifulSoup(html,features='html.parser')
href_ul=soup.find_all('h3',{"class":"c-title"})
time_ul=soup.find_all('p',{"class":"c-author"})
for ul in href_ul:    
    hs=ul.find_all('a')
    for h in hs:
        title=h.text
        print(“新闻标题：”,title)
for ul in href_ul:    
    hs=ul.find_all('a')
    for h in hs:
        url=h['href']
        print(“ 新闻链接：”,url)
for times in time_ul:    
    time=times.text
    print(“ 新闻时间：”,time)