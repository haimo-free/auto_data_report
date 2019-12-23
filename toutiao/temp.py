# **coding = utf-8
'''
post = {'category': 'umeng', 'aggr_type': '1', 'label': 'click_video', 'log_pb': {'impr_id': '2019121718081701001404703513023538', 'parent_group_id': '6767299150301151757', 'is_following': '0', 'parent_impr_id': '2019121718081701001404703513023538'}, 'category_id': 'xx', 'ext_value': '1652163094023278', 'article_type': 'video', 'has_zz_comment': '0', 'item_id': '6767299150301151757', 'value': '6767299150301151757', 'tag': 'go_detail', 'type': '1', 'author_id': '0', 'ab_sdk_version': '794527', 'sdk_dual_report': '0'}
tag = post.get("tag", "not exist")
if tag == "not exist":
    print("not exist")

if tag == "go_detail":
    keyphrase = {"label": {}, "value": {}, "item_id": {}, "from_gid": {}, "aaaa": {}}
    label_values = ["click_related", "click_headline", "click_category", "click_search"]
    lack_key = []
    wrong_key = []
    for key in keyphrase.keys():
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
    if lack_key != [] or wrong_key != []:
        print("存在错误：缺少关键字段：{key1},关键字段上报值错误：{key2}\nparam={param}".format(key1=lack_key, key2=wrong_key, param=post))
'''

post={'ab_sdk_version': '794527', 'sdk_dual_report': '0', 'event': 'go_detail', 'type': '1', 'params':{'aggr_type': '1', 'enter_from': 'click_category', 'log_pb':{'impr_id': '2019121718081701001404703513023538', 'parent_group_id': '6767299150301151757', 'is_following': '0', 'parent_impr_id': '2019121718081701001404703513023538'}, 'category_id': 'xx', 'group_type': 'video', 'article_type': 'video', 'has_zz_comment': '0',  'author_id': '0', 'category_name': 'category', '_staging_flag': '1', 'ad_id': '1652163094023278'}}
if not post or not isinstance(post, dict):
    print("error")

event = post.get("event", "not exist")
params = post.get("params", "not exist")
print(type(params))
print(params)
if event == "not exist":
    print("not exist")
if event == "go_detail":
    keyphrase = ["category_name", "enter_from", "group_id", "item_id"]
    category_name_values = ["__all__", "video", "search", "related"]
    enter_from_vaules = ["click_headline", "click_category", "click_search", "click_related"]
    dict_ec = dict(zip(enter_from_vaules, category_name_values))
    print(dict_ec)
    lack_key = []
    wrong_key = []

    if params == "not exists":
        lack_key.append("params")
    elif not isinstance(params, dict):
        wrong_key.append("params")
    else:
        for key in keyphrase:
            '''判断不缺少关键字'''
            if key not in params.keys():
                lack_key.append(key)
                continue
            '''判断关键字都有值'''
            if not params[key]:
                wrong_key.append(key)
                continue
            '''判断category_name取值不为空'''
            if key == "category_name":
                if params[key] not in category_name_values:
                    lack_key.append(key)
            '''判断category_name和enter_from对应关系正确'''
            if dict_ec[params["enter_from"]] != params["category_name"]:
                wrong_key.append("category")
            '''判断相关视频的go_detail上报扩展字段from_gid'''
            if key == "enter_from":
                if params[key] not in enter_from_vaules:
                    lack_key.append(key)
                elif params[key] == "click_related":
                    if not params.get("from_id"):
                        lack_key.append("from_gid")
                    elif not params["from_id"]:
                        wrong_key.append(key)
    if not lack_key or not wrong_key:
        print("头条V3.0 event=\"{event}\"有错误：\n缺少关键字段：{key1}\n关键字段上报值错误：{key2}\nparam={param}".format(event=event, key1=lack_key, key2=wrong_key, param=post))
