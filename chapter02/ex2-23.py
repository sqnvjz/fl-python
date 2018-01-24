# from collections import deque
#
# dq = deque(range(10), maxlen=10)
#
# dq.rotate(-4)
# dq.appendleft(-3)
# dq.extend([20,30])
# dq.extendleft([40,50])
# print(dq)

l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
s = sorted(l, key=str)
print(s)