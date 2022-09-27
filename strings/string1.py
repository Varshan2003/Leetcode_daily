def removeconsecutiveLetter(str1):
    str2=str1[0]
    for i in range(1,len(str1)):
        if str1[i] == str1[i-1]:
            continue
        else:
            str2=str2+str1[i]
    return str2
print(removeconsecutiveLetter("aabb"))