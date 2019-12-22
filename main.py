#!/usr/bin/python
# coding=utf-8

import file
from xigua import xigua

filters = []


def generate_filter_list():
    temp_filters = xigua.generate_filters()
    if temp_filters:
        for item in temp_filters:
            filters.append(item)


def read_file():
    filepath = "data.xml"
    return file.parse(filepath)


def main():
    # 创建过滤器列表
    generate_filter_list()

    # 读取文件
    request_items = read_file()
    if not request_items:
        print("read file failed")
        return False

    # 分析数据
    # for request in request_items:
    #     for _filter in filters:
    #         if not _filter.analyze(request):
    #             break


main()
