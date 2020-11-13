# # d = {"a": 1, "b": 2}
# # d.update({"c":3})
# # print(d)

# # # or

# # d["d"] = 4


# # a = sum([x for x in d.values()]) 

# # # or

# # b = sum([d[x] for x in d])

# # # or

# # c = sum(d.values())


# # # 

# # e = {"a": 1, "b": 2, "c": 3}

# # for x,y in d.items():
# #   if y > 1:
# #     e.pop(x,y)

# # #or

# # f = dict((k,v) for k,v in e.items() if v <= 1)



# # print(a)
# # print(b)
# # print(c)
# # print(e)
# # print(f)

# d = {}

# d["a"] = [x for x in range(1,11)]
# d["b"] = [x for x in range(12,21)]
# d["c"] = [x for x in range(22,31)]

# print(d)

# # or simple 

# from pprint import pprint

# e = {"a": list(range(1,11)), "b": list(range(12,22)), "c": list(range(22,31))}

# pprint(e)

from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(f'b has value {d["b"]}')

for x,y in d.items():
  print(x, "has value", y)

