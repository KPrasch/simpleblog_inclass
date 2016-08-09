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

# string = 'The fence rocks across a community subsidiary. A valve fingers an the the acquaintance. A crystal the grabs the travelled caffeine throughout the hospital. The tone dips the joy throughout a marital evil. The revealed exposure offends inside a blasted crop.'
#
# def make_dict(text):
#     words = text.lower().split()
#     word_dict = {}
#
#     for word in words:
#         if word in word_dict:
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
#     print(word_dict)
#
# make_dict(string)


# def are_you_kidding_me_chris(text):
#     words = text.split()
#     word_dict = {}
#
#     for word in words:
#         if word in word_dict.keys():
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
#
#     print(word_dict)
#
# are_you_kidding_me_chris("It is true for all that that that that that that that refers to is not the same that that that that refers to.")


# def is_leap(year):
#     leap = False
#     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         leap = True
#
#     return leap
#
# print('***These are False***')
# print(is_leap(1800))
# print(is_leap(1900))
# print(is_leap(2100))
# print(is_leap(2200))
# print(is_leap(2300))
# print(is_leap(2500))
# print('***These are True***')
# print(is_leap(2000))
# print(is_leap(2400))
