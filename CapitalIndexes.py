def capital_indexes(str):
    return [index for index, char in enumerate(str) if char.isupper()]

print(capital_indexes("HeLlO"))