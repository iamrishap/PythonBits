def is_null_or_empty(val):
    '''
    Implements the equivalent of the C# IsNullOrEmpty Method for the String type
    :param val: string to check for null
    :return: True if null, False otherwise
    '''
    if val is None or val is "":
        return True
    else:
        return False


def get_divisors(num):
    '''
    Takes a single positive integer, and returns a List of integers, representing divisors of num.
    :param num: number to find divisors
    :return: List of divisors
    '''
    factors = []
    if num < 1:
        return None
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
    return factors


class InvalidTriangleException(Exception):
    '''
    Custom exception
    '''
    pass


def get_triangle_area(a, b, c):
    '''
    Finds the area of the triangle, using the length of the sides.
    :param a: Length of side a of the triangle
    :param b: Length of side a of the triangle
    :param c: Length of side a of the triangle
    :return: Area of the triangle, if the sides are legit
    '''
    if not isinstance(a, int) or not isinstance(a, int) or not isinstance(a, int):
        raise ValueError('Please enter integer inputs only.')
    if not a or not b or not c:
        raise InvalidTriangleException
    if a < 0 or b < 0 or c < 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise InvalidTriangleException
    else:
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def get_list_mode(val_list):
    '''
    Finds the mode(element(s) occuring maximum number of times) of the array.
    :param val_list: array of integral values
    :return: list of elements occuring maximum number of times
    '''
    # Importing module inside function is not a good practise. Used here to make the function standalone.
    from collections import defaultdict
    import random
    if not val_list:
        return None
    else:
        count_dict = defaultdict(int)
        for val in val_list:
            count_dict[val] += 1
        max_element = random.choice(list(count_dict.keys()))
        max_count = count_dict[max_element]
        for key, val in count_dict.items():
            if val > max_count:
                max_count = val
        list_mode = []
        for key, val in count_dict.items():
            if val == max_count:
                list_mode.append(key)
        return list_mode