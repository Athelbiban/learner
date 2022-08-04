# def run_something(saying):
#     def inner():
#         return 'We are say: "%s"' % saying
#     return inner
#
#
# a = run_something('Duck')
# b = run_something('Abracadabra')
#
# print(run_something('answer')())
# print(a)
# print(b())


# def my_range(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# print(my_range)
#
# ranger = my_range(1, 5)
# print(ranger)
#
# for x in ranger:
#     print(x)
# for try_again in ranger:
#     print(try_again)
# else:
#     print('Генератор истощился.')


# genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
# print(genobj)
#
# for thing in genobj:
#     print(thing)


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@square_it
@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))

# cooler_add_ints = document_it(add_ints)
# print(cooler_add_ints(4, 6))


