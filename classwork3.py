a = {123: 'abc'}
b = {1234: 'bca'}

def add_dict(a, b):

    a.update(b)

    return a

print(add_dict(a, b))





