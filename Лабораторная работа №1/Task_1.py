list_ = [6, 8, 4, 2, 7, 7, 1, None, 10]

sum_ = sum(list_[0:7]) + sum(list_[-1:])

len_ = len(list_)

list_[7] = sum_ / len_

print(list_)