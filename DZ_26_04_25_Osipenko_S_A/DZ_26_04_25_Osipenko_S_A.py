
n = [-2, 3, 8, -11, -4, 6]


def neg_num(lst):
    if len(lst) == 0:
        return 0
    else:
        count = neg_num(lst[1:])
        if lst[0] < 0:
            count += 1
    return count


print("n = ", neg_num(n))
