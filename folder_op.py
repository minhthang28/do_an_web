#Các thư viện cần dùng
import os

#Các hàm cần thiết


def kiem_tra(duong_dan_thu_muc):
    os.chdir(duong_dan_thu_muc)
    check = os.listdir(duong_dan_thu_muc)
    if 'crawl' not in check:
        os.mkdir('crawl')
        print("Đã tạo thư mục crawl")
    duong_dan_thu_muc = 'C:\\crawl\\'
    os.chdir(duong_dan_thu_muc)
    check = os.listdir(duong_dan_thu_muc)
    if 'Lich_su.txt' not in check:
        file = open("Lich_su.txt", "w", encoding="utf-8")
        file.write("Lịch sử các url đã tải về\n")
        file.close()
        print("Đã file lịch sử")

def tao_ten_thu_muc_tu_dong(duong_dan_thu_muc, url):
    os.chdir(duong_dan_thu_muc)
    count = len(os.listdir(duong_dan_thu_muc))
    ten_thu_muc = "Crawl" + str(count)
    os.mkdir(ten_thu_muc)
    return ten_thu_muc


def luu_file(data, ten_thu_muc):
    duong_dan_thu_muc = "C:\\crawl\\"
    os.chdir(duong_dan_thu_muc + str(ten_thu_muc))
    file = open("HTML.html", "w+", encoding="utf-8")
    file.write(str(data))
    file.close()
    
def luu_lich_su_cac_url(url):
    duong_dan_thu_muc = "C:\\crawl\\"
    os.chdir(duong_dan_thu_muc)
    file = open("Lich_su.txt", mode='r+', encoding='utf-8')
    STT = len(file.readlines())
    file.close()
    file = open("Lich_su.txt", mode='a+', encoding='utf-8')
    content = str(STT) + " " + str(url) + "\n"
    file.write(content)
    file.close()
