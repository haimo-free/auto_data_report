#!/usr/bin/python
# coding=utf-8

import json

from filter import Filter


class ToutiaoFilter(Filter):

    def analyze(self, request):
        if not request or not request.valid():
            return False

        if request.query["app_name"] != "news_article":
            return False

        return True


class ToutiaoV1Filter(ToutiaoFilter):

    def analyze(self, request):
        """
        {
            "category":"umeng",
            "aggr_type":"1",
            "label":"detail_show",
            "is_ad_event":"1",
            "item_id":"6767299150301151757",
            "sdk_dual_report":"0",
            "ab_sdk_version":"794527",
            "value":"1652163094023278",
            "tag":"embeded_ad",
            "type":"1",
            "group_id":"6767299150301151757",
            "nt":"4",
            "log_extra":"{"ad_price":"XfipEgAPc7Zd-KkSAA9ztgS4nheQvi5COL0QEA","convert_component_suspend":0,"convert_id":1648784231054344,"external_action":8,"is_from_history":false,"is_pack_v2":true,"log_id":"2019121718081701001404703513023538","orit":1,"placement":"unknown","req_id":"2019121718081701001404703513023538","request_type":1,"rit":1,"style_id":4892,"style_ids":[4892],"tpl_id":10025,"van_package":130000005}"
        }
        """

        if not super().analyze(request):
            return False

        post = json.loads(request.post)
        if not post or not isinstance(post, dict):
            return False

        tag = post.get("tag", "")
        if tag == "":
            return False

        print("[toutiao]v1.0 tag=" + tag)


class ToutiaoV3Filter(ToutiaoFilter):

    def analyze(self, request):
        """
        {
            "ab_sdk_version":"794527",
            "sdk_dual_report":"0",
            "event":"tt_route_open_url",
            "type":"1",
            "params":{
                "route_host":"detail",
                "route_url":"sslocal://detail?groupid=6767299150301151757&ad_id=1652163094023278",
                "route_scheme":"sslocal://",
                "groupid":"6767299150301151757",
                "ad_id":"1652163094023278"
            }
        }
        """

        if not super().analyze(request):
            return False

        post = json.loads(request.post)
        if not post or not isinstance(post, dict):
            return False

        event = post.get("event", "")
        if event == "":
            return False

        print("[toutiao]v3.0 event=" + event)


def generate_filters():
    return [
        ToutiaoV1Filter(),
        ToutiaoV3Filter()
    ]
