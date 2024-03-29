import json

import xlrd

class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        #get excel &sheet
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # get titles
        self.row = self.table.row_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1

    def next(self):
        case = []
        while self.hasNext():
            s = {}
            #获取每一行的值
            col = self.table.row_values(self.curRowNo)
            #总列数
            i = self.colNum
            for x in range(i):
            #创建字典，标题为键，内容为值
                s[self.row[x]] = col[x]
            case.append(s)
            self.curRowNo += 1
        # print(case)
        return case


    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True


if __name__ == '__main__':
    excel = ExcelUtil("G:\LocalGit\github仓库\API_Test\Demo\jiekou.xlsx", '汇总')
    data = excel.next()
    print(data[2])
    print(type(data[2]['参数']))
    # a=json.dumps(data[2]['参数'])
    a=data[2]['参数']
    a=eval(a)
    print(a)
    print(type(a))

