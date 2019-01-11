# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os
import operateSqlite
from datetime import datetime

g_nStartRow = 1
g_nStartCol = 2
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
def _transValueToDate(value):
    try:
        date = datetime(*xlrd.xldate_as_tuple(int(value), 0))
        return date.strftime('%Y-%m-%d')
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

def AddEmployeesInfoByFileName(fileName):       
    excelData = open_excel(fileName)
    for sheet in excelData.sheets():
        if sheet.name.find(u"人员信息")==-1:
            continue
        operateSqlite.ConnectSqlite()
        try:
            nRows = sheet.nrows
            nCols = sheet.ncols
            if nRows > 0 and nCols>0:
                operateSqlite.g_dict["cursor"].execute("delete from Employees;");
                for row in range(g_nStartRow,nRows):
                    rowValue = sheet.row_values(row)   
                    rowValue[5] = _transValueToDate(rowValue[5])
                    rowValue[15] = _transValueToDate(rowValue[15])
                    rowValue[34] = _transValueToDate(rowValue[34])
                    rowValue[36] = _transValueToDate(rowValue[36])
                    rowValue[22] = _transValueToStr(rowValue[22])

                    for i in range(0,len(rowValue)):
                        rowValue[i] = _transFloatToInt(rowValue[i])
                    rowTuple = rowValue[g_nStartCol:40+g_nStartCol]

                    print len(rowTuple)
                    intsertSql = "INSERT INTO Employees(companyName,projName,department, job, name,\
                    enterTime, salaryBegin, salaryStart, salaryChange, salaryCurrent, phoneNum, \
                    nation, marry, education, demobilized, bornTime, sex, age, zodiac, \
                    constellation, jobYear, household, personCard, housebase, personAddr, \
                    personCardUsed, isHouse, nowHouse, urgentName, urgentPhone, introductName, \
                    introductProj,leaveTime, leaveReason, contractBegin, contractYear, contractEnd,\
                    isSecurity, securitySituation, remarks)\
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                    operateSqlite.g_dict["cursor"].execute(intsertSql,tuple(rowTuple))
                print nRows,nCols
                operateSqlite.g_dict["conn"].commit()
        except Exception,error:
            print "error",error
            operateSqlite.g_dict["conn"].rollback();
            pass
        finally:
            operateSqlite.CloseSqlite()
            
##AddEmployeesInfoByFileName("Employees.xlsx")
