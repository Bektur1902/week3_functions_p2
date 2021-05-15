
a = {123: 'asd', 1234: 'abc'}

def take_tuples(a):

    keys = set(a.keys())

    values = set(a.values())

    return keys, values

print(take_tuples(a))

