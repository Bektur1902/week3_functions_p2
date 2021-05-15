
eda = input('Какое блюдо желаете : ')
napitok = input('Какой напиток закажите : ')


def menu(a, b):

    with open('menu.txt', 'a') as f:
        f.writelines(a +' '+ b + '\n')

menu(eda, napitok)



