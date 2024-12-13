


def data_structure_sum (data):
    total = 0
    if isinstance(data,(int, float)):
        total += data
    elif isinstance(data, str):
        total += len(data)
    elif isinstance(data,(list, set, tuple)):
        for item in data:
            total += data_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total += data_structure_sum(key)
            total+= data_structure_sum(value)
    return total

data_structure = [[1,2,3]], {'a': 4, 'b':5},(6, {'cube':7,'drum':8}), "Hello", ((), [{(2, 'Urban', ('Urban2',35))}])
result = data_structure_sum(data_structure)
print(result)