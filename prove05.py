

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

#원하는 글자 제거
s=s.replace(',','')
s=s.replace('.','')
s=s.replace('\n','')

#원하는 글자별로 나눠줌
s=s.split(' ')
#사진 생성
aDict=dict()


for i in range(0,len(s)):
    #소문자 대문자로
        s[i]=s[i].upper()
    #사전에 넣어서 키값으로 찾는다
        if s[i] in aDict:
            aDict[s[i]]+=1
        else:
            aDict[s[i]]=1

#중복 제거
s=list(set(s))
#정렬
s.sort()

for i in range(0,len(s)):
    print(s[i]+":"+str(aDict[s[i]]))
