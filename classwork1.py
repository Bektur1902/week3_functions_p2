
def main():

    a = int(input('Enter number: '))
    b = int(input('Enter number: '))
    
    add(a, b)
    substract(a, b)
    multiple(a, b)
    divide(a , b)

def add(a, b):
    print('Сложение = ', a + b)

def substract(a, b):
    print('вычитание = ', a - b)

def multiple(a, b):
    print('умножение = ', a * b)

def divide(a, b):
    print('Деление = ', a / b)

main()

