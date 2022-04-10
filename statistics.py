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
headings = ['Name', '上周', '本周']
data = [
    ['罗远明', '刘兴国', '王超', '王言章', '李若愚', '聂正']
]


def set_excel_info(chart, x: str):
    """x：图表标题"""
    chart.set_title({'name': x})
    chart.set_x_axis({'name': 'Member name'})
    chart.set_y_axis({'name': 'Weekly volume data'})


# 代码量统计
def code_count():
    data_code_list = data.copy()
    # 上周代码量数据
    list_last_week = [1431, 2228, 1686, 1849, 14619, 531]
    list_this_week = [745, 271, 2105, 723, 1767, 740]
    data_code_list += list_last_week, list_this_week
    # print(type(data_code_list[1][2]))
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
    set_excel_info(chart, '制造协同周代码量分析表')

    # 设置图表的风格
    chart.set_style(1)

    # 把图表插入worksheet以及偏移
    worksheet.insert_chart('A10', chart, {'X_offset': 25, 'y_sheet': 10})


# 任务量统计
def assignment_volumn():
    assign_data_list = data.copy()
    assign_last_week = [1, 0, 1, 3, 4, 0]
    assign_this_week = [6, 6, 2, 8, 2, 11]
    assign_data_list += assign_last_week, assign_this_week

    # 写入表头
    worksheet.write_row('J1', headings, bold)
    # 写入数据
    worksheet.write_column('J2', assign_data_list[0])
    worksheet.write_column('K2', assign_data_list[1])
    worksheet.write_column('L2', assign_data_list[2])

    # 生成图表并插入到excel
    # 1.创建一个柱状图
    chart_2 = workbook.add_chart({'type': 'column'})
    # 2.配置第一个系列的数据
    chart_2.add_series({
        'name': '=Sheet1!$K$1',
        'categories': '=Sheet1!$J2:$J7',
        'values': '=Sheet1!$K2:$K7',
        'line': {'color': 'yellow'},
    })

    # 3.配置第二个系列数据
    chart_2.add_series({
        'name': '=Sheet1!$L$1',
        'categories': '=Sheet1!$J2:$J7',
        'values': '=Sheet1!$L2:$L7',
        'line': {'color': 'purple'},
    })

    # 4.设置图表的title和x，y轴信息
    set_excel_info(chart_2, '制造协同周任务量分析表')

    # 设置图表的风格
    chart_2.set_style(1)

    # 把图表插入worksheet以及偏移
    worksheet.insert_chart('J10', chart_2, {'X_offset': 25, 'y_sheet': 10})
    workbook.close()


# 给出函数入口
if __name__ == '__main__':
    code_count()
    assignment_volumn()