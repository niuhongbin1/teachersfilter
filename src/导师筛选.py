import requests
from lxml import etree
import threading
import save_excel

def get_teacher_list():
    url = "https://power.seu.edu.cn/9355/list.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    html = response.text
    p = etree.HTML(html)   
    ts = p.xpath('//table[@class="MsoNormalTable"]/tbody/tr/td/table[@class="MsoNormalTable"]/tbody//td/p')
    tds_all = []
    for tp in ts:
        try:
            name = tp.xpath('.//a//text()')[0].strip().replace('\n', '').replace('\r', '')
            tu = tp.xpath('.//a/@href')[0]
            tds_all.append({
                            'name': name,
                            'url': tu
                            })
        except:
            pass
    return tds_all

class myThread (threading.Thread):
    def __init__(self,po):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        self.po = po
        self.det = None
    def run(self):
        self.det = ayhet_det(self.po)
    def get_det(self):
        return self.det

def ayhet_det(po):
    url = po['url']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
    except:
        print('error', url)
        response = False
        pass
    if response == False: 
        po['g'] = 0
    else:
    # response.encoding = "utf-8"
        html = response.text
        po['g'] = judge_teacher(html)
        pass



def judge_teacher(t):
    g = 0
    if '计算机' in t:
        g += 1
    elif '人工智能' in t:
        g += 6
    elif '软件' in t:
        g += 1
    elif '网络' in t:
        g += 8
    elif '程序' in t:
        g += 1
    elif '数据' in t:
        g += 3
    elif '通信' in t:
        g += 8
    elif '物联网' in t:
        g += 8
    elif '电子' in t:
        g += 1
    elif '自动化' in t:
        g += 1
    elif '智能' in t:
        g += 2
    elif 'python' in t:
        g += 16
    else:
        pass
    return g

def main():
    ta = get_teacher_list()
    # tasks = []
    for po in ta:
        task = myThread(po)
        task.start()
    tls = []
    for td in ta:
        try:
            tls.append([td['name'],td['g'],td['url']])
        except:
            tls.append([td['name'],0,td['url']])
    save_excel.out('./导师.xlsx',tls)
        
if __name__ == '__main__':
    main()