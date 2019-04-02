# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:27:09 2019

@author: Nagendra.B
"""

import pandas as pd
import json

def educationprocess():    
    edudata = pd.read_csv("D:/2019/Python/Education_new.csv")
    resultframe = pd.DataFrame()
    for i in range(0,len(edudata)):
        try:
            #print(json.loads(edudata["Education"][i]))
            #print(edudata["id"][i])
            framedata = pd.DataFrame.from_dict(json.loads(edudata["Education"][i]), orient='columns')
            framedata["id"] = edudata["id"][i]
            resultframe = resultframe.append(framedata)
        except:
            print("error")
    return  resultframe.reset_index(drop = True)
