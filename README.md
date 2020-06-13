Xbox-Discounting-Games(Python)
======
爬取Xbox Now网站上的游戏优惠信息
=====
简要思路：
------
1.用BeautifulSoup库解析网页<br>
2.构造三个分别获取游戏名、最低价服务器和最低价的函数<br>
3.用正则表达式筛选信息，并添加到相应列表<br>
4.将爬取的数据导入MySQL

完整代码如下
----
```python
from bs4 import BeautifulSoup
import requests
import re
import mysql.connector

gamelist,pricelist,countrylist,syntheize=[],[],[],[]
pattern = re.compile(
    r'欧洲|阿根廷|土耳其|印度|日本|墨西哥|韩国|丹麦|以色列|俄罗斯|加拿大|匈牙利|南非|台湾|哥伦比亚|奥地利|巴西|希腊|德国|意大利|挪威|捷克|斯洛伐克|新加坡|新西兰|智利|比利时|沙特|法国|波兰|澳大利亚|爱尔兰|瑞典|瑞士|美国|芬兰|英国|荷兰|葡萄牙|西班牙|阿拉伯|香港|中国')

for i in [i for i in range(1,6)]:
    url='https://www.xbox-now.com/zh/game-comparison?page='+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')

    for tag in soup.find_all('h5'):
        subTag=tag.find_all('span')
        game=str(subTag[0])[6:-7]
        gamelist.append(game)

    taglist=soup.find_all('span',text=re.compile('CNY'))[1:][1::2]
    for tag in taglist:
        price=re.findall(r'\d+\.\d* CNY',str(tag))
        pricelist.append(price[0])

    taglist=soup.find_all('span', text=pattern)[5:][1::2]
    for tag in taglist:
        country=re.findall(r'[\u4e00-\u9fa5]+',str(tag))
        countrylist.append(country[0])

for j in range(len(gamelist)):
    syntheize.append((gamelist[j],countrylist[j],pricelist[j]))

mydb = mysql.connector.connect(host="localhost",user="root",passwd="123456",database="zinc_db")
mycursor = mydb.cursor()
sql='INSERT INTO xboxnow (Name,Country,Price) VALUES (%s,%s,%s)'
val=syntheize
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "记录插入成功。")
```
结果展示
-----
```
1	Yes, Your Grace	阿根廷	24.64 CNY
2	Double Dragon 4	阿根廷	10.21 CNY
3	Radical Rabbit Stew	阿根廷	23.37 CNY
4	The Jackbox Party Trilogy 2.0	阿根廷	99.42 CNY
5	Horde Of Plenty	阿根廷	21.84 CNY
6	Glass Masquerade Double Pack	阿根廷	19.23 CNY
7	Tower of time	阿根廷	29.32 CNY
8	Spacejacked	阿根廷	11.60 CNY
9	Super Soccer Blast	阿根廷	11.74 CNY
10	Windbound Pre-Order	阿根廷	101.97 CNY
11	Hard West Ultimate Edition	阿根廷	23.19 CNY
12	Timberman VS	阿根廷	2.96 CNY
13	Pity Pit	阿根廷	5.72 CNY
14	Jump King	阿根廷	19.09 CNY
15	1971 Project Helios	阿根廷	58.59 CNY
16	Pathfinder: Kingmaker	阿根廷	146.89 CNY
17	Colt Canyon	阿根廷	21.84 CNY
18	Rock of Ages 3: Make &amp; Break Pre-Order Bundle	土耳其	139.22 CNY
19	极限竞速：地平线 4 与极限竞速：地平线 3 终极版捆绑包	阿根廷	85.71 CNY
20	Tcheco in the Castle of Lucio	阿根廷	7.15 CNY
21	Remnant: From the Ashes - Swamps of Corsus Bundle	土耳其	92.73 CNY
22	Waking (Xbox One)	阿根廷	28.99 CNY
23	Beyond Blue	阿根廷	28.99 CNY
24	Realpolitiks New Power	阿根廷	29.32 CNY
25	Strawberry Vinegar	阿根廷	11.60 CNY
26	Skelattack	土耳其	92.46 CNY
27	BioShock Infinite: The Complete Edition	印度	111.81 CNY
28	PONG Quest	阿根廷	21.84 CNY
29	BioShock 2 Remastered	印度	111.81 CNY
30	BioShock Remastered	印度	111.81 CNY
31	Decay Collection	阿根廷	21.84 CNY
32	Ultimate Fishing Simulator	阿根廷	43.79 CNY
33	Indiecalypse	阿根廷	16.22 CNY
34	Moonlighter: Complete Edition	阿根廷	35.11 CNY
35	WARBORN	阿根廷	29.32 CNY
36	BQM - BlockQuest Maker [COMPLETE EDITION]	阿根廷	36.64 CNY
37	Rigid Force Redux	阿根廷	28.99 CNY
38	Outbuddies DX	阿根廷	26.13 CNY
39	Borderlands Legendary Collection	土耳其	289.87 CNY
40	Shantae and the Seven Sirens	阿根廷	43.79 CNY
41	Goosebumps Dead of Night	阿根廷	58.59 CNY
42	Evan's Remains	阿根廷	10.21 CNY
43	黄泉ヲ裂ク華	日本	514.47 CNY
44	Atomicrops	阿根廷	21.84 CNY
45	Mortal Kombat 11: Aftermath Kollection	印度	326.30 CNY
46	Woodle Tree Bundle	阿根廷	21.84 CNY
47	ONE PIECE 海賊無双4	日本	565.92 CNY
48	Paladins Dragon Rider Pack	阿根廷	22.95 CNY
49	Castle Pals	阿根廷	7.15 CNY
50	Cyber Protocol	阿根廷	8.68 CNY
51	Many Faces: Console Edition	阿根廷	7.15 CNY
52	Warface: Breakout	阿根廷	28.99 CNY
53	Warface: Breakout – Deluxe Edition	阿根廷	43.79 CNY
54	Minecraft Dungeons ヒーローパス アップグレード	土耳其	29.87 CNY
55	Master of Survival bundle	阿根廷	36.64 CNY
56	Black Desert - Drieghan Companion Pack	韩国	135.31 CNY
57	Black Desert - Drieghan Companion Pack	墨西哥	120.34 CNY
58	Project Warlock	阿根廷	21.84 CNY
59	We Were Here Together	阿根廷	19.09 CNY
60	The Taller I Grow	阿根廷	7.15 CNY
61	Genetic Disaster	阿根廷	21.84 CNY
62	Hunting Simulator 2 Pre-Order	阿根廷	72.88 CNY
63	Hunting Simulator 2 - Bear Hunter Edition PreOrder	阿根廷	87.68 CNY
64	Shaolin vs Wutang	阿根廷	20.31 CNY
65	Concept Destruction	阿根廷	7.15 CNY
66	Awesome Pea 2	阿根廷	7.15 CNY
67	THE LAST SCAPE	阿根廷	8.68 CNY
68	Depth of Extinction	阿根廷	21.84 CNY
69	Mafia: Definitive Edition	巴西	231.78 CNY
70	Mafia III: Definitive Edition	巴西	175.57 CNY
71	Mafia Trilogy	巴西	351.21 CNY
72	Mafia II: Definitive Edition	巴西	175.57 CNY
73	World of Warships: Legends – Deutscher Stahl	阿根廷	72.88 CNY
74	Georifters	阿根廷	43.79 CNY
75	A Fold Apart	阿根廷	28.99 CNY
76	Bullet Beat	阿根廷	7.15 CNY
77	Golf With Your Friends	墨西哥	123.85 CNY
78	The LEGO® Games Bundle	巴西	560.65 CNY
79	EMMA: Lost in Memories	阿根廷	11.74 CNY
80	The Culling + Don't Die, Minerva! Bundle	土耳其	29.87 CNY
81	PGA TOUR 2K21 vorbestellen	巴西	351.21 CNY
82	Bestelle PGA TOUR 2K21 Digital Deluxe vor	巴西	407.42 CNY
83	Mecho Collection	阿根廷	10.21 CNY
84	Formula Retro Racing	阿根廷	17.56 CNY
85	Tacticool Champs	阿根廷	28.99 CNY
86	Little Misfortune	阿根廷	28.99 CNY
87	Bug Fables: The Everlasting Sapling	阿根廷	36.64 CNY
88	Those Who Remain	阿根廷	28.99 CNY
89	Super Mega Baseball 3	阿根廷	65.74 CNY
90	Portal Knights - legendäre Edition	阿根廷	43.79 CNY
91	Divinity: Original Sin - The Source Saga	阿根廷	87.68 CNY
92	Deep Rock Galactic - Deluxe Edition	阿根廷	58.59 CNY
93	Deep Rock Galactic - Ultimate Edition	阿根廷	72.88 CNY
94	Thy Sword	阿根廷	14.49 CNY
95	Tony Hawk's™ Pro Skater™ 1 + 2	阿根廷	216.29 CNY
96	Tony Hawk's™ Pro Skater™ 1 + 2 - Digital Deluxe Edition	阿根廷	229.56 CNY
97	Island Saver	中国	0.00 CNY
98	Demon's Tier+	阿根廷	14.49 CNY
99	Tour de France 2020	阿根廷	71.35 CNY
100	Wer weiß denn sowas? Complete Edition	瑞士	420.25 CNY
```
