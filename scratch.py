# lst = [[1, 2, 3],
#         [4, 5, 6]]
#
# lst[1][1]
#
# dct = {'first': {'one': 1, 'two': 2, 'three':3},
#         'second':{'four': 4, 'five': 5, 'six': 6}}
# #
# for key, value in dct.items():
#     print(value)
# #     print(str(key) + ': ' + str(value))
# #
# # lst_comp = [str(key) + ': ' + str(value) for key, value in dct.items()]
# # print(lst_comp)

# def group_by(iterable, key):
#     """Place each item in an iterable into a bucket based on calling the key
#     function on the item."""
#     group_to_items = {}
#     for item in iterable:
#         group = key(item)
#         if group not in group_to_items:
#             group_to_items[group] = []
#         group_to_items[group].append(item)
#     return group_to_items

total = 0
one = [1, 2, 3, 4, 5]
two = [5, 4, 3, 2]

for x in one:
    total += x * x

for x in two:
    total -= x * x

print(total)