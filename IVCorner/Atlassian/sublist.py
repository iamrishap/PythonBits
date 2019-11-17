b7dict = { 0: '0', 1: 'a', 2: 't', 3: 'l', 4: 's', 5: 'i', 6: 'n'}

# def convert(num):
#     pos_val = {}
#     pow = 0
#     pow_7 = 1
#     while num > 0:
#         while pow_7 < num:
#             pow_7 *= 7
#             pow += 1
#         pow_7 /= 7
#         for i in range(6, 0, -1):
#             if pow_7 * i < num:
#                 num -= pow_7
#                 pos_val[pow] = i
#                 break

def convert(num):
    pos_val = {}
    pow = 0
    pow_7 = 1
    if num == 1:
        print(1)
    while num > 0:
        while pow_7 < num:
            pow_7 *= 7
            pow += 1
        pow_7 /= 7
        for i in range(6, 0, -1):
            if pow_7 * i < num:
                num -= pow_7
                pos_val[pow] = i
                break
        pow_7 = 1
        pow = 0

    print(pos_val)

convert(8)
