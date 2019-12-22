#!/usr/bin/python
# coding=utf-8

import filter


class XiguaFilter(filter.Filter):

    def analyze(self, request):
        if not request or not request.valid():
            return False

        if request.query["app_name"] != "xigua":
            return False

        print("Xigua")
        return True


class XiguaV1Filter(XiguaFilter):

    def analyze(self, request):
        if not super().analyze(request):
            return False

        print("Xigua V1")
        return True


def generate_filters():
    return [
        XiguaV1Filter()
    ]
