"""
 Author:twilight2017
 Realization: 实现一个数据统计脚本，把自己从每周重复无聊的数据统计工作中解救出来
"""

# -*- coding:utf-8 -*-
import xlsxwriter

# 创建一个excel
workbook = xlsxwriter.Workbook("piu_statistics.xlsx")
# 创建一个sheet
worksheet = workbook.add_worksheet()

# 自定义样式，加粗
bold = workbook.add_format({'bold': 1})

# 准备数据写入excel中
headings = ['Period', '上周', '本周']
data = [
    ['罗远明', '刘兴国', '王超', '王言章', '李若愚', '聂正']
]


# 代码量统计
def code_count():
    data_code_list = data
    # 上周代码量数据
    list_last_week = [795, 1789, 357, 653, 14438, 506]
    list_this_week = [1431, 2228, 1686, 1849, 14619, 531]
    data_code_list += list_last_week, list_this_week
    #print(type(data_code_list[1][2]))
    # 写入表头
    worksheet.write_row('A1', headings, bold)
    # 写入数据
    worksheet.write_column('A2', data_code_list[0])
    worksheet.write_column('B2', data_code_list[1])
    worksheet.write_column('C2', data_code_list[2])

    # 生成图表并插入excel
    # 1.创建一个柱状图
    chart = workbook.add_chart({'type': 'column'})

    # 2.配置第一个系列数据
    chart.add_series({
        # sheet1采用默认值，因为我们在新建sheet时没有指定sheet名
        # 如果我们新建sheet时设置了sheet名，这里的参数就要修改为sheet表的名字
        'name': '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$B$2:$B$7',
        'line': {'color': 'red'},
    })

    # 3.配置第二个系列数据
    chart.add_series({
        'name': '=Sheet1!$C$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values': '=Sheet1!$C$2:$C$7',
        'line': {'color': 'blue'},
    })

    # 4.设置图表的title和x，y轴信息
    chart.set_title({'name': '制造协同周代码量分析表'})
    chart.set_x_axis({'name': 'Member name'})
    chart.set_y_axis({'name': 'Weekly code volume data'})

    # 设置图表的风格
    chart.set_style(1)

    # 把图表插入worksheet以及偏移
    worksheet.insert_chart('A10', chart, {'X_offset': 25, 'y_sheet': 10})
    workbook.close()


# 给出函数入口
if __name__ == '__main__':
    code_count()