import rubbish.v111.Users
from bs4 import BeautifulSoup
class Users(rubbish.v111.Users.Users):

    def __init__(self ):  # 先继承，在重构
        super(Users, self).__init__()  # 继承父类的构造方法
        self.login_url= "http://bkjws.sdu.edu.cn/b/ajaxLogin"
        self.login_headers["host"]="bkjws.sdu.edu.cn"
        self.login_headers["origin"]="http://bkjws.sdu.edu.cn"
        # print(self.sessions)
    def bxqList(self):
        """本学期成绩"""
        data = """aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A10%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A20%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22xnxq%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22kch%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22kcm%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22kxh%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22xf%22%7D%2C%7B%22name%22%3A%22mDataProp_5%22%2C%22value%22%3A%22kssj%22%7D%2C%7B%22name%22%3A%22mDataProp_6%22%2C%22value%22%3A%22kscjView%22%7D%2C%7B%22name%22%3A%22mDataProp_7%22%2C%22value%22%3A%22wfzjd%22%7D%2C%7B%22name%22%3A%22mDataProp_8%22%2C%22value%22%3A%22wfzdj%22%7D%2C%7B%22name%22%3A%22mDataProp_9%22%2C%22value%22%3A%22kcsx%22%7D%2C%7B%22name%22%3A%22iSortCol_0%22%2C%22value%22%3A5%7D%2C%7B%22name%22%3A%22sSortDir_0%22%2C%22value%22%3A%22desc%22%7D%2C%7B%22name%22%3A%22iSortingCols%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22bSortable_0%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_1%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_2%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_3%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_4%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_5%22%2C%22value%22%3Atrue%7D%2C%7B%22name%22%3A%22bSortable_6%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_7%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_8%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_9%22%2C%22value%22%3Afalse%7D%5D"""
        self.login_headers["content-length"] = "1744"
        r=self.sessions.post(url="http://bkjws.sdu.edu.cn/b/cj/cjcx/xs/list",data=data,headers=self.login_headers)
        return r.json()
    def lscj(self):
        """历史成绩"""
        data="""aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A10%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A20%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22xnxq%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22kch%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22kcm%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22kxh%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22xf%22%7D%2C%7B%22name%22%3A%22mDataProp_5%22%2C%22value%22%3A%22kssj%22%7D%2C%7B%22name%22%3A%22mDataProp_6%22%2C%22value%22%3A%22kscjView%22%7D%2C%7B%22name%22%3A%22mDataProp_7%22%2C%22value%22%3A%22wfzjd%22%7D%2C%7B%22name%22%3A%22mDataProp_8%22%2C%22value%22%3A%22wfzdj%22%7D%2C%7B%22name%22%3A%22mDataProp_9%22%2C%22value%22%3A%22kcsx%22%7D%2C%7B%22name%22%3A%22iSortCol_0%22%2C%22value%22%3A5%7D%2C%7B%22name%22%3A%22sSortDir_0%22%2C%22value%22%3A%22desc%22%7D%2C%7B%22name%22%3A%22iSortingCols%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22bSortable_0%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_1%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_2%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_3%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_4%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_5%22%2C%22value%22%3Atrue%7D%2C%7B%22name%22%3A%22bSortable_6%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_7%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_8%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_9%22%2C%22value%22%3Afalse%7D%5D"""
        self.login_headers["content-length"]="1744"
        r=self.sessions.post(url="http://bkjws.sdu.edu.cn/b/cj/cjcx/xs/lscx",data=data,headers=self.login_headers)
        return r.json()
    def bjgcj(self):
        """不及格成绩"""
        data = """aoData=%5B%7B%22name%22%3A%22sEcho%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22iColumns%22%2C%22value%22%3A10%7D%2C%7B%22name%22%3A%22sColumns%22%2C%22value%22%3A%22%22%7D%2C%7B%22name%22%3A%22iDisplayStart%22%2C%22value%22%3A0%7D%2C%7B%22name%22%3A%22iDisplayLength%22%2C%22value%22%3A20%7D%2C%7B%22name%22%3A%22mDataProp_0%22%2C%22value%22%3A%22xnxq%22%7D%2C%7B%22name%22%3A%22mDataProp_1%22%2C%22value%22%3A%22kch%22%7D%2C%7B%22name%22%3A%22mDataProp_2%22%2C%22value%22%3A%22kcm%22%7D%2C%7B%22name%22%3A%22mDataProp_3%22%2C%22value%22%3A%22kxh%22%7D%2C%7B%22name%22%3A%22mDataProp_4%22%2C%22value%22%3A%22xf%22%7D%2C%7B%22name%22%3A%22mDataProp_5%22%2C%22value%22%3A%22kssj%22%7D%2C%7B%22name%22%3A%22mDataProp_6%22%2C%22value%22%3A%22kscjView%22%7D%2C%7B%22name%22%3A%22mDataProp_7%22%2C%22value%22%3A%22wfzjd%22%7D%2C%7B%22name%22%3A%22mDataProp_8%22%2C%22value%22%3A%22wfzdj%22%7D%2C%7B%22name%22%3A%22mDataProp_9%22%2C%22value%22%3A%22kcsx%22%7D%2C%7B%22name%22%3A%22iSortCol_0%22%2C%22value%22%3A5%7D%2C%7B%22name%22%3A%22sSortDir_0%22%2C%22value%22%3A%22desc%22%7D%2C%7B%22name%22%3A%22iSortingCols%22%2C%22value%22%3A1%7D%2C%7B%22name%22%3A%22bSortable_0%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_1%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_2%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_3%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_4%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_5%22%2C%22value%22%3Atrue%7D%2C%7B%22name%22%3A%22bSortable_6%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_7%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_8%22%2C%22value%22%3Afalse%7D%2C%7B%22name%22%3A%22bSortable_9%22%2C%22value%22%3Afalse%7D%5D"""
        self.login_headers["content-length"] = "1744"
        r=self.sessions.post(url="http://bkjws.sdu.edu.cn/b/cj/cjcx/xs/bjgcx",data=data,headers=self.login_headers)
        return r.json()
    def paiming(self,datas):
        self.login_headers["content-length"] =str(len(datas))
        r=self.sessions.post(url="http://bkjws.sdu.edu.cn/f/cj/cjcx/xs/xspm",data=datas,headers=self.login_headers)
        html=r.text
        if "排名" not in html:
            return ""
        soup=BeautifulSoup(html,"lxml")
        js=soup.find_all('td')
        ans="选课人数:"+str(js[6]).replace("<td>","").replace("</td>","")+\
        "排名:" + str(js[7]).replace("<td>", "").replace("</td>", "") +\
        "最高分:" + str(js[8]).replace("<td>", "").replace("</td>", "") +\
        "最低分:" + str(js[9]).replace("<td>", "").replace("</td>", "")
        return ans

