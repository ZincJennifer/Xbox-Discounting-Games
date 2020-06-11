from bs4 import BeautifulSoup
import requests
import re
from prettytable import PrettyTable

for i in [i for i in range(1,11)]:
    url='https://www.xbox-now.com/zh/game-comparison?page='+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')

    def getGameName():
        gamelist=[]
        for tag in soup.find_all('h5'):
            subTag=tag.find_all('span')
            game=str(subTag[0])[6:-7]
            gamelist.append(game)
        return gamelist

    def getPrice():
        taglist=soup.find_all('span',text=re.compile('CNY'))[1:][1::2]
        pricelist=[]
        for tag in taglist:
            price=re.findall(r'\d+\.\d* CNY',str(tag))
            pricelist.append(price[0])
        return pricelist

    def getCountry():
        pattern = re.compile(r'欧洲|阿根廷|土耳其|印度|日本|墨西哥|韩国|丹麦|以色列|俄罗斯|加拿大|匈牙利|南非|台湾|哥伦比亚|奥地利|巴西|希腊|德国|意大利|挪威|捷克|斯洛伐克|新加坡|新西兰|智利|比利时|沙特|法国|波兰|澳大利亚|爱尔兰|瑞典|瑞士|美国|芬兰|英国|荷兰|葡萄牙|西班牙|阿拉伯|香港|中国')
        taglist=soup.find_all('span', text=pattern)[5:][1::2]
        countrylist=[]
        for tag in taglist:
            country=re.findall(r'[\u4e00-\u9fa5]+',str(tag))
            countrylist.append(country[0])
        return countrylist

    def main():
        header=PrettyTable()
        header.add_column('游戏',getGameName())
        header.add_column('最低价国家',getCountry())
        header.add_column('最低价',getPrice())
        return header

    print(main())