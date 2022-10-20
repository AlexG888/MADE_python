from collections import Counter


def find_anagrams(text: str, pattern: str):
    text_dict = Counter(text[: len(pattern) - 1])
    pattern_dict = Counter(pattern)
    start = 0
    result = []
    if pattern == "":
        return []
    for i in range(len(pattern) - 1, len(text)):
        text_dict[text[i]] += 1
        if text_dict == pattern_dict:
            result.append(start)
        text_dict[text[start]] -= 1
        if text_dict[text[start]] == 0:
            del text_dict[text[start]]
        start += 1
    return result
