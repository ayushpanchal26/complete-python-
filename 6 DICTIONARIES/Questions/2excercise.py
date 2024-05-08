def word(s):
    dict2 = {}
    for i in s:
        dict2[i] = s.count(i)
    return dict2

print(word('ayushpanchal'))