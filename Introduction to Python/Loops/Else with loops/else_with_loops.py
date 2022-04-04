i = 0
while i < 5:
    print('it\'s less than 5')
    i += 1
else:
    print('and now it\'s 5')  # Print this message when the condition is no longer True

for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("for loop is done")

print("Outside the for loop")


# for n in range(2, 10):      CHECK if you have any doubts regarding else statement with loops
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             # break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
