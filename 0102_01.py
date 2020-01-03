from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
#web크롤링
request = Request("https://movie.naver.com/movie/running/current.nhn")
response = urlopen(request)
html = response.read().decode("utf-8")

bs = BeautifulSoup(html, "html.parser")
# current_movies = bs.select(".lst_detail_t1 > li")
# for movie in current_movies:
#titles = bs.select(".lst_dsc > .tit > a")
titles = bs.select(".tit > a")
f = open('html.txt', 'w', encoding='utf-8')
for title in titles :
     f.write(title.text+" "+title['href']+"\n")
     #print(title.text, title['href'])
f.close()

f = open('html.txt', 'r')
print(f.read())
f.close()