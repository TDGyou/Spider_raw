'''
此模块实现数据精炼功能
'''
import re

douyu = '<div class="DyListCover-info">([\s\S]*?)<\div>'

panda = '<div class="video-info">([\s\S]*?)</div>'
panda_name = '<span class="video-nickname" title="([\s\S]*?)">'
panda_hot = '<span class="video-number"><i class="ricon ricon-eye"></i>([\s\S]*?)</span>'


def refine_data(data): 
    r = re.findall(panda,data)
    data_refined = []
    for i in r:
        name = re.findall(panda_name,i)[0]
        hot = re.findall(panda_hot,i)[0]
        #有部分高人气主播的人气达到万人级别，故需要转换
        if '万' in hot:
            hot = float(re.sub('万','',hot)) * 10000 
        result = {'name':name,'hot':int(hot)}
        data_refined.append(result)
    return data_refined
