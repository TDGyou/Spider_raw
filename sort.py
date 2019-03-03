'''
此模块实现对处理过后的数据进行排序
'''

def sort_rule(data):
    return data['hot']

def sort(data):
    sorted_data = sorted(data,key = sort_rule,reverse = True)
    return sorted_data
