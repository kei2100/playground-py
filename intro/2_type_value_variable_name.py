# set
s = {3, 5, 7}
d = s.difference({3, 5, 8})
print(d)
# {7}


# frozenset
f_set = frozenset({3, 5, 7})
print(f_set)
# frozenset({3, 5, 7})


# print keywords
help("keywords")

# list keywords
import keyword

k_list = keyword.kwlist
print(k_list)


print(type("hoge"))

print(type("hoge") == str)

print(isinstance("hoge", str))

# <class 'str'>
# True
# True


two = ni = 2
print(two, ni)
# 2 2


googol = 10 ** 100
print(googol)

print(googol * googol)