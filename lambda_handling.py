
data = [2, 3, 6, 7, 10]

# # filter
#
# new_data = list(filter(lambda x: (x % 2 == 0), data))
#
# print(new_data)

#
# # map
# #
# new_data = list(map(lambda x: x*2, data))
#
# print(new_data)


# # reduce

from functools import reduce

total = reduce(lambda x, y: (x+y), data)

print(total)

print(((((2+3)+6)+7)+10))


