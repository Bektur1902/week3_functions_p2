
a = input('Enter text: ')

def get_name(a):

    with open(a, 'w') as f:
        f.write('abc')

get_name(a)


