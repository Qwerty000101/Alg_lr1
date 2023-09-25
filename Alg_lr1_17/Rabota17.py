with open('17.txt',encoding="utf8") as file1:
    s=[int(x) for x in file1]
    arr=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if ((s[i]-s[j])%60==0) and ((s[i]%15==0) or (s[j]%15==0)):
                arr.append(s[i]-s[j])
print(len(arr),max(arr))
