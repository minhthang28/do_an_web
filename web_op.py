#Các thư viện cần dùng
import requests
from bs4 import BeautifulSoup

#Các hàm cần thiết

def doc_noi_dung(url):
    page = requests.get(url)
    html = BeautifulSoup(page.content, 'html.parser')
    return html

def chinh_sua_link(url,item):
    item = item.split(" ")
    url_new= str(url) + item[0]
    return url_new

def kiem_tra_link(url):
    if url[:4] == "http":
        return True
    else:
        return False

def lay_cac_duong_link(file_code_html):
    url = file_code_html.find_all("a")
    url_list = []
    url_hop_le = []
    for i in url:
        link = i.get("href")
        url_list.append(link)
    for i in url_list:
        i = str(i)
        if (i.find("http", 0, 4)):
            if (i.find("java", 0, 4)):
                    if (i.find("#", 0, 4)):
                        if (i.find("None", 0, 4)):
                            if len(i) > 2:
                                url_hop_le.append(i)
        if not(i.find("http", 0, 4)):
            url_hop_le.append(i)
    return url_hop_le