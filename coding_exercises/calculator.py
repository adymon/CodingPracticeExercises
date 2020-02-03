"""
Make a calculator:

make_float = boolean which returns float if true or an integer if false
operation = which either 'add, subtract, multiply or divide'

first =  a number
second = another number
message = string that can be added


"""


def calculate(**kwargs):
    operations_set = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0)
    }

    is_float = kwargs.get('make_float', False)
    operation_search = operations_set[kwargs.get('operation','')]

    if is_float:
        result = print("The Result is", float(operation_search))

    else:
        result = print(f"{kwargs.get('message','')}, " + " The Result is", int(operation_search))

    return result


calculate(make_float=False, operation='add', message='You just added', first=100, second=20)
calculate(make_float=True, operation='divide', first=10.5, second=2)
