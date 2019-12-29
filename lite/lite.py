#!/usr/bin/python
# coding=utf-8

import json
import time
from timetransfer import TimeToDate
from filter import Filter

date = int(time.time())
date_str = TimeToDate().time_date2(date)

class Lite(Filter):

    def analyze(self, request):
        if not request or not request.valid():
            return False

        if request.query["app_name"] != "news_article_lite":
            return False

        return True


class LiteV1Filter(Lite):

    def analyze(self, request):

        if not super().analyze(request):
            return False

        post = json.loads(request.post)

        if not post or not isinstance(post, dict):
            return False

        tag = post.get("tag", "not exist")
        if tag == "not exist":
            return False

        """{"category_name":{}, "value":{}, "duration":{}, "percent":{}, "item_id":{}, "from_gid":{}, "label":{}, "ext_value":{}, }"""
        lack_key = []
        wrong_key = []

        event = ["go_detail", "video_play", "video_over", "stay_page"]
        if tag in event:
            keyphrase = ["label", "value", "item_id"]
            label_values = ["click_related", "click_headline", "click_category", "click_search", "click_video"]
            pos_values = ["detail","list"]
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

            if tag == "go_detail":
                pass

            if tag == "stay_page":
                ext_value = post.get("ext_value", "not exist")
                if ext_value == "not exist":
                    lack_key.append("ext_value")
                elif not ext_value:
                    wrong_key.append("ext_value")

            if tag == "video_play":
                position = post.get("position", "not exist")
                if position == "not exist":
                    lack_key.append("position")
                elif position not in pos_values:
                    wrong_key.append("position")

            if tag == "video_over":
                position = post.get("position", "not exist")
                if position == "not exist":
                    lack_key.append("position")
                else:
                    if position not in pos_values:
                        wrong_key.append("position")

                duration = post.get("duration", "not exist")
                if duration == "not exist":
                    lack_key.append("duration")
                else:
                    if not duration:
                        wrong_key.append("duration")

                percent = post.get("percent", "not exist")
                if percent == "not exist":
                    lack_key.append("percent")
                else:
                    if not percent:
                        wrong_key.append("percent")

        if tag == "navbar":
            label = post.get("label", "not exist")
            if label == "not exist":
                lack_key.append("label")
            elif not label:
                wrong_key.append("label")
        if lack_key or wrong_key:
            cont = "event：" + tag + "\n缺少关键字段：" + str(lack_key) + "\n关键字段上报值错误：" + str(wrong_key) + "\n" + str(
                post) + "\n\n"
            with open(r"/Users/gengliting/Documents/埋点/测试结果/测试结果_Litev1.0_{0}.txt".format(date_str), 'a') as f:
                f.write(cont)
#        if post.get("value") == "1652163094023278":
#            print(post,"\n")


def generate_filters():
    return [
        LiteV1Filter()
    ]
