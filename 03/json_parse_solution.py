import json


def keyword_callback():
    global cnt
    cnt += 1
    return cnt


def parse_json(keyword_callback, json_str: str, required_fields=None, keywords=None):
    if (len(json_str) != 0) and (len(required_fields) != 0) and (len(keywords) != 0):
        json_doc = json.loads(json_str)
        for key, value in json_doc.items():
            if key in required_fields:
                for v in value.split():
                    if v in keywords:
                        keyword_callback()
    else:
        print("Недостаточно данных!")


cnt = 0
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields = ["key1"]
keywords = ["word2"]
assert parse_json(keyword_callback, json_str, required_fields, keywords) is None
assert keyword_callback() == 1 + 1

cnt = 0
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields = []
keywords = ["word2"]
assert parse_json(keyword_callback, json_str, required_fields, keywords) is None
assert keyword_callback() == 0 + 1

cnt = 0
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields = ["key1"]
keywords = []
assert parse_json(keyword_callback, json_str, required_fields, keywords) is None
assert keyword_callback() == 0 + 1

cnt = 0
json_str = ""
required_fields = ["key1"]
keywords = ["word2"]
assert parse_json(keyword_callback, json_str, required_fields, keywords) is None
assert keyword_callback() == 0 + 1

cnt = 0
json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields = ["key1"]
keywords = ["word2", "Word1"]
assert parse_json(keyword_callback, json_str, required_fields, keywords) is None
assert keyword_callback() == 2 + 1

print("OK")
