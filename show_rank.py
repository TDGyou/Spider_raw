'''
此模块为实现排行榜的打印
'''

def show_rank(data):
    l = len(data)
    for i in range(l):
        print('排名' + str(i + 1) 
        + ': ' + data[i]['name'] 
        + '  人气: ' 
        + str(data[i]['hot']) )
