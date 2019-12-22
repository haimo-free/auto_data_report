#!/usr/bin/python
# coding=utf-8

from filter import Filter


class ToutiaoFilter(Filter):

    def do(self, request):
        if request.query["app_name"] != "toutiao":
            return False

        print("Toutiao")
        return True
