# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:18:45 2019

@author: Nagendra.B
"""

import pandas as pd

def dataprocess(filepath,collen,startline):
    weddata = pd.read_fwf(filepath,header = None)
    #weddata = pd.read_fwf("D:/2019/Python/wed.txt",header = None)
    resultframe = pd.DataFrame()
    for i in range(startline,len(weddata)):
        xx = weddata[0][i].split(" ")
        if len(xx) > collen:
            xx.reverse()
            yy = xx[0:(collen-1)]
            name_value = xx[(collen-1):]
            name_value.reverse()
            name_value = ' '.join(name_value)
            yy.append(name_value)
            yy.reverse()
            resultframe = resultframe.append((pd.DataFrame(yy)).transpose())
        else:
            resultframe = resultframe.append((pd.DataFrame(xx)).transpose())
    return resultframe.reset_index(drop = True)


        




    









#df1['State_reverse'] = df1.loc[:,'State'].apply(lambda x: x[::-1])

    