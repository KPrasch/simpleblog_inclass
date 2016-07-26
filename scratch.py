# def trickySum(a,b,c):
#     intList = [a,b,c]
#     total = 0
#     for i in range(0,len(intList)):
#         if intList[i] == 13:
#             break
#         else:
#             total = total + intList[i]
#     print(total)
#
#
# def lucky_sum(a, b, c):
#   list = [a,b,c]
#   sum = 0
#   if 13 in list:
#      i = list.index(13)
#      for x in list[:i]:
#          sum += x
#   else:
#       sum = a + b + c
#   return sum
# 
# def lucky_sum(a, b, c):
#     lst = [a, b, c]
#     if 13 in lst:
#         return sum(lst[:lst.index(13)])
#     else:
#         return sum(lst)
#
#
# print(lucky_sum(13, 3, 3))
# print(lucky_sum(3, 13, 3))
# print(lucky_sum(3, 3, 13))
print(lucky_sum(3, 3, 3))
