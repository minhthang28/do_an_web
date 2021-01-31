#Các thư viện cần dùng
import  folder_op, web_op

def start():
    url_list = ["https://vietnamnet.vn/"]
    url_list_const=10000
    history=[]
    max_page = 100
    count=0
    folder_op.kiem_tra("C:\\")
    thu_muc_luu_du_lieu = 'C:\\crawl'

    #kịch bản các đường dẫn
    while (count < max_page) and (len(url_list) > 0):
        url_new = []
        url = url_list.pop(0)
        page = web_op.doc_noi_dung(url)
        links = web_op.lay_cac_duong_link(page)
        for item in links:
            if web_op.kiem_tra_link(item)==False:
                item = web_op.chinh_sua_link(url,item)
            if (item not in url_list) and (item not in history) and (item not in url_new) and (item != url):
                url_new.append(item)
        if (len(url_list) + len(url_new) <= url_list_const):
            url_list = url_list + url_new
        else:
            check = int(url_list_const - len(url_list))
            array =url_new[:check]
            url_list = url_list + array
        count += 1
        history.append(url)
        ten_thu_muc = folder_op.tao_ten_thu_muc_tu_dong(thu_muc_luu_du_lieu,url)
        folder_op.luu_file(page, ten_thu_muc)
        folder_op.luu_lich_su_cac_url(url)
        print("Đã duyệt " + str(count) + " url")

if __name__ == '__main__':
    start()