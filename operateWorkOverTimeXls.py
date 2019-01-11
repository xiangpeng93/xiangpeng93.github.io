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
        date = datetime(*xlrd.xldate_as_tuple(int(value), 0))
        return date.strftime('%Y-%m-%d:%H-%M-%S')
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
OvertimeWorkData = {};

def ProcessWorkOvertimeXLS(fileName):
    print u"处理加班信息"
    
    excelData = open_excel(fileName)
    for sheet in excelData.sheets():
        print  sheet.name
        if sheet.name.find(u"加班")==-1:
            continue
        try:
            nRows = sheet.nrows
            nCols = sheet.ncols
            if nRows > 0 and nCols>0:
                for row in range(g_nStartRow,nRows):
                    rowValue = sheet.row_values(row)   
                    rowValue[4] = _transValueToDate(rowValue[4])
                    rowValue[5] = _transValueToDate(rowValue[5])
                    for i in range(0,len(rowValue)):
                        rowValue[i] = _transFloatToInt(rowValue[i])
                    if rowValue[8] == "on":
                        rowValue[8] = 1
                    else :
                        rowValue[8] = 0
                        
                    tData = (rowValue[0],rowValue[1],rowValue[2],rowValue[3],rowValue[4],
                             rowValue[5],rowValue[6],rowValue[7],rowValue[8])
                    
                    if OvertimeWorkData.has_key(rowValue[0]):
                        pass
                    else:
                        OvertimeWorkData[rowValue[0]] = []
                    OvertimeWorkData[rowValue[0]].append(tData)
                print nRows,nCols
        except Exception,error:
            print "error",error
            pass
        finally:
            pass
def GetWorkoverData():
    print u"获取加班信息"
    DstInfo = [];
    for item in OvertimeWorkData:
        days = 0
        hours = 0
        leaves = 0
        
        for info in OvertimeWorkData[item]:
            tDataDict = {}
            days = days + int(info[6])
            hours = hours + int(info[7])
            leaves = leaves + int(info[8])
            tDataDict["name"] = info[0]
            tDataDict["comp"] = info[1]
            tDataDict["proj"] = info[2]
            tDataDict["job"] = info[3]
            tDataDict["startTime"] = info[4]
            tDataDict["endTime"] = info[5]
            tDataDict["days"] = info[6]
            tDataDict["hours"] = info[7]
            tDataDict["leaves"] = info[8]
            DstInfo.append(tDataDict)
        tDataAll = {}
        tDataAll["name"] = u"合计"
        tDataAll["days"] = days
        tDataAll["hours"] = hours
        tDataAll["leaves"] = leaves
        DstInfo.append(tDataAll)
    OvertimeWorkData.clear()
    return DstInfo
##ProcessWorkOvertimeXLS("test.xlsx")
##print GetWorkoverData()
