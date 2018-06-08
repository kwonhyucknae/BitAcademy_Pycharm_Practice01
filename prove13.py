
num=int(input("숫자를 입력하세요:"))
ans=0
if num % 2 ==0 :
    for i in range(1,num+1):
        if i % 2 ==0 :
            ans+=i
else:
    for i in range(1,num+1):
        if i%2 ==1:
            ans+=i

print(ans)