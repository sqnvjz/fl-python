#
#
# class StrKeyDict0(dict):
#     def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str(key)]
#
#     def get(self, key, default=None):
#         try:
#             return self[key]
#         except KeyError:
#             return default
#
#     def __contains__(self, key):
#         return key in self.keys() or str(key) in self.keys()
#
#
# d = StrKeyDict0([('2', 'two'), ('4', 'four')])
# # print(d['1'])
# print(d.get(2))


import collections

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __setitem__(self, key, value):
        self.data[str(key)] = value

    def __contains__(self, key):
        return str(key) in self.keys()