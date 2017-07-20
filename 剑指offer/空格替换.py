def replaceBlank(string, num):
    l1 = list(string)
    s2 = []
    for i in l1:
        if i != ' ':
            s2.append(i)
        else:
            s2.append('%20')
    return ''.join(s2)


b = replaceBlank('hello word', 10)
print(b, len(b))

# s = "hello word"
# s1 = s.replace(' ','%20')
# print(s)
