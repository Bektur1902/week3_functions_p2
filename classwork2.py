
len_text = input('Enter text: ')

def text(len_text):

    count = 0
    for i in len_text:
        count += 1
    return count


print('Количество букв в предложении: ', text(len_text))
    
    
