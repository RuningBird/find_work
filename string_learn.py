# 字符串连接
# a = '1'
# b = a+'23'
# print(a,b)
# import operator as ot
# s2 = ot.concat('456','123')
#
# # 字符串的截取
# s = '0123456789'
# print(s[1:5])

# # 字符串替换
# s1 = 'hello word wordword'
# s2 = s1.replace('word','yhr',2)
# print(s2)

# 字符串比较
# import operator as ot
# s1 = 'abc'
# s2 = 'acb'
# print('abc'<='ac')
# print(ot.eq(s1,s2))
# print(ot.lt(s1,s2))
# print(ot.le(s1,s2))
# # print(ot.le('a','a'))
# print(ot.gt(s1,s2))
# print(ot.ge(s1,s2))

# 字符串相加
# s1 = 'abc'
# s2 = s1+'4'
# print(s2)

# 字符串查找
# s1 = 'abc ac bd ac ac'
# print(s1.find('ac'))
# print(s1.rfind('ac'))
# print(s1.index('bd'))


# 字符串分割
# info = 'name:haha,age:20$name:python,age:30$name:fef,age:55'
# content = info.split('$')
# content2 = info.rsplit("$")
# print(content,'\n',content2)

# 字符串反转
# s1='abc'
# print(s1[::-1])
# print(id(s1),id(s1[::-1]))

# 字符串编码
# s1 = 'abc'
# print(s1.encode("utf-8").decode("GBK"))

# # 字符串拼接之一
# m = 'python2'
# astr = "i love %(python)s " % {'python':m}
# print(astr)

# 字符串复制
# s1 = 'abc'
# s3 = s1[::-1][::-1]
# print(s3,id(s1),id(s3))

