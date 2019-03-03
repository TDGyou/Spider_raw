'''
此原生爬虫项目旨在实现对直播平台（本项目以pandaTV为例）上某分类（本项目为Dota2）的主播人气\
    进行排行，并得出排行榜
'''
from get_html import get_html
from refine_data import refine_data
from sort import sort
from show_rank import show_rank

class Spider():
    html = 'null'
    data = 'null'
    rank = []
    def __get_html(self):
        Spider.html = get_html()
    
    def __refine_data(self,data):
        Spider.data = refine_data(data)
    
    def __sort_data(self,data):
        Spider.rank = sort(data)
    
    def __show_rank(self,data):
        show_rank(data)

    def get_rank(self):
        self.__get_html()
        self.__refine_data(Spider.html)
        self.__sort_data(Spider.data)
        self.__show_rank(Spider.rank)


spider_panda = Spider()
spider_panda.get_rank()

