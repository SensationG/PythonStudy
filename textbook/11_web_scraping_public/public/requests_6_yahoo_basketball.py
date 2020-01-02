#! python3
# lucky.py - Opens several Google search results.
#-----------------------------爬取yahoo篮球模块--待后期处理----------------------
import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlsplit

print('Crawling Yahoo Basketball News...') # display text while downloading the Google page

#-------------------------url处理---------------------------
base_url = 'https://tw.news.yahoo.com/basketball'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}

# Download the raw CA Bundle at https://certifi.io/en/latest/
# cert_path = "C:/Users/Public/drivers/certs.pem"

r = requests.get(base_url, verify=False, headers=headers)

#print(r.raise_for_status())
#print(r.status_code)

#--------------------------内容处理--------------------------
# Get crawling results 
soup = BeautifulSoup(r.text, 'html.parser')
#爬head title标题
page_title = soup.select('head > title')[0].text
print("\n----" + page_title + "----\n")

# Retrieve top ten search result links.
#linkElems = soup.select('li.js-stream-content.Pos\(r\) a.C\(\$c-fuji-grey-l\)')
#爬取文章title
linkElems = soup.select('li[class*="js-stream-content"] a[class*="fuji-grey-l"]') # <a> tag under "li"
print(len(linkElems)) #爬取的数量
numOpen = min(20, len(linkElems)) #限制20个或者网页最大文章量

#剔除广告网址
bad_urls = ['http://help.yahoo.com', 'https://info.yahoo.com', 'https://beap.gemini.yahoo.com', 'https://twhbl.yahoo.com.tw']
#选取内容
nba_words = ['nba', 'NBA', '勇士', '湖人']

for i in range(numOpen):
    title = linkElems[i].getText()
    link = linkElems[i].get('href') # get url from <href> tag
    link = unquote(link) #把 % 開頭的16進位網址轉換為正常文字
    
    #print("原始的link: " + link + "\n")
    if link.startswith('http'): #link的开头以http
        # https://info.yahoo.com/privacy/tw/yahoo/relevantads.html
        # link.find(".com"): index of .com
        if ".com.tw" in link: # 字符串是否包含".com.tw"
            baseurl = link[0:link.find(".com.tw")+7] #这是一段长度
        else: # .com
            baseurl = link[0:link.find(".com")+4]
        # baseurl = "{0.scheme}://{0.netloc}".format(urlsplit(link))
        # print(baseurl)
        if baseurl not in bad_urls:
            siteurl = link
        else:
            # print("bad url: ", baseurl)
            continue
    # /nba-戈貝爾開賽三分鐘爆氣被趕出場-回到健身房繼續訓練-082252250.html
    # /勇士半場變4打5，場均三分外線17中1成進攻漏洞
    elif any(w in link for w in nba_words):
        print(title)
        print("處理過link: " + link)
        siteurl = 'https://tw.news.yahoo.com' + link
    else: 
        continue
    
    # Open a browser tab for each result.
    #webbrowser.open_new(siteurl)
    
    print("處理過link: " + unquote(siteurl))
    print()
    
    
    