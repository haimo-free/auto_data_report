#!/usr/bin/python
# coding=utf-8

from xigua import xigua

filters = []


def generate_filter_list():
    temp_filters = xigua.generate_filters()
    if temp_filters:
        for item in temp_filters:
            filters.append(item)


def main():
    generate_filter_list()

    get = {"app_name": "xigua", "version": "1.0.0"}
    post = '''{"tag":"video_play"}'''

    for _filter in filters:
        if _filter.analyze(get, post):
            break


main()
