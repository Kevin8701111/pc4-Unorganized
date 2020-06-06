import requests

homepage = requests.get('https://www.ptt.cc/bbs/hotboards.html')
# print(homepage)
from bs4 import BeautifulSoup

# with open ('ppt_hotboards_homepage1.html','a') as f:
#     f.write(homepage.text)
soup = BeautifulSoup(homepage.text,'lxml')
# print(soup)
# with open ('b.text','a') as f:
#     f.write(soup.text)

# posts11 = soup.find('a', class_= 'board')
# posts12 = soup.select_one('a.board')
# print(posts11)
# print('---')
# print(posts12)

board_find = soup.find_all('a', class_= 'board')
board_select = soup.select('a.board')

for board in board_select:
    h_name = board.find('div', class_= 'board-name')
    print('===========================================')
    print(h_name.text)
    h_page = board.select('span')[0]
    print(h_page.text)
    h_classname = board.select('div.board-class')[0]
    print(h_classname.text)
    h_title = board.select('div.board-title')[0]
    print(h_title.text)
    h_url = 'https://www.ptt.cc' + board['href']
    print(h_url)
    article = requests.get(
            url = h_url,
            cookies = {'over18': 'yes'}  # ptt18歲的認證
        )
    soup = BeautifulSoup(article.text,'lxml')
    r_ent = soup.select('div.r-ent')[0].text
    a_url = soup.select('div.title > a')[0]['href']
    a_title = soup.select('div.title')[0].text
    print(a_title)
    a_author = soup.select('div.author')[0].text
    print(a_author)
    a_date = soup.select('div.date')[0].text
    print(a_date)
    print('https://www.ptt.cc/'+a_url)
    print('===========================================')
