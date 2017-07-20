def find_count(s=""):
    if not len(s):
        return None

    i = num = str_num = other = 0
    while i < len(s):
        if s[i].isnumeric():
            while i < len(s) and s[i].isnumeric():
                i += 1
            num += 1
        elif s[i].isalpha():
            while i < len(s) and s[i].isalpha():
                i += 1
            str_num += 1
        else:
            while i < len(s) and not s[i].isnumeric() and not s[i].isalpha():
                i += 1
            other += 1
    print(num, str_num, other)


s = "11ab##11"
find_count(s)
