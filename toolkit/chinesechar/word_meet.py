#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: word_meet
# author: leo.liu
# date: 2018.5.10


# 基于汉字字库，列出
# 两个字 
# 三个字
# 四个字
# 的列表
def word_meet(wordlist, count):
    # namelist = []

    f = open('out.txt', 'w')
    for w1 in wordlist:
        for w2 in wordlist:
            name1 = w1+w2
            # print(name1)
            # namelist.append(name1)
            f.write(name1.encode('utf-8') + '\n')
    f.close()


#    指定前面一个字，自动生成后面的
def add_word(pre_word, word_list, count=1000):

    # name_list = []

    f = open('out.txt', 'w')
    for w1 in word_list:
        name1 = pre_word + w1
        f.write(name1.encode('utf-8') + '\n')

    f.close()


# 功能：从文本文件中读取返回为列表的形式
# 输入：文件名称，分隔符（默认,）
def read_list_csv(filename="", split_symbol=","):
    data_list = []
    with open(filename, "r") as csvFile:
        data_line = csvFile.readline().strip("\n")
        while data_line != "":
            tmp_list = data_line.split(split_symbol)
            data_list.append(tmp_list)
            data_line = csvFile.readline().strip("\n")
        csvFile.close()
    return data_list


# 所有汉字
def all_words(num=1000):
    # 加载常用字
    filename = 'allChineseChar.csv'
    lists = read_list_csv(filename=filename)
    lists = lists[1:]

    word_list = []
    for line in lists:
        print("%s %s %s" % (line[0], line[1], line[2].decode("utf-8")))
        cid = int(line[0][1:-1])
        if cid > num:
            break
        word_list.append(line[2][1:-1].decode('utf-8'))

    return word_list


# 3500个常用汉字
def common_words():
    filename = '3500words.txt'
    m_str = ''
    for line in open(filename):
        m_str += line

    print(m_str)
    m_str = m_str.decode("utf-8")

    word_list = []
    for ss in m_str:
        word_list.append(ss)
        # print(ss.encode("utf-8"))

    return word_list


def main():
    # word_list = all_words()
    word_list = common_words()
    # 两个字
    #word_meet(word_list)
    # 三个字

    add_word(u'一', word_list)



if __name__ == "__main__":
    main()
