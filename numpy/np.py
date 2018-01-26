import numpy as np

# li = [1,2,3,4]
# l1 = np.array(li)
# # print(l1)
# l2 = [5,6,7,8]
# array_2 = np.array([l1, l2])
# print(array_2)
# print(array_2.shape)
# # print(l1.shape)
# print(array_2.dtype)
# a_4 = np.arange(1, 11)
# print(a_4)
# print(np.zeros([2,3]))
#
# print(np.eye(5).dtype)

# ab = np.random.randint(20, size=20).reshape(4, 5)
#
# # a = np.mat([[1,2,3], [4,5,6]])
# a = np.mat(ab)
# print(ab)
# print(max(ab[:,0]))

import pickle

a = np.arange(20)
b = np.arange(10)
# f = open('t.t', 'wb')
# pickle.dump(a, f)

# f = open('t.t', 'rb')
# b = pickle.load(f)
# print(b)

# np.save('m.pp', a)
# b = np.load('m.pp.npy')
# print(b)

# np.savez('mm', a=a, b=b)
m = np.load('mm.npz')
print(type(m[a]))