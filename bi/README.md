本程序用于按输入文件中号码的前7位（地区）统计号码，要求每行开头是一个手机号

static -f input_file [-o output_file] -m month_of_data -p plat_of_data

-f  待分析的文件
-o  输出文件名
-m  数据属于哪个月，如2018-1
-p  数据属于哪个平台，
        云信          yx,
        触发          cf,
        云集触发      yjcf,
        云集群发      yjqf