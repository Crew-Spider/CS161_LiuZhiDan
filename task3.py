#coding: UTF-8
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
base_url="https://www.thebump.com/real-answers/v1/categories/33/questions"
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0','authority':'securepubads.g.doubleclick.net','method':'GET','path':'/gampad/ads?gdfp_req=1&correlator=4366897610693029&output=json_html&callback=googletag.impl.pubads.callbackProxy21&impl=fif&eid=21060617%2C21061301%2C21061871&vrg=205&guci=2.2.0.0.2.2&sc=1&sfv=1-0-23&iu=%2F4879%2Fki.tb.realanswers%2Fmain&sz=300x250%7C640x480&rc=5&scp=pos%3Dinfeed9%26category%3DFirst%2520Trimester%26topics%3D&eri=33&cookie=ID%3D4f30bc9ca5447d84%3AT%3D1525962811%3AS%3DALNI_MbbYqjbdhUOT7Y2ej2-HsGZBJFhYQ&bc=5&abxe=1&lmt=1526523353&dt=1526523353660&frm=20&biw=967&bih=849&oid=3&adx=420&ady=12700&adk=1612682022&gut=v2&ifi=21&u_tz=480&u_his=6&u_h=1080&u_w=1920&u_ah=1030&u_aw=1920&u_cd=24&u_nplug=36&u_nmime=62&u_sd=1&flash=22.0.0&url=https%3A%2F%2Fwww.thebump.com%2Freal-answers%2Fstages%2Ffirst-trimester%23backPage%3D3&ref=https%3A%2F%2Fwww.thebump.com%2Freal-answers%2Fstages&dssz=21&icsg=10494655&std=0&vis=1&scr_x=0&scr_y=12676&psz=740x270&ga_vid=1015401143.1526109654&ga_sid=1526479745&ga_hid=1098733311','scheme':'https','origin':'https://www.thebump.com','referer':'https://www.thebump.com/real-answers/stages/first-trimester','accept':'*/*','accept-encoding':'gzip, deflate, sdch','accept-language':'zh-CN,zh;q=0.8','cookie':'id=22d8770ad30a0069||t=1474362697|et=730|cs=002213fd483d76c087c6db5617'}
param={'filter':'ranking','page_num':1,'page_size':10}
r=requests.get(base_url,params=param,headers=header).json()
# 得到总size
total=r["total"]
rows=[]

#通过“页数增加”来爬取，一次爬取30条，直到爬完
while True:
    for l in r["questions"]:
        row=(l["title"].replace("\n"," "),l["created_at"],l["user_id"],l["user"]["username"],"PREGNANCY","FIRST TRIMESTER")
        rows.append(row)
    total -= 30
    if (total > 0):
        param["page_num"] += 1
        r = requests.get(base_url, params=param,headers=header).json()
    else:
        break
f=open('result.csv','w',newline='',encoding='utf-8')
writer = csv.writer(f)
writer.writerow(['title', 'created_at', 'user_id','username','category_name','subcategory_name'])
writer.writerows(rows)