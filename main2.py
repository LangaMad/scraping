import requests
from bs4 import BeautifulSoup as BS
import openpyxl
import csv


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_link(html):
    links = []
    soup = BS(html,"html.parser")
    container = soup.find("div",{"class":"container body-container"})
    main = container.find("div",{"class":"main-content"})
    listing = main.find("div",{"class":"listings-wrapper"})
    post = listing.find_all("div",{"class":"listing"})
    for posts in post:
        l_side = posts.find("div",{"class":"left-side"})
        # title = l_side.find("p").text.strip()
        # address = l_side.find("div",{"class":"address"}).text.strip()
        link = l_side.find("a").get("href")
        full_link = "https://www.house.kg" + link
        # r_side = posts.find("div",{"class":"right-side"})
        # money = r_side.find("div",{"class":"sep main"})
        # dollar = money.find("div",{"class":"price"}).text.strip()
        # som = money.find("div",{"class":"price-addition"}).text.strip()
        # description = posts.find("div",{"class":"description"}).text.strip()
        links.append(full_link)
    return links


def get_post(html):
    soup = BS(html,"html.parser")
    main = soup.find("div",{"class":"main-content"})
    header = main.find("div",{"class":"details-header"})
    name = header.find("div",{"class":"left"}).find("h1").text.strip()
    print(name)
    address = header.find("div",{"class":"address"}).text.strip() 
    dollar = header.find("div",{"class":"sep main"}).find("div",
    {"class":"price-dollar"}).text.strip()
    som = header.find("div",{"class":"sep main"}).find("div",
    {"class":"price-som"}).text.strip()
    mobile = main.find("div",{"class":"phone-fixable-block"}).find(
        "div",{"class":"number"}
    ).text.strip()
    desc = main.find("div",{"class":"description"})
    desc = desc.text.strip() if desc else 'Нет описания'
    # lon = main.find("div",{"id":"map2gis"}).get("data-lon")
    # lat = main.find("div",{"id":"map2gis"}).get("data-lat")
    infos = main.find("div",{"class":"details-main"}).find_all(
        "div",{"class":"info-row"}
    )
    add_info = {}
    
    for info in infos:
        key = info.find("div",{"class":"label"}).text.strip()
        value = info.find("div",{"class":"info"}).text.strip()
        add_info.update({key:value})
    
    data = {
        'title':name,
        'address':address,
        'dollar':dollar,
        'som':som,
        'phone':mobile,
        'description':desc,
        'info':add_info
        
    }
    return data
    
    
def get_last_page(html):
    soup = BS(html,"html.parser")
    page = soup.find("ul",{"class":"pagination"})
    page_list = page.find_all("a",{"class":"page-link"})
    last_page = page_list[-1].get("data-page")  
    
    return int(last_page)
    

def save_to_exel(data):
    workbook  = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Название'
    sheet['B1'] = 'Адрес'
    sheet['C1'] = 'Цена в долларах'
    sheet['D1'] = 'Цена в сом'
    sheet['E1'] = 'Номер'
    sheet['F1'] = 'Описание'
    
    for i,item in enumerate(data,2):
        sheet[f'A{i}'] = item['title']
        sheet[f'B{i}'] = item['address']
        sheet[f'C{i}'] = item['dollar']
        sheet[f'D{i}'] = item['som']
        sheet[f'E{i}'] = item['phone']
        sheet[f'F{i}'] = item['description']
    
    workbook.save('house_data.xlsx')
    
def save_to_csv(data):
    with open('house_data.csv','w', newline = '', 
              encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Название',"Адрес","Цена в долларах",
        "Цена в сома","Номер","Описание"])
        
        for item in data:
            csv_writer.writerow([item['title'],item['address'],item['dollar'],
                    item['som'],item['phone'],item['description']])
   
    
def main():
    URL = 'https://www.house.kg/snyat-kvartiru?region=1&town=2&sort_by=upped_at+desc'
    html = get_html(URL)
    
    last_page = get_last_page(get_html(URL))
    
    
    for i in range(1,3):
        page_url = URL + f'&page={i}'
        
        data = []
        links = get_link(html=html)
        for link in  links:
            detail_html = (get_html(link))
            data.append(get_post(detail_html))
            
    save_to_csv(data)
    save_to_exel(data)
            
    
        

if __name__ == "__main__":
    main()
