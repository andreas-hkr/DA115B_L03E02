def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calculate(arg1, arg2, function):
    return function(float(arg1), float(arg2))


def main():
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    print('Please write a mathematical expression:')
    print('For example 1 + 2, or 2 * 3.')
    parts = input('>>> ').split()
    first, op, second = input('>>>').split()

    first_num = float(parts[0])
    operator = parts[1]
    second_num = float(parts[2])

    print(f'Result is {calculate(first_num, second_num, operators[operator])}')
    print(f'Result is {calculate(first, second, operators[op])}')
    print(globals()['add'](1, 2))


if __name__ == '__main__':
    main()
