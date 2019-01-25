# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os
import operateSqlite
import employeesManger
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

## 获取上个月的个税缴纳信息
def _getLastMonthTaxInfo(date):
    taxResults = []
    if date.find("-01") != -1:
        print "first month don't have last month"
        return taxResults
    lastDate = date[0:date.find("-")+1]
    currentMonth = int(date[date.find("-")+1:])
    currentMonth = currentMonth - 1 
    if currentMonth < 10:
        lastDate = lastDate + "0"+str(currentMonth)
    else:
        lastDate = lastDate + str(currentMonth)
    return _getMonthTaxInfo(lastDate)

def _getMonthTaxInfo(date):
    taxResults = [] 
    try:
        operateSqlite.ConnectSqlite()
        operateSqlite.g_dict["cursor"].execute( str("select * from TaxInfos where date = '%s'"%(date)))
        taxInfos = operateSqlite.g_dict["cursor"].fetchall();
        for info in taxInfos:
            result = {}
            result["name"] = info[1]
            result["comp"] = info[2]
            result["department"] = info[3]
            result["job"] = info[4]
            result["currentSalary"] = info[5]
            result["currentNeedTaxNumber"] = info[6]
            result["yearTaxNumber"] = info[7]
            result["customCutout"] = info[8]
            result["currentTax"] = info[9]
            result["yearTax"] = info[10]
            result["date"] = info[11]
            result["comunicationCost"] = info[12]
            result["socialSecurity"] = info[13]
            taxResults.append(result)
    except Exception,error:
        print "error ",error
        pass
    finally:
        operateSqlite.CloseSqlite()
    return taxResults

def _getMonthsTaxInfo(dateStart,dateEnd):
    taxResults = [] 
    try:
        operateSqlite.ConnectSqlite()
        operateSqlite.g_dict["cursor"].execute( str("select * from TaxInfos where date >= '%s' and date <='%s' order by date"%(dateStart,dateEnd)))
        taxInfos = operateSqlite.g_dict["cursor"].fetchall();
        for info in taxInfos:
            result = {}
            result["name"] = info[1]
            result["comp"] = info[2]
            result["department"] = info[3]
            result["job"] = info[4]
            result["currentSalary"] = info[5]
            result["currentNeedTaxNumber"] = info[6]
            result["yearTaxNumber"] = info[7]
            result["customCutout"] = info[8]
            result["currentTax"] = info[9]
            result["yearTax"] = info[10]
            result["date"] = info[11]
            result["comunicationCost"] = info[12]
            result["socialSecurity"] = info[13]
            taxResults.append(result)
    except Exception,error:
        print "error ",error
        pass
    finally:
        operateSqlite.CloseSqlite()
    return taxResults

## 根据月份删除个税信息
def _deleteTaxInfoByDate(date):
    try:
        operateSqlite.ConnectSqlite()
        operateSqlite.g_dict["cursor"].execute( str("delete from TaxInfos where date = '%s'"%(date)))
    except Exception,error:
        print "error ",error
        pass
    finally:
        operateSqlite.CloseSqlite()

def _insertTaxInfo(info):
    try:
        operateSqlite.ConnectSqlite()
        operateSqlite.g_dict["cursor"].execute("insert into TaxInfos(name, comp,department,job, \
                                                currentSalary,currentNeedTaxNumber,\
                                               yearTaxNumber,customCutout, currentTax,yearTax, date,\
                                               comunicationCost,socialSecurity) \
                                               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",info)
    except Exception,error:
        print "error ",error
        pass
    finally:
        operateSqlite.CloseSqlite()
        
## 测试
##print _getLastMonthTaxInfo("2019-05")

TaxData = {};

def ProcessTaxXLS(date,fileName):
    print u"处理个税信息"
    lastTaxInfos = _getLastMonthTaxInfo(date)
    
    excelData = open_excel(fileName)
    for sheet in excelData.sheets():
        if sheet.name.find(u"个税")==-1:
            continue
##        print  sheet.name
        _deleteTaxInfoByDate(date)
        employeesInfos = employeesManger.GetSimpleEmployeeInfo()
        try:
            nRows = sheet.nrows
            nCols = sheet.ncols
            if nRows > 0 and nCols>0:
                for row in range(g_nStartRow,nRows):
                     
                    ## 增加容错率
                    try:
                        rowValue = sheet.row_values(row)
                        name = rowValue[0]
                        
                        comp = ""
                        department = ""
                        job = ""
                        for info in employeesInfos:
                            if info["name"] == name:
                                comp = info["projName"]
                                department = info["department"]
                                job = info["job"]
                                break;
                        ## 收入
                        salary = float(rowValue[1])
                        ## 通信费用
                        cut1 = 0.0
                        ## 三险一金费用
                        cut2 = 0.0
                        ## 专项扣除1
                        cut3 = 0.0
                        ## 专项扣除2
                        cut4 = 0.0
                        ## 专项扣除3
                        cut5 = 0.0
                        ## 专项扣除4
                        cut6 = 0.0
                        ## 专项扣除5
                        cut7 = 0.0
                        ## 专项扣除6
                        cut8 = 0.0
                        try:
                            if rowValue[2] != "" :
                                cut1 = float(rowValue[2])
                            if rowValue[3] != "" :
                                cut2 = float(rowValue[3])
                            if rowValue[4] != "" :
                                cut3 = float(rowValue[4])
                            if rowValue[5] != "" :
                                cut4 = float(rowValue[5])
                            if rowValue[6] != "" :
                                cut5 = float(rowValue[6])
                            if rowValue[7] != "" :
                                cut6 = float(rowValue[7])
                            if rowValue[8] != "" :
                                cut7 = float(rowValue[8])
                            if rowValue[9] != "" :
                                cut8 = float(rowValue[9])
                        except Exception,error:
                            print u"解析专项扣除失败",error
                        currentSalary = salary
                        ## 计算所需缴纳税金
                        salary = salary - 5000 - cut1 - cut2 - cut3 - cut4 - cut5 - cut6 - cut7 - cut8
                        
                        currentNeedTaxNumber = 0.0
                        yearTaxNumber = 0.0
                        customCutout = cut3+cut4+cut5+cut6+cut7+cut8
                        currentTax = 0.0
                        yearTax = 0.0
                        ## 假如存在历史数据
                        if len(lastTaxInfos) > 0:
                            for info in lastTaxInfos:
                                if info["name"] == name:
                                    if salary > 0:
                                        currentNeedTaxNumber = salary
                                    else:
                                        currentNeedTaxNumber = 0
                                    yearTaxNumber = float(info["yearTaxNumber"])
                                    yearTaxNumber = yearTaxNumber + currentNeedTaxNumber
                                    
                                    if yearTaxNumber <= 36000:
                                        currentTax = currentNeedTaxNumber * 0.03
                                    elif yearTaxNumber <= 144000:
                                        currentTax = currentNeedTaxNumber * 0.1
                                    elif yearTaxNumber <= 300000:
                                        currentTax = currentNeedTaxNumber * 0.2
                                    elif yearTaxNumber <= 420000:
                                        currentTax = currentNeedTaxNumber * 0.25
                                    elif yearTaxNumber <= 660000:
                                        currentTax = currentNeedTaxNumber * 0.3
                                    elif yearTaxNumber <= 960000:
                                        currentTax = currentNeedTaxNumber * 0.35
                                    elif yearTaxNumber > 960000:
                                       currentTax = currentNeedTaxNumber * 0.45
                                    yearTax = float(info["yearTax"])
                                    yearTax =  yearTax + currentTax
                                    print u"当月税金",currentTax,u"当年税金",yearTax,u"年度累计应纳税总额",yearTaxNumber
                                    break
                            pass
                        ## 不存在历史数据
                        else:
                            if salary > 0:
                                currentNeedTaxNumber = salary
                            else:
                                currentNeedTaxNumber = 0
                            yearTaxNumber = yearTaxNumber + currentNeedTaxNumber
                            if yearTaxNumber <= 36000:
                                currentTax = currentNeedTaxNumber * 0.03
                            elif yearTaxNumber <= 144000:
                                currentTax = currentNeedTaxNumber * 0.1
                            elif yearTaxNumber <= 300000:
                                currentTax = currentNeedTaxNumber * 0.2
                            elif yearTaxNumber <= 420000:
                                currentTax = currentNeedTaxNumber * 0.25
                            elif yearTaxNumber <= 660000:
                                currentTax = currentNeedTaxNumber * 0.3
                            elif yearTaxNumber <= 960000:
                                currentTax = currentNeedTaxNumber * 0.35
                            elif yearTaxNumber > 960000:
                               currentTax = currentNeedTaxNumber * 0.45
                            yearTax =  yearTax + currentTax
                            print u"当月税金",currentTax,u"当年税金",yearTax,u"年度累计应纳税总额",yearTaxNumber
                            pass
                        _insertTaxInfo((name,comp,department,job,currentSalary,currentNeedTaxNumber,
                                        yearTaxNumber,customCutout,currentTax,yearTax,date,cut1,cut2))
                        print name,salary
                    except Exception,error:
                        print "parse row error",error
                        pass
                print "rows",nRows,"cols",nCols
        except Exception,error:
            print "error",error
            pass
        finally:
            pass

##ProcessTaxXLS("2019-02","testTax.xlsx")
def GetTaxData(date):
    print u"获取所得税信息信息",date
    return _getMonthTaxInfo(date)
##print GetTaxData("2019-02")

def GetTaxDataByMonths(dateStart,dateEnd):
    print u"根据月份获取所得税信息信息",dateStart,dateEnd
    return _getMonthsTaxInfo(dateStart,dateEnd)
