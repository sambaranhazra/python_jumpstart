def calculate(**kw):
    is_float = kw.get("make_float")
    operation = kw.get("operation")
    first = kw.get('first')
    second = kw.get('second')
    message = kw.get('message')

    if operation == 'add':
        result = add(first, is_float, second)
    elif operation == 'subtract':
        result = subtract(first, is_float, second)
    elif operation == 'multiply':
        result = multiply(first, is_float, second)
    elif operation == 'divide':
        result = divide(first, is_float, second)
    if not message:
        message = "The result is"
    return "{} {}".format(message, result)


def divide(first, is_float, second):
    result = first / second
    if is_float:
        result = float(result)
    else:
        result = int(result)
    return result


def multiply(first, is_float, second):
    result = first * second
    if is_float:
        result = float(result)
    else:
        result = int(result)
    return result


def subtract(first, is_float, second):
    result = first - second
    if is_float:
        result = float(result)
    else:
        result = int(result)
    return result


def add(first, is_float, second):
    result = first + second
    if is_float:
        result = float(result)
    else:
        result = int(result)
    return result


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))  # "You just added 6"
