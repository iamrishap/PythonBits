# func('ABC') -> ["ABC", "ACB", "BCA" ...]
result = []
length = 0


def permutations(input_string):
    # perm = ""
    if not input_string or len(input_string) == 0:
        return ''
    if len(input_string) == 1:
        return input_string
    for idx, char in enumerate(input_string):
        perm = ""
        perm += char
        starting_part = input_string[0:idx] if input_string[0:idx] else ''
        ending_part = input_string[idx + 1:] if input_string[idx + 1:] else ''
        perm += permutations(starting_part + ending_part)
        # print(perm)
        if not len(perm) == length:
            return perm
        else:
            result.append(perm)
    return result


input_string = "ABC"
length = len(input_string)
result = []
print(permutations(input_string))


# ABC

# input_string  ABC
# idx 0
# char A
# perm ABC

# input_string  BC
# idx 0
# char B
# perm BC

# input_string  C
# idx 0
# char C
# perm C


# ABCDE
# B + ACDE
# A       C
# CDE    ADE
# ACDE
