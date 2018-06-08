def reverse(s):
    ret=""
    for i in range(len(s)-1,-1,-1):
        ret+=s[i]
        #print(s[i],end="")
    return ret

s=input("입력>")
print("결과>"+reverse(s))
