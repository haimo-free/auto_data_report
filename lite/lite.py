#!/usr/bin/python
# coding=utf-8

import json

from filter import Filter


class LiteFilter(Filter):

    def analyze(self, request):
        if not request or not request.valid():
            return False

        if request.query["app_name"] != "news_article":
            return False

        return True


class LiteV1Filter(LiteFilter):

    def analyze(self, request):

        if not super().analyze(request):
            return False

        post = json.loads(request.post)

        if not post or not isinstance(post, dict):
            return False

        tag = post.get("tag", "not exist")
        if tag == "not exist":
            return False
        return tag
å
    def decide(self):

        keyphrase = ["label", "value", "item_id"]
        label_values = ["click_related", "click_headline", "click_category", "click_search", "click_video"]
        lack_key = []
        wrong_key = []

        for key in keyphrase:
            if key not in post.keys():
                lack_key.append(key)
                continue
            if not post[key]:
                wrong_key.append(key)
                continue
            if key == "label":
                if post[key] not in label_values:
                    lack_key.append(key)
                elif post[key] == label_values[0]:
                    if not post.get("from_id"):
                        lack_key.append("from_id")
                    elif not post["from_id"]:
                        wrong_key.append(key)

        for case in switch(tag):
            if case("go_detail"):
                pass
            if case("video_play"):
                pass
            if case("video_over"):
                pass
            if case("stay_page"):
                pass
            if case("video_play_auto"):
                pass
            if case("video_over_auto"):
                pass
        if lack_key or wrong_key:
            print("头条V1.0 event=\"{event}\"：缺少关键字段：{key1}\n关键字段上报值错误：{key2}\nparam={param}\n".format(event=tag, key1=lack_key, key2=wrong_key, param=post))

def generate_filters():
    return [LiteV1Filter()]
