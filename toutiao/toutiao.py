#!/usr/bin/python
# coding=utf-8

import json
import time
from timetransfer import TimeToDate
from filter import Filter

date = int(time.time())
date_str = TimeToDate().time_date2(date)

class ToutiaoFilter(Filter):

    def analyze(self, request):
        if not request or not request.valid():
            return False

        if request.query["app_name"] != "news_article":
            return False

        return True


class ToutiaoV1Filter(ToutiaoFilter):
    file = "测试结果_头条v1.0_" + date_str + ".text"
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
            cont = "event："+tag+"\n缺少关键字段："+str(lack_key)+"\n关键字段上报值错误："+str(wrong_key)+"\n"+str(post)+"\n\n"
            with open(r"/Users/gengliting/Documents/埋点/测试结果/测试结果_头条v1.0_{0}.txt".format(date_str), 'a') as f:
                f.write(cont)

#        if post.get("value") == "1652163094023278":
#            print(post,"\n")


class ToutiaoV3Filter(ToutiaoFilter):
    def analyze(self, request):
        if not super().analyze(request):
            return False

        post = json.loads(request.post)
        if not post or not isinstance(post, dict):
            return False

        tag = post.get("event", "not exist")
        params = post.get("params", "not exist")

        if tag == "not exist":
            return False

        lack_key = []
        wrong_key = []
        event = ["go_detail", "video_play", "video_over", "stay_page", "video_play_auto", "video_over_auto"]
        if tag in event:
            keyphrase = ["category_name", "enter_from", "group_id", "item_id"]
            category_name_values = ["__all__", "video", "search","related", "tt_subv_inner_feed"]
            enter_from_values = ["click_headline", "click_category", "click_search", "click_related", "click_category"]
            pos_values = ["detail", "list"]
            dict_ec = dict(zip(enter_from_values, category_name_values))

            if params == "not exists":
                lack_key.append("params")
            elif not isinstance(params, dict):
                wrong_key.append("params")
            else:
                for key in keyphrase:
                    # 判断不缺少关键字
                    if key not in params.keys():
                        lack_key.append(key)
                        continue
                    # 判断关键字都有值
                    if not params[key]:
                        wrong_key.append(key)
                        continue

                    if key == "enter_from":
                        if params[key] not in enter_from_values:
                            wrong_key.append("enter_from")
                        else:
                            if (dict_ec[params[key]] != params["category_name"]) or (params["category_name"] not in category_name_values):
                                wrong_key.append("category_name")
                            if (params[key] == "click_related"):
                                if not params.get("from_id"):
                                    lack_key.append("from_gid")
                                elif not params["from_id"]:
                                    wrong_key.append(key)

            if tag == "go_detail":
                pass
            if tag == "stay_page":
                stay_time = params.get("stay_time", "not exist")
                if stay_time == "not exist":
                    lack_key.append("stay_time")
                page_type = params.get("page_type", "not exist")
                if page_type == "not exist":
                    lack_key.append("page_type")
                else:
                    if page_type != "video":
                        wrong_key.append("page_type")

            if tag == "video_paly":
                position = params.get("position", "not exist")
                if position == "not exist":
                    lack_key.append("position")
                elif position not in pos_values:
                    wrong_key.append("position")

            if tag == "video_over":
                position = params.get("position", "not exist")
                if position == "not exist":
                    lack_key.append("position")
                else:
                    if position not in pos_values:
                        wrong_key.append("position")

                duration = params.get("duration", "not exist")
                if duration == "not exist":
                    lack_key.append("duration")
                else:
                    if not duration:
                        wrong_key.append("duration")

                percent = params.get("percent", "not exist")
                if percent == "not exist":
                    lack_key.append("percent")
                else:
                    if not percent:
                        wrong_key.append("percent")

            if tag == "video_play_auto":
                root_git = params.get("root_git", "not exist")
                if root_git == "not exist":
                    lack_key.append("root_git")

                position = params.get("position", "not exist")
                if position == "not exist":
                    lack_key.append("position")
                else:
                    if position not in pos_values:
                        wrong_key.append("position")

            if tag == "video_over_auto":
                root_git = params.get("root_git", "not exist")
                if root_git == "not exist":
                    lack_key.append("root_git")

                position = params.get("position", "not exist")
                if position == "not exist":
                    lack_key.append("position")
                else:
                    if position not in pos_values:
                        wrong_key.append("position")

                duration = params.get("duration", "not exist")
                if duration == "not exist":
                    lack_key.append("duration")
                else:
                    if not duration:
                        wrong_key.append("duration")

                percent = params.get("percent", "not exist")
                if percent == "not exist":
                    lack_key.append("percent")
                else:
                    if not percent:
                        wrong_key.append("percent")

        if lack_key or wrong_key:
            cont = "event："+tag+"\n缺少关键字段："+str(lack_key)+"\n关键字段上报值错误："+str(wrong_key)+"\n"+str(post)+"\n\n"
            with open(r"/Users/gengliting/Documents/埋点/测试结果/测试结果_头条v3.0_{0}.txt".format(date_str), 'a') as f:
                f.write(cont)

#        if params.get("group_id") == "6767299150301151757":
#            print(post,"\n")
        

def generate_filters():
    return [
        ToutiaoV1Filter(),
        ToutiaoV3Filter()
    ]
