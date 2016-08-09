

# int value: 0=no ticket,
# 1=small ticket,
# 2=big ticket. If speed is 60 or less, the result is 0.
# If speed is between 61 and 80 inclusive, the result is 1. If speed is 81
# or more, the result is 2. Unless it is your birthday -- on that day, your
# speed can be 5 higher in all cases.

# def ticket(speed, birthday):
#     ticket = 0
#     if birthday:
#         if speed > 65 and speed <= 85:
#             ticket = 1
#         elif speed > 85:
#             ticket = 2
#     else:
#         if speed > 60 and speed <= 80:
#             ticket = 1
#         elif speed > 80:
#             ticket = 2
#     return ticket

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a
# boolean indicating if we are on vacation, return a string of the form
# "7:00" indicating when the alarm clock should ring. Weekdays, the alarm
# should be "7:00" and on the weekend it should be "10:00". Unless we are
# on vacation -- then on weekdays it should be "10:00" and weekends it
# should be "off".

# def alarm(day, vacation):
#     time = ""
#     if vacation:
#         if day in [0, 6]:
#             time = 'OFF'
#         elif day in list(range(1,6)):
#             time = '10:00'
#     else:
#         if day in [0, 6]:
#             time = '10:00'
#         elif day in list(range(1,6)):
#             time = '7:00'
#     return time

# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# def len(thing):
#     count = 0
#     for i in thing:
#         count += 1
#     return count
#
# print(len('hello'))

# def reverse(string):
#     return string[::-1]

# test = "The disclaimer steams the complex. The joy assesses a stamp. The gasp labels the relative controversy. The graduated festival picks whatever sundry sky. Why won't the dish best the guitar? How will a honey tear beside the devastating principal?"
#
# def word_sort(text):
#     word_dict = {}
#     words = text.lower().split()
#     for word in words:
#         if word in word_dict:
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
#
#     return word_dict
#
# print(word_sort(test))
