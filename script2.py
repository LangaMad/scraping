
data = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, 
        {}, {},
        {"key1": "value1"},
        {"key1": "value1"}, {"key2": "value2"}]

def remove_duplicate_dicts(input_list):
    seen = set()
    result = []

    for d in input_list:
        dict_str = str(d)
        
        if dict_str not in seen:
            seen.add(dict_str)
            result.append(d)

    return result


result = remove_duplicate_dicts(input_list=data)
print(result)

