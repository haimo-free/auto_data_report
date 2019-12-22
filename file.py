#!/usr/bin/python
# coding=utf-8
import request
import urllib
from xml.etree import ElementTree
import define


class Request:

    def _parse_query(self, transaction):
        query = transaction.get("query")
        if query == "":
            return None

        return urllib.parse.parse_qs(query)

    def _parse_post(self, transaction):
        request = transaction.find("request")
        if not request:
            return ""

        body = request.findtext("body")
        if body == "":
            return ""

        body_dict = urllib.parse.parse_qs(body)
        if not body_dict:
            return ""

        parameter = body_dict.get("parameter")
        if not parameter:
            return ""

        return parameter[0]

    def _parse_transaction(self, transaction):
        if transaction.get("host") != "data.bytedance.net":
            return None

        if transaction.get("path") != "/et_api/logview/verify/":
            return None

        request = define.RequestItem()

        request.host = transaction.get("host")
        request.path = transaction.get("path")
        request.query = self._parse_query(transaction)
        request.post = self._parse_post(transaction)

        if request.valid():
            return request
        else:
            return None

    def parse(self, filepath):
        tree = ElementTree.parse(filepath)
        if not tree:
            return None

        root = tree.getroot()

        items = []

        for child in root:
            item = self._parse_transaction(child)
            if item:
                items.append(item)

        return items


def parse(filepath):
    return Request().parse(filepath)
