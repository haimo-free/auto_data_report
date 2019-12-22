#!/usr/bin/python
# coding=utf-8

from filter import Filter


class ToutiaoFilter(Filter):

    def analyze(self, request):
        if not request or not request.valid():
            return False

        if request.query["app_name"] != "news_article":
            return False

        print("Toutiao")
        return True


def generate_filters():
    return [
        ToutiaoFilter()
    ]