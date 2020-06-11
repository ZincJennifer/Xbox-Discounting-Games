Xbox-Discounting-Games(Python)
======
爬取Xbox Now网站上的游戏优惠信息
=====
简要思路：
------
1.用BeautifulSoup库解析网页<br>
2.构造三个分别获取游戏名、最低价服务器和最低价的函数<br>
3.用正则表达式筛选信息，并添加到相应列表<br>
4.利用prettytable库将列表转换成表格

完整代码如下
----
```python
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
    
```
结果展示
-----
```
+------------------------------------------------------+------------+------------+
|                         游戏                         | 最低价国家 |   最低价   |
+------------------------------------------------------+------------+------------+
|                 Windbound Pre-Order                  |   阿根廷   | 102.02 CNY |
|              Hard West Ultimate Edition              |   阿根廷   | 23.20 CNY  |
|                     Timberman VS                     |   阿根廷   |  2.96 CNY  |
|                       Pity Pit                       |   阿根廷   |  5.72 CNY  |
|                      Jump King                       |   阿根廷   | 19.10 CNY  |
|                 1971 Project Helios                  |   阿根廷   | 58.62 CNY  |
|                Pathfinder: Kingmaker                 |   阿根廷   | 146.96 CNY |
|                     Colt Canyon                      |   阿根廷   | 21.85 CNY  |
|  Rock of Ages 3: Make &amp; Break Pre-Order Bundle   |   土耳其   | 139.68 CNY |
| 极限竞速：地平线 4 与极限竞速：地平线 3 终极版捆绑包 |   阿根廷   | 85.75 CNY  |
|            Tcheco in the Castle of Lucio             |   阿根廷   |  7.15 CNY  |
|  Remnant: From the Ashes - Swamps of Corsus Bundle   |   土耳其   | 93.03 CNY  |
|                  Waking (Xbox One)                   |   阿根廷   | 29.00 CNY  |
|                     Beyond Blue                      |   阿根廷   | 29.00 CNY  |
|                Realpolitiks New Power                |   阿根廷   | 29.33 CNY  |
|                  Strawberry Vinegar                  |   阿根廷   | 11.60 CNY  |
|                      Skelattack                      |   土耳其   | 92.76 CNY  |
|       BioShock Infinite: The Complete Edition        |    印度    | 111.85 CNY |
|                      PONG Quest                      |   阿根廷   | 21.85 CNY  |
|                BioShock 2 Remastered                 |    印度    | 111.85 CNY |
+------------------------------------------------------+------------+------------+
+-------------------------------------------+------------+------------+
|                    游戏                   | 最低价国家 |   最低价   |
+-------------------------------------------+------------+------------+
|            BioShock Remastered            |    印度    | 111.85 CNY |
|              Decay Collection             |   阿根廷   | 21.85 CNY  |
|         Ultimate Fishing Simulator        |   阿根廷   | 43.81 CNY  |
|                Indiecalypse               |   阿根廷   | 16.23 CNY  |
|       Moonlighter: Complete Edition       |   阿根廷   | 35.13 CNY  |
|                  WARBORN                  |   阿根廷   | 29.33 CNY  |
| BQM - BlockQuest Maker [COMPLETE EDITION] |   阿根廷   | 36.66 CNY  |
|             Rigid Force Redux             |   阿根廷   | 29.00 CNY  |
|               Outbuddies DX               |   阿根廷   | 26.14 CNY  |
|      Borderlands Legendary Collection     |   土耳其   | 290.84 CNY |
|        Shantae and the Seven Sirens       |   阿根廷   | 43.81 CNY  |
|          Goosebumps Dead of Night         |   阿根廷   | 58.62 CNY  |
|               Evan's Remains              |   阿根廷   | 10.21 CNY  |
|                黄泉ヲ裂ク華               |    日本    | 515.05 CNY |
|                 Atomicrops                |   阿根廷   | 21.85 CNY  |
|   Mortal Kombat 11: Aftermath Kollection  |    印度    | 326.42 CNY |
|             Woodle Tree Bundle            |   阿根廷   | 21.85 CNY  |
|            ONE PIECE 海賊無双4            |    日本    | 566.56 CNY |
|         Paladins Dragon Rider Pack        |   阿根廷   | 22.96 CNY  |
|                Castle Pals                |   阿根廷   |  7.15 CNY  |
+-------------------------------------------+------------+------------+
+----------------------------------------------------+------------+------------+
|                        游戏                        | 最低价国家 |   最低价   |
+----------------------------------------------------+------------+------------+
|                   Cyber Protocol                   |   阿根廷   |  8.68 CNY  |
|            Many Faces: Console Edition             |   阿根廷   |  5.72 CNY  |
|                 Warface: Breakout                  |   阿根廷   | 29.00 CNY  |
|         Warface: Breakout – Deluxe Edition         |   阿根廷   | 43.81 CNY  |
|        Minecraft Dungeons Hero Pass Upgrade        |   土耳其   | 29.97 CNY  |
|             Master of Survival bundle              |   阿根廷   | 36.66 CNY  |
|       Black Desert - Drieghan Companion Pack       |    韩国    | 136.04 CNY |
|       Black Desert - Drieghan Companion Pack       |   墨西哥   | 120.44 CNY |
|                  Project Warlock                   |   阿根廷   | 21.85 CNY  |
|               We Were Here Together                |   阿根廷   | 19.10 CNY  |
|                 The Taller I Grow                  |   阿根廷   |  7.15 CNY  |
|                  Genetic Disaster                  |   阿根廷   | 21.85 CNY  |
|           Hunting Simulator 2 Pre-Order            |   阿根廷   | 72.92 CNY  |
| Hunting Simulator 2 - Bear Hunter Edition PreOrder |   阿根廷   | 87.72 CNY  |
|                 Shaolin vs Wutang                  |   阿根廷   | 20.32 CNY  |
|                Concept Destruction                 |   阿根廷   |  7.15 CNY  |
|                   Awesome Pea 2                    |   阿根廷   |  7.15 CNY  |
|                   THE LAST SCAPE                   |   阿根廷   |  8.68 CNY  |
|                Depth of Extinction                 |   阿根廷   | 21.85 CNY  |
|             Mafia: Definitive Edition              |    印度    | 233.13 CNY |
+----------------------------------------------------+------------+------------+
```
