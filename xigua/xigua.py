#!/usr/bin/python
# coding=utf-8

import filter


class XiguaFilter(filter.Filter):

    def analyze(self, get, post):
        if get["app_name"] != "xigua":
            return False

        print("Xigua")
        return True


class XiguaV1Filter(XiguaFilter):

    def analyze(self, get, post):
        if not super().analyze(get, post):
            return False

        print("Xigua V1")
        return True


def generate_filters():
    return [
        XiguaV1Filter
    ]
