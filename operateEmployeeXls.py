# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os
import operateSqlite

g_nStartRow = 0
g_nStartCol = 0
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def AddEmployeesInfoByFileName(fileName):       
    excelData = open_excel(fileName)
    for sheet in excelData.sheets():
        operateSqlite.ConnectSqlite()
        try:
            nRows = sheet.nrows
            nCols = sheet.ncols
            if nRows > 0 and nCols>0:
                operateSqlite.g_dict["cursor"].execute("delete from Employees;");
                for row in range(g_nStartRow,nRows):
                    rowValue = sheet.row_values(row)
                    rowTuple = rowValue[g_nStartCol:]
                    print len(rowTuple),rowTuple
                    break
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
