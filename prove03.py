import os.path

s='/usr/local/bin/python'

filename=os.path.basename(s)
dirname=os.path.dirname(s)

s=s.split('/')

for i in range(1,len(s)):
    print("'"+s[i],end="'")
    if i != len(s)-1 :
        print("," , end="")
print()

print("'"+dirname,end="',")
print("'"+filename,end="'")