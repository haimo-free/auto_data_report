#!/usr/bin/python
# coding=utf-8

from filter import Filter


class Toutiao_Filter(Filter):

    def do(self, get, post):
        if (get["app_name"] != "toutiao"):
            return False

        print("Toutiao")
        return True
