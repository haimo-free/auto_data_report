#!/usr/bin/python
# coding=utf-8


class RequestItem:
    host = ""
    path = ""
    query = {}
    post = ""

    def valid(self):
        return self.host != "" and \
               self.path != "" and \
               self.query and \
               self.post != ""