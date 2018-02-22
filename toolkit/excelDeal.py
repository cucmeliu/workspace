# -*- coding: UTF-8 -*-

import xlrd

def open_excel(fileName):
    try:
        data = xlrd.open_workbook(fileName)
        return data
    except Exception as e:
        print str(e)
        return nil

#根据索引获取Excel表格中的数据
#参数:file：Excel文件路径, headrow：表头列名所在行的索引 ，tableindex：表的索引
def read_excel(fileName, tableindex=0, headrow=0):
    # 打开Excel文件读取数据
    data = open_excel(fileName)
    # 获取一个工作表
    # ①  table = data.sheets()[0]       #通过索引顺序获取
    # ②  table = data.sheet_by_index(0) #通过索引顺序获取
    # ③  table = data.sheet_by_name(u'Sheet1')#通过名称获取
    table = data.sheets()[tableindex]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(headrow)
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


    # 4、获取整行和整列的值（返回数组）
    #
    # table.row_values(i)
    # table.col_values(i)
    #
    # 5、获取行数和列数　
    #
    # table.nrows
    # table.ncols
    #
    # 6、获取单元格
    # table.cell(0,0).value
    # table.cell(2,3).value


def readDict(fileName, tableindex=0):
    pass


# 写Excel
# 1、导入模块
#
# 复制代码代码如下:
# import xlwt
#
# 2、创建workbook（其实就是excel，后来保存一下就行）
# 复制代码代码如下:
# workbook = xlwt.Workbook(encoding = 'ascii')
#
# 3、创建表
# 复制代码代码如下:
# worksheet = workbook.add_sheet('My Worksheet')
#
# 4、往单元格内写入内容
# 复制代码代码如下:
# worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
#
# 5、保存
# 复制代码代码如下:
# workbook.save('Excel_Workbook.xls')
