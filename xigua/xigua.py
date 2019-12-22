#!/usr/bin/python
# coding=utf-8

import filter


class XiguaFilter(filter.Filter):

    def analyze(self, request):
        if not request or not request.valid():
            return False

        if request.query["app_name"] != "xigua":
            return False

        print("[xigua]")

        return True


def generate_filters():
    return [
        XiguaFilter()
    ]
