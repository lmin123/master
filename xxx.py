# -*- coding:utf8 -*-
#



dict = {'x': 'a| b| c |  ','y' :'ss|dd|yy  ' ,'z' : 'ww| rr| gg |  '}


def myfunc(xxx):
    query_list = []
    for k,v in xxx.items():
        for key in v.split('|'):
            if key.strip():
                query_list.append(key.strip())
    return query_list



print myfunc(dict)



