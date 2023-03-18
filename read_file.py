# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Python3.10

import pandas as pd
import sys
def parse_file(file_name):
    row_list = []
    if file_name.endswith('.csv'):
        # data = pd.read_csv(file_name,dtype={})
        data = pd.read_csv(file_name,low_memory=False)
    elif file_name.endswith('.xlsx'):
        data = pd.read_excel(file_name)
    else:
        sys.exit()
    head_list = list(data.columns)
    for val in data.values:
        line = dict(zip(head_list,val))
        row_list.append(line)
    return row_list



if __name__ == '__main__':
    f = parse_file("D:\桌面\数据样本例V1.xlsx")
    # print(f)
    for i in f[:1]:
        # print(i['Name'])
        print(i)