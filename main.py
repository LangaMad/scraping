import requests
from bs4 import BeautifulSoup as BS


# file = open('test.html',encoding='utf-8')

# html = file.read()

# soup = BS(html,'html.parser')
# # menu_list = soup.find("div",{"class":"container"})
# # nav_menu = menu_list.find("div",{"class":"navigator-container"})
# # ul = nav_menu.find("ul",{"class":"menu"})
# # li_list = ul.find_all("li")
# # for li in li_list:
# #     print(li.text.strip())

# content = soup.find("div",{"class":"container"})
# cont_con = content.find("div",{"class":"content-container"})
# post_list = cont_con.find_all("div",{"class":"post"})

# for post in post_list:
#     title = post.find("h1",{"class":"title"})
#     print(title.text.strip())

# URL = "https://www.house.kg/snyat-kvartiru?"
# def get_html(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.text
#     return None



# def main():
#     URL = "https://www.house.kg/snyat-kvartiru?"
#     html = get_html(URL)
