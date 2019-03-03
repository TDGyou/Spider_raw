'''
此模块实现get html功能
'''
from urllib import request
import gzip

#panda dota2网址
url_dota2 = 'https://www.panda.tv/cate/dota2?pdt=1.24.s1.16.7ko54c8j1cb'
#panda lol网址
url_lol ='https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7ti3ad20q0c'

url = url_dota2

#如果接收到的html数据为gzip类型，则进行解压
def ungzip(data):
    try:
        data = gzip.decompress(data)
    except:
        pass
    return data

def get_html():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent':user_agent}
    page = request.Request(url,headers=headers)
    r = request.urlopen(page)

    #获得字节码类型的html数据
    # html = r.read()
    html = ungzip(r.read())

    #转换成str类型
    html = str(html,encoding = 'utf-8')

    return html

#以下代码为调试模块功能是否实现
if __name__ == '__main__':
    test = get_html()
    print(test)
