# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os
import operateSqlite
from datetime import datetime

g_nStartRow = 1
g_nStartCol = 0
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
def _transValueToDate(value):
    try:
        date = datetime(*xlrd.xldate_as_tuple(float(value), 0))
        return date.strftime('%Y-%m-%d %H:%M:%S')
    except Exception,error:
        pass
        #print "_transValueToDate error",error
    return value
def _transValueToStr(value):
    try:
        return "%d"%value
    except Exception,error:
        pass
        #print "_transValueToStr error",error
    return value
def _transFloatToInt(value):
    try:
        return int(value)
    except Exception,error:
        pass
    return value
RewardData = {};

def ProcessRewardXLS(fileName):
    print u"处理奖励信息"
    
    excelData = open_excel(fileName)
    for sheet in excelData.sheets():
        print  sheet.name
        if sheet.name.find(u"奖励")==-1:
            continue
        try:
            nRows = sheet.nrows
            nCols = sheet.ncols
            if nRows > 0 and nCols>0:
                for row in range(g_nStartRow,nRows):
                     
                    ## 增加容错率
                    try:
                        rowValue = sheet.row_values(row)   
                        rowValue[6] = _transValueToDate(rowValue[6])
                        for i in range(0,len(rowValue)):
                            rowValue[i] = _transFloatToInt(rowValue[i])
                            
                        tData = (rowValue[0],rowValue[1],rowValue[2],rowValue[3],rowValue[4],
                                 rowValue[5],rowValue[6],rowValue[7],rowValue[8],rowValue[10])
                        
                        if RewardData.has_key(rowValue[2]):
                            pass
                        else:
                            RewardData[rowValue[2]] = []
                        RewardData[rowValue[2]].append(tData)
                    except:
                        print "parse ProcessRewardXLS row value error",error
                        pass
                print nRows,nCols
        except Exception,error:
            print "error",error
            pass
        finally:
            pass
def GetRewardData():
    if len(RewardData) == 0:
        ProcessRewardXLS("reward.xlsx")
    print u"获取奖励信息"
    DstInfo = [];
    
    for item in RewardData:
        ## 增加容错率
        try:
            SalaryPerson = 0;
            for info in RewardData[item]:
                tDataDict = {}
                tDataDict["id"] = info[0]
                tDataDict["status"] = info[1]
                tDataDict["name"] = info[2]
                tDataDict["comp"] = info[3]
                tDataDict["proj"] = info[4]
                tDataDict["job"] = info[5]
                tDataDict["time"] = info[6]
                tDataDict["position"] = info[7]
                tDataDict["description"] = info[8]
                tDataDict["salary"] = info[9]
                SalaryPerson = SalaryPerson + int(info[9])
                DstInfo.append(tDataDict)
            tDataAll = {}
            tDataAll["name"] = item + u" 奖励统计:"
            tDataAll["proj"] = RewardData[item][0][4]
            tDataAll["job"] = u"总额： "+str(SalaryPerson)
            DstInfo.append(tDataAll)
        except:
            print "parse GetRewardData row value error",error
            pass
    RewardData.clear()
    return DstInfo
##ProcessRewardXLS("test.xlsx")
##print GetRewardData()
