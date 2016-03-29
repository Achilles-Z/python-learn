#!/usr/bin/python
# -*- coding: utf-8 -*-
# author zeck.tang 2016-03-15

import datetime

"""
脚本用于计算SDK各Event数据Count
1. event=play (PV)
2. event=router (Router)
3. event=cdn (CDN)
4. event=resource (Resource)
5. DAU(依据play事件deviceid去重得到)
"""



def getCount ():
    today = datetime.date.today()
    yesterday = today + datetime.timedelta(-1)
    fileName = 'sdk_%s.log' % yesterday.strftime('%Y%m%d')
    playCount = 0
    routerCount =0
    cdnCount =0
    resourceCount =0
    DAUCount =0
    file =  open(fileName,'r')
    dic = {}
    dauArray = []
    line = file.readline()
    while line:
        line = line.replace('\n','')
        tempStr = line.split('&')
        print tempStr
        for temp in tempStr:
            if temp != '':
                tempArr = temp.split('=')
                key = tempArr[0]
                value = tempArr[1]
                dic[key] = value
        print dic

        if dic['event'] == 'play':
            playCount = playCount + 1
            if len(dauArray) >0 :
                if dic['uniqueId'] in dauArray :
                    print 'not unique'
                else :
                    dauArray.append(dic['uniqueId'])
            else:
                dauArray.append(dic['uniqueId'])
        if dic['event'] == 'router':
            routerCount  = routerCount + 1
        if dic['event'] == 'cdn':
            cdnCount  = cdnCount + 1
        if dic['event'] == 'resource':
            resourceCount  = resourceCount + 1

        #read next do loop
        line = file.readline()
    file.close()
    print 'playCount =%s ; routerCount = %s ; cdnCount = %s ; resourceCount = %s ; DAU = %s' % (playCount,routerCount,cdnCount,resourceCount,len(dauArray))




if __name__ == '__main__':
    getCount()