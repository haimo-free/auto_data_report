# **coding = utf-8
post = {'category': 'umeng', 'aggr_type': '1', 'label': 'click_video', 'log_pb': {'impr_id': '2019121718081701001404703513023538', 'parent_group_id': '6767299150301151757', 'is_following': '0', 'parent_impr_id': '2019121718081701001404703513023538'}, 'category_id': 'xx', 'ext_value': '1652163094023278', 'article_type': 'video', 'has_zz_comment': '0', 'item_id': '6767299150301151757', 'value': '6767299150301151757', 'tag': 'go_detail', 'type': '1', 'author_id': '0', 'ab_sdk_version': '794527', 'sdk_dual_report': '0'}
tag = post.get("tag", "not exist")
if tag == "not exist":
    print("not exist")

if tag == "go_detail":
    print(post)
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
    if not lack_key and not wrong_key:
        print("存在错误：缺少关键字段：{key1},关键字段上报值错误：{key2}\nparam={param}".format(key1=lack_key, key2=wrong_key, param=post))
